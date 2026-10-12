"""
CineLens AI - One-Click Demo Runner
Launches local web server for Fire TV frontend & FastAPI backend
"""

import sys
import os
import webbrowser
import http.server
import socketserver
import threading
import time

FRONTEND_PORT = 5500
BACKEND_PORT = 8000
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend")
BACKEND_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend")

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FRONTEND_DIR, **kwargs)

def run_frontend():
    with socketserver.TCPServer(("", FRONTEND_PORT), CustomHandler) as httpd:
        print(f"[Frontend Server] Serving Fire TV Web App at http://localhost:{FRONTEND_PORT}")
        httpd.serve_forever()

def run_backend():
    try:
        import uvicorn
        sys.path.insert(0, BACKEND_DIR)
        print(f"[Backend Server] Starting FastAPI on http://localhost:{BACKEND_PORT}")
        uvicorn.run("app:app", host="127.0.0.1", port=BACKEND_PORT, log_level="warning")
    except ImportError:
        print("[Notice] uvicorn not installed; frontend will utilize built-in on-device AI simulation mode.")

if __name__ == "__main__":
    print("=" * 65)
    print("  🚀 CineLens AI - Fire TV & Vega OS Viewing Companion")
    print("  Powered by Amazon Bedrock & AWS Serverless")
    print("=" * 65)

    # Start frontend thread
    t_front = threading.Thread(target=run_frontend, daemon=True)
    t_front.start()

    # Attempt to start backend thread
    t_back = threading.Thread(target=run_backend, daemon=True)
    t_back.start()

    time.sleep(1)
    target_url = f"http://localhost:{FRONTEND_PORT}/index.html"
    print(f"\n✨ Opening demo app: {target_url}")
    print("👉 Use your Keyboard Arrow keys & Enter to test D-pad navigation!")
    print("👉 Or click 'Toggle Virtual Remote' in the lower right.")
    webbrowser.open(target_url)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping CineLens AI servers. Goodbye!")
