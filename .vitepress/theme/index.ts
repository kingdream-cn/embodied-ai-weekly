import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import './style.css'
import IssuesGrid from './components/IssuesGrid.vue'
import MediaEmbed from './components/MediaEmbed.vue'

const theme: Theme = {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('IssuesGrid', IssuesGrid)
    app.component('MediaEmbed', MediaEmbed)
  },
}

export default theme