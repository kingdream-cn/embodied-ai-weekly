import { createContentLoader } from 'vitepress'

export default createContentLoader('issues/*.md', {
  transform(raw) {
    return raw
      .filter((p) => p.url !== '/issues/')
      .sort((a, b) => new Date(b.frontmatter.date ?? 0) - new Date(a.frontmatter.date ?? 0))
      .map((p) => ({
        title: p.frontmatter.title,
        date: p.frontmatter.date,
        description: p.frontmatter.description,
        tags: p.frontmatter.tags ?? [],
        cover: p.frontmatter.cover,
        url: p.url,
      }))
  },
})