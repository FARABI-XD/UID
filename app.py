from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/save_uid", methods=["POST"])
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

if __name__ == "__main__":
    app.run()
