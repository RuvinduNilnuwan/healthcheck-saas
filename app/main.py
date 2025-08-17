from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/healthcheck")
def healthcheck():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return jsonify({"status": "up", "code": response.status_code})
    except Exception as e:
        return jsonify({"status": "down", "error": str(e)}), 500

# This must be outside of any function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


