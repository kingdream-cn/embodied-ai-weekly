<script setup>
import { data as posts } from '../issues.data'

function fmt(s) {
  if (!s) return ''
  const d = new Date(s)
  if (Number.isNaN(d.getTime())) return s
  return `${d.getUTCFullYear()}.${String(d.getUTCMonth() + 1).padStart(2, '0')}.${String(d.getUTCDate()).padStart(2, '0')}`
}
</script>

<template>
  <div class="issues-grid">
    <a v-for="p in posts" :key="p.url" :href="p.url" class="issue-card">
      <div v-if="p.cover" class="cover" :style="{ backgroundImage: `url(${p.cover})` }"></div>
      <div class="card-body">
        <div class="card-meta">
          <time>{{ fmt(p.date) }}</time>
          <span v-for="t in p.tags" :key="t" class="tag">{{ t }}</span>
        </div>
        <h3 class="card-title">{{ p.title }}</h3>
        <p class="card-desc">{{ p.description }}</p>
      </div>
    </a>
  </div>
</template>