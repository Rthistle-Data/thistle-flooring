import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { once } from 'node:events';
import net from 'node:net';
let child, base;
before(async () => {
  const reservation = net.createServer();
  reservation.listen(0, '127.0.0.1');
  await once(reservation, 'listening');
  const port = reservation.address().port;
  await new Promise(resolve => reservation.close(resolve));
  base = `http://127.0.0.1:${port}`;
  child = spawn(process.execPath, ['server.mjs'], { env: { ...process.env, PORT: String(port), GMAIL_APP_PASSWORD: '' }, stdio: ['ignore', 'pipe', 'pipe'] });
  await Promise.race([once(child.stdout, 'data'), once(child, 'exit').then(() => { throw new Error('Server exited before startup'); })]);
});
after(() => child?.kill());
test('public pages and assets remain available', async () => {
  for (const path of ['/', '/contact', '/services', '/gallery', '/winter-special', '/kitchen-revival', '/css/styles.css', '/js/main.js', '/assets/gallery/vinyl-rec-room-walnut.jpg', '/robots.txt', '/sitemap.xml']) {
    assert.equal((await fetch(base + path)).status, 200, path);
  }
});
test('internal files and encoded paths are not public', async () => {
  for (const path of ['/server.mjs', '/mail.mjs', '/package.json', '/README.md', '/_build_pages.py', '/.git/config', '/.env', '/%73erver.mjs', '/assets/images/../../server.mjs', '/node_modules/nodemailer/package.json', '/tests/server.test.mjs']) {
    for (const method of ['GET', 'HEAD']) assert.equal((await fetch(base + path, { method })).status, 404, `${method} ${path}`);
  }
});
test('invalid quote requests are rejected without sending mail', async () => {
  const response = await fetch(base + '/api/quote', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ name: 'Test', email: 'invalid' }) });
  assert.equal(response.status, 400);
  assert.equal((await response.json()).ok, false);
});
