map.on('click', 'buildings-fill', (e) => {
  const f = e.features?.[0];
  if (!f?.id) return;
  map.setFeatureState(
    { source: 'buildings', sourceLayer: 'buildings', id: f.id },
    { selected: true }
  );
});
