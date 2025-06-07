import os
from flask import Flask, Response, render_template, request
import requests
from waitress import serve
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

# Get config from environment
EXPORTER_URL = os.environ.get("EXPORTER_URL", "http://localhost/containers/metrics")
USERNAME = os.environ.get("EXPORTER_USERNAME", "")
PASSWORD = os.environ.get("EXPORTER_PASSWORD", "")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/containers/metrics")
def proxy_metrics():
    try:
        resp = requests.get(
            EXPORTER_URL,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            headers={"Accept": "text/plain"},
            verify=False,
	    timeout=30
        )
        return Response(resp.content, status=resp.status_code, content_type=resp.headers.get("Content-Type", "text/plain"))
    except Exception as e:
        return f"Proxy error: {e}", 500

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=80)
