import json
from flask import Flask, jsonify, request
import pyotp

app = Flask(__name__)
SECRETS_FILE = "secrets.json"


def load_secrets():
    try:
        with open(SECRETS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_secret(username, secret):
    secrets = load_secrets()
    secrets[username] = secret
    with open(SECRETS_FILE, "w") as file:
        json.dump(secrets, file)


@app.route("/setup", methods=["POST"])
def setup_account():
    data = request.get_json()
    username = data.get("username")
    secret = data.get("secret")
    save_secret(username, secret)
    return jsonify({"username": username, "secret": secret})


@app.route("/get-totp/<username>", methods=["GET"])
def get_totp(username):
    secrets = load_secrets()
    user_secret = secrets.get(username)
    if not user_secret:
        return jsonify({"error": "User not found"}), 404

    totp = pyotp.TOTP(user_secret)
    return jsonify({"username": username, "totp": totp.now()})


if __name__ == "__main__":
    app.run(debug=True)
