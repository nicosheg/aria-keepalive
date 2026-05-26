import requests, os, time, threading
from http.server import HTTPServer, BaseHTTPRequestHandler

url = os.environ.get("ARIA_URL", "https://aria-brain-6b6u.onrender.com/health")

def ping_aria():
    while True:
        try:
            requests.get(url, timeout=10)
            print(f"✅ Pinged ARIA")
        except:
            print(f"❌ Ping failed")
        time.sleep(300)

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status":"Keep-alive running"}')
        else:
            self.send_response(404)
            self.end_headers()

threading.Thread(target=ping_aria, daemon=True).start()
port = int(os.environ.get("PORT", 8080))
print(f"✅ Keep-alive listening on port {port}...")
HTTPServer(("0.0.0.0", port), Handler).serve_forever()
