# app/main.py
from flask import Flask, request, jsonify, redirect
from app.models import URLStorage
from app.utils import generate_code, is_valid_url

app = Flask(__name__)
storage = URLStorage()

@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' field"}), 400

    original_url = data["url"]
    if not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    # Generate a unique code
    code = generate_code()
    while storage.exists(code):
        code = generate_code()

    storage.add(code, original_url)
    short_url = f"http://localhost:5000/{code}"
    return jsonify({"short_code": code, "short_url": short_url}), 201

@app.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):
    record = storage.get(short_code)
    if not record:
        return jsonify({"error": "Short code not found"}), 404
    storage.increment_clicks(short_code)
    return redirect(record["url"], code=302)

@app.route("/api/stats/<short_code>", methods=["GET"])
def stats(short_code):
    record = storage.get(short_code)
    if not record:
        return jsonify({"error": "Short code not found"}), 404
    return jsonify({
        "url": record["url"],
        "clicks": record["clicks"],
        "created_at": record["created_at"]
    }), 200
