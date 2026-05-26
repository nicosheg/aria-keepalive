import requests, os, time
url = os.environ.get("ARIA_URL", "https://aria-brain-6b6u.onrender.com/health")
while True:
    try:
        r = requests.get(url, timeout=10)
        print(f"✅ [{time.strftime('%H:%M:%S')}] Pinged ARIA")
    except Exception as e:
        print(f"❌ [{time.strftime('%H:%M:%S')}] Ping failed: {e}")
    time.sleep(600)
