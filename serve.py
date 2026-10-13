# Servidor local: serve a pasta e salva PNGs enviados por POST /save?name=arquivo.png
import http.server, pathlib, urllib.parse
d = pathlib.Path(__file__).parent
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s, *a, **k): super().__init__(*a, directory=str(d), **k)
    def do_POST(s):
        name = urllib.parse.parse_qs(urllib.parse.urlparse(s.path).query)['name'][0]
        data = s.rfile.read(int(s.headers['Content-Length']))
        (d / 'saidas').mkdir(exist_ok=True)
        (d / 'saidas' / pathlib.Path(name).name).write_bytes(data)
        s.send_response(200); s.end_headers(); s.wfile.write(b'ok')
http.server.ThreadingHTTPServer(('127.0.0.1', 8765), H).serve_forever()
