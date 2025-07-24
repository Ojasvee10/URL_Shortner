# TODO: Implement your data models here
# Consider what data structures you'll need for:
# - Storing URL mappings
# - Tracking click counts
# - Managing URL metadata
# app/models.py
import threading
from datetime import datetime

class URLStorage:
    """Thread-safe in-memory storage for URL mappings."""
    def __init__(self):
        self._store = {}
        self._lock = threading.Lock()

    def add(self, short_code, original_url):
        with self._lock:
            self._store[short_code] = {
                "url": original_url,
                "clicks": 0,
                "created_at": datetime.utcnow().isoformat()
            }

    def get(self, short_code):
        with self._lock:
            return self._store.get(short_code)

    def increment_clicks(self, short_code):
        with self._lock:
            if short_code in self._store:
                self._store[short_code]["clicks"] += 1

    def exists(self, short_code):
        with self._lock:
            return short_code in self._store
