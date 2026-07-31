from flask import Flask, send_from_directory, request, jsonify
import os, json

app = Flask(__name__)

DATA_DIR  = os.environ.get('DATA_DIR', os.path.join(os.path.dirname(__file__), 'data'))
DATA_FILE = os.path.join(DATA_DIR, 'candidatos.json')

os.makedirs(DATA_DIR, exist_ok=True)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/escudo.png")
def logo():
    return send_from_directory(".", "escudo.png")

@app.route("/apple-touch-icon.png")
def touch_icon():
    return send_from_directory(".", "apple-touch-icon.png")

@app.route("/candidatos")
def candidatos():
    return send_from_directory(".", "candidatos.html")

@app.route("/api/candidatos", methods=["GET"])
def get_candidatos():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return jsonify(json.load(f))
        return jsonify(None)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/candidatos", methods=["POST"])
def post_candidatos():
    try:
        data = request.get_json()
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        return jsonify({"ok": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
