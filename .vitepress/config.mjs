import { defineConfig } from 'vitepress'
import container from 'markdown-it-container'

export default defineConfig({
  // 网站标题/描述
  title: '具身智能周刊',
  description: 'Embodied AI Weekly — 追踪具身智能、人形机器人、灵巧操作与自主导航的前沿进展',
  lang: 'zh-CN',
  lastUpdated: true,

  // 极简黑客科技风：强制暗色终端模式
  appearance: 'force-dark',

  // GitHub Pages 项目站点部署路径（owner.github.io/embodied-ai-weekly/）
  base: '/embodied-ai-weekly/',

  // 显式指定构建输出目录，与 GitHub Actions 上传路径保持一致
  outDir: 'dist',

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/logo.svg' }],
    ['meta', { name: 'theme-color', content: '#00e599' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: '具身智能周刊' }],
    ['meta', { property: 'og:description', content: 'Embodied AI Weekly — 每周追踪具身智能前沿进展' }],
  ],

  // 导航栏
  themeConfig: {
    logo: '/logo.svg',
    nav: [
      { text: '首页', link: '/' },
      { text: '往期周刊', link: '/issues/' },
    ],

    // 侧边栏
    sidebar: [
      {
        text: '导航',
        items: [
          { text: '首页', link: '/' },
          { text: '往期周刊', link: '/issues/' },
        ],
      },
    ],

    // 站内全文搜索（本地索引）
    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: '搜索', buttonAriaLabel: '搜索' },
          modal: {
            noResultsText: '没有找到相关结果',
            resetButtonTitle: '清除查询',
            footer: { selectText: '选择', navigateText: '切换' },
          },
        },
      },
    },

    outline: { level: [2, 3], label: '本页目录' },
    docFooter: { prev: '上一篇', next: '下一篇' },
    lastUpdatedText: '最近更新',
  },

  markdown: {
    theme: { light: 'github-light', dark: 'github-dark' },

    // 允许容器内的标题进入右侧大纲（周刊条目标题写在 ::: card 内）
    headers: { shouldAllowNested: true },

    config(md) {
      // 「要点卡片」自定义容器：::: key-points
      md.use(container, 'key-points', {
        render(tokens, idx) {
          const token = tokens[idx]
          if (token.nesting === 1) {
            return '<div class="key-points">\n'
          }
          return '</div>\n'
        },
      })

      // 周刊条目卡片容器：::: card [板块标识]
      // 板块标识（insight / tutorial / opensource / practice / paper）决定卡片配色
      md.use(container, 'card', {
        render(tokens, idx) {
          const token = tokens[idx]
          if (token.nesting === 1) {
            const kind = token.info.trim().split(/\s+/)[1]
            return `<div class="news-card${kind ? ` card-${kind}` : ''}">\n`
          }
          return '</div>\n'
        },
      })
    },
  },
})