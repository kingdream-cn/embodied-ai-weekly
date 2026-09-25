import { writeFileSync } from 'node:fs'
import { join } from 'node:path'

function escapeXml(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;')
}

/**
 * 依据 transformPageData 收集的页面元数据生成 RSS 2.0，输出到 outDir/feed.xml。
 * 绝对地址由环境变量 SITE_URL(站点根) + BASE(部署路径) 组成。
 */
export function generateFeed(siteConfig, pages) {
  const base = process.env.BASE || '/'
  const siteUrl = (process.env.SITE_URL || 'https://example.com').replace(/\/+$/, '')

  const posts = (pages || [])
    .filter(
      (p) =>
        p.relativePath &&
        p.relativePath.startsWith('issues/') &&
        !p.relativePath.endsWith('/index.md') &&
        p.frontmatter?.title
    )
    .sort(
      (a, b) =>
        new Date(b.frontmatter?.date || 0) - new Date(a.frontmatter?.date || 0)
    )

  const items = posts
    .map((p) => {
      const fm = p.frontmatter || {}
      const rel = p.relativePath.replace(/\.md$/, '') + '.html'
      const url = `${siteUrl}${base}${rel}`
      const date = fm.date ? new Date(fm.date) : new Date()
      return [
        '    <item>',
        `      <title>${escapeXml(fm.title)}</title>`,
        `      <link>${escapeXml(url)}</link>`,
        `      <guid isPermaLink="true">${escapeXml(url)}</guid>`,
        `      <pubDate>${date.toUTCString()}</pubDate>`,
        `      <description>${escapeXml(fm.description || '')}</description>`,
        '    </item>',
      ].join('\n')
    })
    .join('\n')

  const channelLink = `${siteUrl}${base}`

  const feed = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
    '  <channel>',
    '    <title>具身智能周刊 Embodied AI Weekly</title>',
    `    <link>${escapeXml(channelLink)}</link>`,
    '    <description>Embodied AI Weekly — 每周追踪具身智能前沿进展</description>',
    '    <language>zh-CN</language>',
    `    <atom:link href="${escapeXml(channelLink)}feed.xml" rel="self" type="application/rss+xml" />`,
    items,
    '  </channel>',
    '</rss>',
  ].join('\n')

  writeFileSync(join(siteConfig.outDir, 'feed.xml'), feed, 'utf-8')
}