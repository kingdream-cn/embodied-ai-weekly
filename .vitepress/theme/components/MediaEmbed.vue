<script setup>
defineProps({
  src: { type: String, required: true },
  title: { type: String, default: '' },
  ratio: { type: String, default: '16 / 9' },
})

function kind(src) {
  if (/\.(mp4|webm|mov|m3u8)(\?|$)/i.test(src)) return 'video'
  if (/\.(gif|png|jpe?g|webp|avif)(\?|$)/i.test(src)) return 'img'
  return 'iframe'
}
</script>

<template>
  <figure class="media-embed" :style="{ aspectRatio: ratio }">
    <video v-if="kind(src) === 'video'" :src="src" controls playsinline preload="metadata"></video>
    <img v-else-if="kind(src) === 'img'" :src="src" :alt="title" loading="lazy" />
    <iframe v-else :src="src" :title="title" allowfullscreen allow="autoplay; encrypted-media; picture-in-picture"></iframe>
    <figcaption v-if="title">{{ title }}</figcaption>
  </figure>
</template>