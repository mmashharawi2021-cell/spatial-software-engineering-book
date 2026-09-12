let controller: AbortController | undefined;
async function refresh(url: string) {
  controller?.abort();
  controller = new AbortController();
  const r = await fetch(url, {signal: controller.signal});
  return r.json();
}
