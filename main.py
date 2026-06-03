from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/escudo.png")
def logo():
    return send_from_directory(".", "escudo.png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
