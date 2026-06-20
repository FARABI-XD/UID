from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "uids.txt")


@app.route("/")
def home():
    return "Server is running!"


@app.route("/save_uid", methods=["GET"])
def save_uid():
    uid = request.args.get("uid")

    if not uid:
        return jsonify({"error": "UID required"}), 400

    # Save UID
    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(uid + "\n")
        f.flush()
        os.fsync(f.fileno())

    return jsonify({
        "success": True,
        "uid": uid,
        "saved_to": FILE_PATH
    })


@app.route("/uids")
def show_uids():
    if not os.path.exists(FILE_PATH):
        return "No UID saved yet."

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return f.read(), 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
