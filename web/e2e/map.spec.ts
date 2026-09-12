import { expect, test } from '@playwright/test';

const oneFeature = {
  type: 'FeatureCollection',
  features: [
    {
      type: 'Feature',
      id: 'A-001',
      geometry: {
        type: 'Polygon',
        coordinates: [[[35.2055,31.893],[35.2067,31.893],[35.2067,31.8942],[35.2055,31.8942],[35.2055,31.893]]],
      },
      properties: { name: 'Training Asset', review_status: 'pending' },
    },
  ],
  links: [],
};

test('loads the map and visible features', async ({ page }) => {
  await page.route('http://localhost:8000/assets**', async route => {
    await route.fulfill({ status: 200, contentType: 'application/geo+json', body: JSON.stringify(oneFeature) });
  });

  await page.goto('/');
  await expect(page.locator('.maplibregl-canvas')).toBeVisible();
  await expect(page.locator('#status')).toHaveAttribute('data-state', 'ready');
  await expect(page.locator('#status')).toContainText('1');
});

test('surfaces API errors to the reader', async ({ page }) => {
  await page.route('http://localhost:8000/assets**', async route => {
    await route.fulfill({ status: 503, contentType: 'application/json', body: JSON.stringify({ detail: { code: 'unavailable' } }) });
  });

  await page.goto('/');
  await expect(page.locator('#status')).toHaveAttribute('data-state', 'error');
  await expect(page.locator('#status')).toContainText('تعذر');
});

test('cancels the previous request when a new refresh starts', async ({ page }) => {
  let requestCount = 0;
  await page.route('http://localhost:8000/assets**', async route => {
    requestCount += 1;
    if (requestCount === 1) {
      await new Promise(resolve => setTimeout(resolve, 500));
    }
    await route.fulfill({ status: 200, contentType: 'application/geo+json', body: JSON.stringify(oneFeature) }).catch(() => undefined);
  });

  await page.goto('/');
  await page.waitForFunction(() => typeof (window as any).__loadVisibleAssets === 'function');
  await page.evaluate(() => {
    void (window as any).__loadVisibleAssets();
    void (window as any).__loadVisibleAssets();
  });
  await expect.poll(() => requestCount).toBeGreaterThanOrEqual(2);
  await expect(page.locator('#status')).toHaveAttribute('data-state', 'ready');
});
