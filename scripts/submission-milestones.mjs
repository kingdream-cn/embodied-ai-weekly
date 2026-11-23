const week = 7 * 24 * 60 * 60 * 1000;
const firstStart = Date.parse('2026-11-14T15:00:00+08:00');
const dateTime = new Intl.DateTimeFormat('sv-SE', {
  timeZone: 'Asia/Shanghai', dateStyle: 'short', timeStyle: 'short',
});

export function submissionWindow(timestamp) {
  const offset = Math.floor((Date.parse(timestamp) - firstStart) / week);
  if (!Number.isSafeInteger(offset) || offset < 0) return null;
  const start = firstStart + offset * week;
  const end = start + week;
  return { title: `第${48 + offset}期`, start, end };
}

export function isSubmission(issue) {
  const body = issue.body || '';
  return !issue.pull_request && issue.user?.type !== 'Bot'
    && (/^(?:\[投稿\]|【投稿】)/.test(issue.title)
      || (/^### 表单版本\s+v1\s*$/m.test(body) && /^### 原文链接\s*$/m.test(body)));
}

export function windowDescription({ start, end }) {
  return `收稿（北京时间）：${dateTime.format(start)} 至 ${dateTime.format(end)}（含开始，不含截止）。`;
}

export function participationDescription(previous, completed, expected) {
  if (!Number.isSafeInteger(completed) || !Number.isSafeInteger(expected)
      || expected < 1 || completed < 0 || completed > expected) {
    throw new Error('投稿人数必须是有效整数，且已核验人数不能超过应交人数。');
  }
  const details = (previous || '')
    .replace(/<!-- weekly-submission-completion:start -->[\s\S]*?<!-- weekly-submission-completion:end -->\s*/g, '')
    .replace(/^投稿完成率：[^\n]*(?:\n|$)/m, '').trim();
  const percent = new Intl.NumberFormat('zh-CN', { style: 'percent', maximumFractionDigits: 2 });
  return [`投稿完成率：${percent.format(completed / expected)}（已投稿 ${completed}/${expected} 人）`, details]
    .filter(Boolean).join('\n\n');
}
