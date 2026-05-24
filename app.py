from flask import Flask
import requests
import os
from datetime import datetime

app = Flask(__name__)

ARIA_URL = "https://aria-brain-6b6u.onrender.com"

@app.route("/")
def health():
    try:
        requests.get(ARIA_URL, timeout=10)
        return {"status": "✅ ARIA alive"}
    except:
        return {"status": "⚠️ ARIA sleeping"}

@app.route("/ping")
def ping():
    try:
        r = requests.get(ARIA_URL, timeout=10)
        return {"pinged": True, "time": str(datetime.now())}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
