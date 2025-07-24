# TODO: Implement utility functions here
# Consider functions for:
# - Generating short codes
# - Validating URLs
# - Any other helper functions you need
# app/utils.py
import re, string, random
from urllib.parse import urlparse

ALPHANUM = string.ascii_letters + string.digits

def generate_code(length=6):
    """Generate a random alphanumeric code."""
    return ''.join(random.choices(ALPHANUM, k=length))

def is_valid_url(url):
    """Basic validation to ensure scheme and netloc exist."""
    try:
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except Exception:
        return False
