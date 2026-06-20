from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/save_uid", methods=["GET"])
def save_uid():
    uid = request.form.get("uid")

    if not uid:
        return jsonify({"error": "UID required"}), 400

    with open("uids.txt", "a", encoding="utf-8") as f:
        f.write(uid + "\n")

    return jsonify({
        "success": True,
        "uid": uid
    })
import os
@app.route("/")
def home():
    return "Server is running!"
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
