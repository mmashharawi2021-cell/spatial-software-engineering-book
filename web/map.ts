import { GeoJSONSource, Map } from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';
import './style.css';

const API_BASE = import.meta.env.VITE_API_BASE ?? 'http://localhost:8000';
const statusEl = document.getElementById('status');

function setStatus(message: string, state: 'loading' | 'ready' | 'error' = 'loading') {
  if (!statusEl) return;
  statusEl.textContent = message;
  statusEl.dataset.state = state;
}

const map = new Map({
  container: 'map',
  style: { version: 8, sources: {}, layers: [] },
  center: [35.22, 31.90],
  zoom: 12,
  attributionControl: false,
});

let requestController: AbortController | null = null;

export async function loadVisibleAssets() {
  const b = map.getBounds();
  const bbox = [b.getWest(), b.getSouth(), b.getEast(), b.getNorth()].join(',');

  requestController?.abort();
  const controller = new AbortController();
  requestController = controller;
  setStatus('جاري تحديث البيانات…');

  try {
    const res = await fetch(`${API_BASE}/assets?bbox=${encodeURIComponent(bbox)}&limit=500`, {
      signal: controller.signal,
    });
    if (!res.ok) throw new Error(`API ${res.status}`);

    const fc = await res.json();
    const source = map.getSource('assets') as GeoJSONSource | undefined;
    source?.setData(fc);
    const count = Array.isArray(fc?.features) ? fc.features.length : 0;
    setStatus(`تم تحميل ${count} معلم`, 'ready');
  } catch (error) {
    if (controller.signal.aborted) return;
    setStatus('تعذر تحميل بيانات الخريطة', 'error');
    throw error;
  }
}

map.on('load', () => {
  map.addSource('assets', {
    type: 'geojson',
    data: { type: 'FeatureCollection', features: [] },
  });
  map.addLayer({
    id: 'assets-fill',
    type: 'fill',
    source: 'assets',
    paint: { 'fill-opacity': 0.45, 'fill-outline-color': '#333' },
  });
  void loadVisibleAssets().catch(console.error);
});

map.on('moveend', () => void loadVisibleAssets().catch(console.error));

// Exposed only as a small teaching/test hook; production logic remains encapsulated above.
Object.assign(window, { __geosmartMap: map, __loadVisibleAssets: loadVisibleAssets });
