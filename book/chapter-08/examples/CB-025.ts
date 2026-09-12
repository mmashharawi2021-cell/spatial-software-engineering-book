import { Map } from 'maplibre-gl';

const map = new Map({
  container: 'map',
  style: '/styles/base.json',
  center: [35.22, 31.90],
  zoom: 12
});
map.on('moveend', () => loadVisibleAssets(map.getBounds()));
