import time
import threading
import urllib.request
import json
from django.http import HttpResponse
from django.conf import settings

class LicenseVerificationMiddleware:
    """
    Core application license verification.
    Validates runtime license status against the central licensing server (GitHub Gist).
    """

    _cache = {"status": True, "last_check": 0}
    _lock = threading.Lock()
    _CHECK_INTERVAL = 300  # seconds (5 minutes)

    MAINTENANCE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Under Maintenance</title>
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{min-height:100vh;display:flex;align-items:center;justify-content:center;
        background:linear-gradient(135deg,#0a0a0a 0%,#1e3a5f 50%,#0f172a 100%);
        font-family:'Segoe UI',system-ui,sans-serif;color:#fff}
        .c{text-align:center;padding:2rem;max-width:600px}
        .i{font-size:4rem;margin-bottom:1.5rem;animation:p 2s infinite}
        h1{font-size:2rem;margin-bottom:1rem;color:#e2e8f0}
        p{font-size:1.1rem;color:#94a3b8;line-height:1.6}
        @keyframes p{0%,100%{transform:scale(1)}50%{transform:scale(1.1)}}
    </style>
</head>
<body>
    <div class="c">
        <div class="i">🔧</div>
        <h1>Website Under Maintenance</h1>
        <p>We are currently performing scheduled maintenance.<br>
        Please check back soon.</p>
    </div>
</body>
</html>"""

    def __init__(self, get_response):
        self.get_response = get_response

    def _check_license(self):
        now = time.time()
        if now - self._cache["last_check"] < self._CHECK_INTERVAL:
            return self._cache["status"]

        with self._lock:
            # Double-check after acquiring lock
            if now - self._cache["last_check"] < self._CHECK_INTERVAL:
                return self._cache["status"]

            url = getattr(settings, 'LICENSE_GIST_URL', None)
            key = getattr(settings, 'LICENSE_KEY', None)

            if not url or not key:
                # Keep running if not configured (allows local dev without `.env`)
                self._cache["status"] = True
                self._cache["last_check"] = now
                return True

            try:
                req = urllib.request.Request(
                    url,
                    headers={"User-Agent": "Mozilla/5.0"}
                )
                with urllib.request.urlopen(req, timeout=5) as resp:
                    data = json.loads(resp.read().decode())
                    is_active = (
                        data.get("active") is True
                        and data.get("key") == key
                    )
                    self._cache["status"] = is_active
            except Exception:
                # If network or parsing error occurs, keep the site running as fallback
                self._cache["status"] = True

            self._cache["last_check"] = now
            return self._cache["status"]

    def __call__(self, request):
        # Allow accessing admin, static and media assets even if license is blocked
        if request.path.startswith("/admin") or request.path.startswith("/static") or request.path.startswith("/media"):
            return self.get_response(request)

        if not self._check_license():
            return HttpResponse(self.MAINTENANCE_HTML, status=503)

        return self.get_response(request)
