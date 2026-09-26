import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import './style.css'
import IssuesGrid from './components/IssuesGrid.vue'

const theme: Theme = {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('IssuesGrid', IssuesGrid)
  },
}

export default theme