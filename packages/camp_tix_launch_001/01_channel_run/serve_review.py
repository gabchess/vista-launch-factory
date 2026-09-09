"""Serve this campaign review locally. Only explicit media paths are exposed."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit
import re
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent


class ReviewHandler(SimpleHTTPRequestHandler):
    media = {}

    def do_GET(self):
        path = urlsplit(self.path).path
        if path not in self.media:
            return super().do_GET()
        file = self.media[path]
        if not file.is_file():
            return self.send_error(404, 'Approved media was not attached to this local preview.')
        size = file.stat().st_size
        start, end = 0, size - 1
        request_range = self.headers.get('Range')
        if request_range:
            match = re.fullmatch(r'bytes=(\d*)-(\d*)', request_range)
            if not match or not any(match.groups()):
                return self.send_error(416, 'Unsupported media range')
            if not match[1]:
                start = max(0, size - int(match[2]))
            else:
                start = int(match[1])
                end = min(int(match[2]) if match[2] else end, end)
            if start > end or start >= size:
                return self.send_error(416, 'Media range is outside file')
        self.send_response(206 if request_range else 200)
        self.send_header('Content-Type', 'video/mp4')
        self.send_header('Content-Length', str(end-start+1))
        self.send_header('Accept-Ranges', 'bytes')
        if request_range:
            self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        self.end_headers()
        try:
            with file.open('rb') as f:
                f.seek(start)
                remaining = end-start+1
                while remaining:
                    chunk = f.read(min(256*1024, remaining))
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    remaining -= len(chunk)
        except (BrokenPipeError, ConnectionResetError):
            pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8770)
    parser.add_argument('--film', type=Path)
    parser.add_argument('--animation', type=Path)
    args = parser.parse_args()
    data_path = ROOT/'01_channel_run/review-data.json'
    if not data_path.is_file():
        parser.error('Build review-data.json before starting this review server.')
    data = json.loads(data_path.read_text())
    expected = {a['id']: a['sha256'] for a in data['assets'] if a.get('approved')}
    for name, file in [('film', args.film), ('animation', args.animation)]:
        if file:
            asset_id = 'social-video' if name == 'film' else 'animation'
            if not file.is_file():
                parser.error(f'{name} does not exist: {file}')
            digest = hashlib.sha256()
            with file.open('rb') as stream:
                for chunk in iter(lambda: stream.read(1024*1024), b''):
                    digest.update(chunk)
            actual = digest.hexdigest()
            if actual != expected.get(asset_id):
                parser.error(f'{name} does not match the approved artifact SHA-256.')
            ReviewHandler.media[f'/media/{name}.mp4'] = file.resolve()
    handler = partial(ReviewHandler, directory=str(ROOT))
    print(f'Review: http://127.0.0.1:{args.port}/01_channel_run/review.html', flush=True)
    ThreadingHTTPServer(('127.0.0.1', args.port), handler).serve_forever()
