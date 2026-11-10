import { createContentLoader } from 'vitepress'

// 非法或缺失的日期统一按 0 处理，避免 NaN 参与比较导致排序结果不稳定
function toTimestamp(value: unknown): number {
  const time = new Date(value as string | number | Date).getTime()
  return Number.isNaN(time) ? 0 : time
}

export default createContentLoader('issues/*.md', {
  transform(raw) {
    return raw
      .filter((p) => p.url !== '/issues/')
      .map((p) => ({
        title: p.frontmatter.title,
        date: p.frontmatter.date,
        description: p.frontmatter.description,
        tags: Array.isArray(p.frontmatter.tags) ? p.frontmatter.tags : [],
        cover: p.frontmatter.cover,
        url: p.url,
      }))
      .sort(
        (a, b) =>
          toTimestamp(b.date) - toTimestamp(a.date) || b.url.localeCompare(a.url),
      )
  },
})
