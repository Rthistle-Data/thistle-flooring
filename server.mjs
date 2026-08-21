import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import zlib from "node:zlib";
import { pipeline } from "node:stream";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = __dirname;
const PORT = Number(process.env.PORT) || 3000;
const HOST = "0.0.0.0";

const ROUTES = {
  "/": "index.html",
  "/index": "index.html",
  "/index.html": "index.html",
  "/services": "services.html",
  "/services.html": "services.html",
  "/winter-special": "winter-special.html",
  "/winter-special.html": "winter-special.html",
  "/kitchen-revival": "kitchen-revival.html",
  "/kitchen-revival.html": "kitchen-revival.html",
  "/gallery": "gallery.html",
  "/gallery.html": "gallery.html",
  "/contact": "contact.html",
  "/contact.html": "contact.html",
};

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".mjs": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".gif": "image/gif",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
  ".webp": "image/webp",
  ".txt": "text/plain; charset=utf-8",
  ".xml": "application/xml; charset=utf-8",
  ".woff2": "font/woff2",
  ".map": "application/json",
};

const COMPRESSABLE = new Set([
  "text/html; charset=utf-8",
  "text/css; charset=utf-8",
  "text/javascript; charset=utf-8",
  "application/json; charset=utf-8",
  "image/svg+xml",
  "application/xml; charset=utf-8",
  "text/plain; charset=utf-8",
]);

function send(res, status, headers, body) {
  res.writeHead(status, headers);
  res.end(body);
}

function safePath(urlPath) {
  let decoded;
  try {
    decoded = decodeURIComponent(urlPath);
  } catch {
    return null;
  }
  const resolved = path.resolve(ROOT, "." + decoded);
  if (resolved !== ROOT && !resolved.startsWith(ROOT + path.sep)) return null;
  return resolved;
}

function cacheControl(ext) {
  if (ext === ".html") return "public, max-age=0, must-revalidate";
  if ([".css", ".js", ".mjs"].includes(ext)) return "public, max-age=86400";
  if ([".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".woff2", ".ico"].includes(ext)) {
    return "public, max-age=604800, immutable";
  }
  return "public, max-age=3600";
}

function streamFile(req, res, filePath, status = 200) {
  const ext = path.extname(filePath).toLowerCase();
  const type = MIME[ext] || "application/octet-stream";
  const headers = {
    "Content-Type": type,
    "Cache-Control": cacheControl(ext),
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "X-Frame-Options": "SAMEORIGIN",
  };

  const accept = req.headers["accept-encoding"] || "";
  const canGzip = COMPRESSABLE.has(type) && /\bgzip\b/.test(accept);
  if (canGzip) headers["Content-Encoding"] = "gzip";

  if (req.method === "HEAD") {
    res.writeHead(status, headers);
    res.end();
    return;
  }

  const src = fs.createReadStream(filePath);
  src.on("error", () => {
    if (!res.headersSent) send(res, 500, { "Content-Type": "text/plain" }, "Error");
  });

  res.writeHead(status, headers);
  if (canGzip) {
    pipeline(src, zlib.createGzip(), res, () => {});
  } else {
    pipeline(src, res, () => {});
  }
}

function serve404(req, res) {
  const notFound = path.join(ROOT, "404.html");
  if (fs.existsSync(notFound)) {
    streamFile(req, res, notFound, 404);
    return;
  }
  send(res, 404, { "Content-Type": "text/plain; charset=utf-8" }, "Not found");
}

const server = http.createServer((req, res) => {
  if (!["GET", "HEAD"].includes(req.method || "")) {
    send(res, 405, { Allow: "GET, HEAD" }, "Method not allowed");
    return;
  }

  const url = new URL(req.url || "/", `http://${req.headers.host || "localhost"}`);
  let pathname = url.pathname;
  if (pathname.length > 1 && pathname.endsWith("/")) {
    pathname = pathname.slice(0, -1);
  }

  if (pathname === "/health") {
    send(res, 200, { "Content-Type": "text/plain; charset=utf-8", "Cache-Control": "no-store" }, "ok");
    return;
  }

  const routed = ROUTES[pathname];
  if (routed) {
    streamFile(req, res, path.join(ROOT, routed));
    return;
  }

  const filePath = safePath(pathname);
  if (!filePath) {
    send(res, 403, { "Content-Type": "text/plain" }, "Forbidden");
    return;
  }

  fs.stat(filePath, (err, stat) => {
    if (!err && stat.isFile()) {
      streamFile(req, res, filePath);
      return;
    }
    if (!err && stat.isDirectory()) {
      const index = path.join(filePath, "index.html");
      if (fs.existsSync(index)) {
        streamFile(req, res, index);
        return;
      }
    }
    serve404(req, res);
  });
});

server.listen(PORT, HOST, () => {
  console.log(`Thistle Flooring listening on http://${HOST}:${PORT}`);
});
