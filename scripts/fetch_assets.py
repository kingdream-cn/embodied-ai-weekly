#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
外链媒体本地化抓取脚本（issue-39 专用）

用法:
    python3 scripts/fetch_assets.py                  # 全量抓取并输出报告
    python3 scripts/fetch_assets.py --only digit-5   # 只抓某一条
    python3 scripts/fetch_assets.py --refresh-images # 即使已有本地图也重新抓取

设计约束（对应「人机协作异常兜底」要求）:
  - 每个 URL 最多请求 1 次 + 1 次重试，绝不死循环重试
  - 只有通过 PIL 校验（可解码、尺寸达标、体积达标）的真实图片才会落盘，
    绝不会生成空文件或损坏的伪占位文件
  - 命中人机验证 / 反爬 / 需登录 / 内容已删除时，立即把该条标记为 blocked
    并继续处理下一条，不阻塞整体流程
"""

import argparse
import io
import json
import os
import re
import sys
import time
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(ROOT, "public", "images", "issue-39")
VIDEO_DIR = os.path.join(ROOT, "public", "videos", "issue-39")
DEBUG_DIR = "/tmp/fetch_assets_debug"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
# 关键：置空 Referer，绕过微信 mmbiz.qpic.cn 等图床的防盗链
HEADERS = {
    "User-Agent": UA,
    "Referer": "",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

TIMEOUT = 25
MIN_IMG_BYTES = 15 * 1024      # 小于 15KB 的"配图"基本是图标/头像
MIN_IMG_SIDE = 400             # 最短边门槛
MIN_VIDEO_BYTES = 200 * 1024   # 小于 200KB 的视频视为异常/空响应
MAX_CANDIDATES = 8             # 每条最多尝试下载的图片候选数

# 反爬 / 人机验证 / 需登录 特征串 -> 受限原因
BLOCK_MARKERS = [
    ("环境异常", "触发微信环境异常校验（需在微信客户端或真人会话中打开）"),
    ("完成验证后即可继续访问", "需要人机验证"),
    ("去验证", "需要人机验证"),
    ("请在微信客户端打开链接", "仅限微信客户端内打开"),
    ("该内容已被发布者删除", "源内容已被删除"),
    ("此内容因违规无法查看", "源内容已被平台屏蔽"),
    ("系统繁忙，请稍后再试", "接口限流"),
    ("参数错误", "链接签名已失效（微信带时效签名）"),
    ("Just a moment", "Cloudflare 人机验证"),
    ("Enable JavaScript and cookies to continue", "Cloudflare JS 校验"),
    ("Attention Required! | Cloudflare", "Cloudflare 拦截"),
    ("滑动验证", "滑块验证拦截"),
    ("captcha", "验证码拦截"),
    ("登录后", "需要登录后查看"),
]

# 无用图特征（头像、图标、二维码、广告位等）
JUNK_IMG_PATTERNS = [
    "avatar", "logo", "icon", "qrcode", "qr_code", "favicon", "emoji",
    "sprite", "badge", "blank", "spacer", "1x1", "loading", "placeholder",
    "wx_fmt=gif", "/common/", "share_", "guide", "arrow", "btn_",
]

IMG_EXT_RE = re.compile(r"https?://[^\s\"'\\<>()]+?\.(?:jpe?g|png|webp|gif)(?:\?[^\s\"'\\<>()]*)?", re.I)
VIDEO_URL_RE = re.compile(r"https?:\\?/\\?/[^\s\"'\\<>]+?\.(?:mp4|m3u8)[^\s\"'\\<>]*", re.I)

TARGETS = [
    {
        "id": "zhiyuan-a3",
        "label": "第 1 条 · 智元远征 A3 Ultra（今日头条 + 微信专栏）",
        "image": "zhiyuan-a3.png",
        "urls": [
            "https://www.toutiao.com/article/7686296704445940274/?utm_source=gemini",
            "https://mp.weixin.qq.com/s?src=11&timestamp=1789951685&ver=6979&signature=luPsj4JCR-MKIZtV3Eb69LrTae11LP0hB9VE48XLd-hic4aITlZ7dq*clvYDAQ8Bc*f9q3SDyVSsJRKgMUWjPHs*hlLSFEUdPZyfYBSljT4pR0nJXweu8tGvFM16Em31&new=1&utm_source=gemini",
        ],
    },
    {
        "id": "anu-six-models",
        "label": "第 2 条 · 安努智能全栈六模型（微信公众号）",
        "image": "anu-six-models.png",
        "urls": ["https://mp.weixin.qq.com/s/c8RWwl_nSpzlunxe9HgOvQ?utm_source=gemini"],
    },
    {
        "id": "digit-5",
        "label": "第 3 条 · Agility Digit 5（The Robot Report）",
        "image": "digit-5.png",
        "urls": [
            "https://www.therobotreport.com/agilitys-digit-5-humanoid-has-new-legs-batteries-safety-upgrades/?utm_source=gemini"
        ],
    },
    {
        "id": "typesafe-jev",
        "label": "第 4 条 · TypeSafe System One Jev（微信公众号）",
        "image": "typesafe-jev.png",
        "urls": ["https://mp.weixin.qq.com/s/DNr2E1OW63GO0v9dMsrvSA?utm_source=gemini"],
    },
    {
        "id": "motor-drive",
        "label": "教程 1 · 电机与减速器全解析（CSDN）",
        "image": "motor-drive.png",
        "urls": ["https://blog.csdn.net/m0_63284825/article/details/162054649?utm_source=gemini"],
    },
    {
        "id": "brain-vla-wm",
        "label": "教程 2 · LLM / VLA / WM 科普（抖音短视频）",
        "image": "brain-vla-wm.png",
        "video": "brain-vla-wm.mp4",
        "urls": ["https://v.douyin.com/XX64wj1A3ZA/?utm_source=gemini"],
    },
]


def log(msg):
    print(msg, flush=True)


def ensure_dirs():
    for d in (IMG_DIR, VIDEO_DIR, DEBUG_DIR):
        os.makedirs(d, exist_ok=True)


def fetch(url):
    """单次请求 + 至多一次重试。返回 (resp, error_reason)。"""
    for attempt in (1, 2):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
            return resp, None
        except requests.RequestException as exc:
            if attempt == 2:
                return None, f"网络请求失败：{type(exc).__name__}: {exc}"
            time.sleep(2)
    return None, "网络请求失败"


def detect_block(resp, html):
    """识别反爬/人机验证。返回受限原因或 None。"""
    if resp.status_code in (401, 403, 418, 429, 451):
        return f"HTTP {resp.status_code} 反爬拦截"
    if resp.status_code >= 500:
        return f"HTTP {resp.status_code} 源站异常"
    lowered = html[:200000]
    for marker, reason in BLOCK_MARKERS:
        if marker.lower() in lowered.lower():
            return reason
    if len(html) < 2000:
        return f"响应体仅 {len(html)} 字节，内容为空壳页"
    return None


def is_junk_image(url):
    low = url.lower()
    return any(p in low for p in JUNK_IMG_PATTERNS)


def collect_image_candidates(soup, raw_html, base_url):
    """按优先级收集候选图：og:image > 正文容器内 img > 全页 img > 裸正则兜底。"""
    ordered = []

    def push(u):
        if not u:
            return
        u = urljoin(base_url, u.strip())
        if not u.startswith("http"):
            return
        if u not in ordered:
            ordered.append(u)

    for meta in soup.find_all("meta"):
        prop = (meta.get("property") or meta.get("name") or "").lower()
        if prop in ("og:image", "twitter:image", "og:image:secure_url"):
            push(meta.get("content"))

    body_selectors = [
        "div.rich_media_content",
        "div#js_content",
        "div#content_views",
        "div.article-content",
        "article",
        "div.entry-content",
        "div.post-content",
        "div#content",
    ]
    for sel in body_selectors:
        node = soup.select_one(sel)
        if not node:
            continue
        for tag in node.find_all(["img", "source"]):
            push(tag.get("data-src") or tag.get("src") or tag.get("data-original"))

    for tag in soup.find_all("img"):
        push(tag.get("data-src") or tag.get("src") or tag.get("data-original"))

    if not ordered:
        for m in IMG_EXT_RE.findall(raw_html):
            push(m.replace("\\u002F", "/").replace("\\/", "/"))

    return [u for u in ordered if not is_junk_image(u) and not u.startswith("data:")]


def download_image(url):
    """下载并用 PIL 校验；通过则返回 (png_bytes, w, h)，否则返回 (None, 原因)。"""
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    except requests.RequestException as exc:
        return None, f"下载失败 {type(exc).__name__}"
    if r.status_code != 200:
        return None, f"HTTP {r.status_code}"
    if len(r.content) < MIN_IMG_BYTES:
        return None, f"体积过小 {len(r.content) // 1024}KB"
    try:
        img = Image.open(io.BytesIO(r.content))
        img.load()
    except Exception as exc:
        return None, f"非有效图片 {type(exc).__name__}"
    w, h = img.size
    if min(w, h) < MIN_IMG_SIDE:
        return None, f"尺寸过小 {w}x{h}"
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")
    buf = io.BytesIO()
    img.save(buf, "PNG", optimize=True)
    return buf.getvalue(), (w, h)


def extract_video_urls(raw_html, soup):
    urls = []
    for tag in soup.find_all("video"):
        for s in tag.find_all("source"):
            if s.get("src"):
                urls.append(urljoin("", s["src"]))
        if tag.get("src"):
            urls.append(tag["src"])
    for m in VIDEO_URL_RE.findall(raw_html):
        u = m.replace("\\u002F", "/").replace("\\/", "/")
        if u not in urls:
            urls.append(u)
    return urls


def download_video(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=60, stream=True)
    except requests.RequestException as exc:
        return None, f"下载失败 {type(exc).__name__}"
    if r.status_code != 200:
        return None, f"HTTP {r.status_code}"
    data = b""
    for chunk in r.iter_content(65536):
        data += chunk
        if len(data) > 60 * 1024 * 1024:
            break
    if len(data) < MIN_VIDEO_BYTES:
        return None, f"体积过小 {len(data) // 1024}KB（可能为空响应）"
    if b"ftyp" not in data[:64] and "video" not in r.headers.get("Content-Type", ""):
        return None, "响应不是有效视频流"
    return data, None


def process_target(target):
    tid = target["id"]
    result = {
        "id": tid,
        "label": target["label"],
        "status": "blocked",
        "reason": "",
        "source_url": "",
        "page_title": "",
        "image": None,
        "image_dim": "",
        "video": None,
        "candidates_tried": 0,
    }

    for url in target["urls"]:
        log(f"\n>>> [{tid}] GET {url[:110]}")
        resp, err = fetch(url)
        if err:
            result["reason"] = err
            continue

        html = resp.text or ""
        host = urlparse(resp.url).netloc
        log(f"    HTTP {resp.status_code}  {len(html)} bytes  -> {host}")
        with open(os.path.join(DEBUG_DIR, f"{tid}.html"), "w", encoding="utf-8") as fh:
            fh.write(html)

        blocked = detect_block(resp, html)
        if blocked:
            result["reason"] = blocked
            log(f"    BLOCKED: {blocked}")
            continue

        soup = BeautifulSoup(html, "lxml")
        result["source_url"] = resp.url
        result["page_title"] = (soup.title.get_text(strip=True) if soup.title else "")

        # ---- 图片 ----
        if target.get("image") and not result["image"]:
            cands = collect_image_candidates(soup, html, resp.url)
            log(f"    图片候选 {len(cands)} 个")
            for cand in cands[:MAX_CANDIDATES]:
                result["candidates_tried"] += 1
                data, why = download_image(cand)
                if data:
                    abs_path = os.path.join(IMG_DIR, target["image"])
                    with open(abs_path, "wb") as fh:
                        fh.write(data)
                    result["image"] = f"public/images/issue-39/{target['image']}"
                    result["image_dim"] = f"{why[0]}x{why[1]}"
                    log(f"    ✔ 图片已保存 {target['image']} {result['image_dim']} {len(data)//1024}KB")
                    break
                log(f"      ✗ 弃用候选（{why}） {cand[:100]}")

        # ---- 视频 ----
        if target.get("video") and not result["video"]:
            vurls = extract_video_urls(html, soup)
            log(f"    视频候选 {len(vurls)} 个")
            if vurls:
                data, why = download_video(vurls[0])
                if data:
                    abs_path = os.path.join(VIDEO_DIR, target["video"])
                    with open(abs_path, "wb") as fh:
                        fh.write(data)
                    result["video"] = f"public/videos/issue-39/{target['video']}"
                    log(f"    ✔ 视频已保存 {target['video']} {len(data)//1024}KB")
                else:
                    log(f"      ✗ 视频不可用（{why}）")
                    result["reason"] = result["reason"] or f"视频流不可直连下载（{why}）"
            else:
                result["reason"] = result["reason"] or "页面为 JS 动态渲染，静态 HTML 中无公开视频直链"

        if result["image"] or (target.get("video") and result["video"]):
            result["status"] = "ok"
            break

    if result["status"] != "ok" and not result["reason"]:
        result["reason"] = "未找到通过质量校验的媒体资源"
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", help="只处理指定 id")
    args = parser.parse_args()

    ensure_dirs()
    targets = [t for t in TARGETS if not args.only or t["id"] == args.only]
    if not targets:
        log(f"未找到条目: {args.only}")
        return 1

    log("=" * 72)
    log("外链媒体本地化抓取开始")
    log(f"图片目录: {IMG_DIR}")
    log(f"视频目录: {VIDEO_DIR}")
    log("=" * 72)

    results = []
    for t in targets:
        results.append(process_target(t))
        time.sleep(1.5)

    report_path = os.path.join(DEBUG_DIR, "report.json")
    with open(report_path, "w", encoding="utf-8") as fh:
        json.dump(results, fh, ensure_ascii=False, indent=2)

    log("\n" + "=" * 72)
    log("抓取结果汇总")
    log("=" * 72)
    ok = [r for r in results if r["status"] == "ok"]
    blocked = [r for r in results if r["status"] != "ok"]
    for r in results:
        flag = "OK     " if r["status"] == "ok" else "BLOCKED"
        log(f"[{flag}] {r['label']}")
        log(f"          图片: {r['image'] or '未获取'} {r['image_dim']}")
        log(f"          视频: {r['video'] or '未获取'}")
        if r["status"] != "ok":
            log(f"          受限原因: {r['reason']}")
    log(f"\n成功 {len(ok)} 条 / 受限 {len(blocked)} 条")
    log(f"详细报告: {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())