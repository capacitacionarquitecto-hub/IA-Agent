import json
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent
OPENAI_API_BASE = os.environ.get("OPENAI_API_BASE", "http://localhost:11434/v1")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "ollama")
CHAT_MODEL = os.environ.get("CHAT_MODEL", "qwen3.5:397b-cloud")

client = OpenAI(base_url=OPENAI_API_BASE, api_key=OPENAI_API_KEY)


class ChatRequestHandler(SimpleHTTPRequestHandler):
    server_version = "LocalChat/0.1"

    def do_POST(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path != "/api/chat":
            return self.send_error(404, "Not Found")

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")

        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            return self.send_error(400, "Invalid JSON")

        messages = payload.get("messages")
        model = payload.get("model", CHAT_MODEL)

        if not isinstance(messages, list):
            return self.send_error(400, "`messages` must be a JSON array")

        try:
            response = client.chat.completions.create(model=model, messages=messages)
            assistant_text = response.choices[0].message.content
        except Exception as exc:
            self.send_response(500)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            error_body = {"error": str(exc)}
            self.wfile.write(json.dumps(error_body, ensure_ascii=False).encode("utf-8"))
            return

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        response_body = {"reply": assistant_text}
        self.wfile.write(json.dumps(response_body, ensure_ascii=False).encode("utf-8"))

    def translate_path(self, path):
        # Serve files from the repository root only
        path = super().translate_path(path)
        return path


def run(server_class=ThreadingHTTPServer, handler_class=ChatRequestHandler, port=8000):
    os.chdir(BASE_DIR)
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving chat UI at http://localhost:{port}/chat.html")
    print(f"Using OpenAI base URL: {OPENAI_API_BASE}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()


if __name__ == "__main__":
    run()
