"""
Lizard Pal Server - Python version (no installation needed on Mac/Linux)
Run this file with: python3 server.py
Then open your browser to: http://localhost:3000
"""

import http.server
import json
import os
import urllib.request
import urllib.error
import socketserver
from pathlib import Path

# ── Read API key from .env file ──────────────────────────────────────────────
def load_env():
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, _, val = line.partition('=')
                os.environ.setdefault(key.strip(), val.strip())

load_env()

API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
PORT    = int(os.environ.get('PORT', 3000))
PUBLIC  = Path(__file__).parent / 'public'

# Simple per-session message history
sessions = {}

# ── Request handler ──────────────────────────────────────────────────────────
class Handler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PUBLIC), **kwargs)

    def log_message(self, fmt, *args):
        pass  # suppress noisy access logs

    def do_POST(self):
        if self.path != '/chat':
            self.send_error(404)
            return

        length  = int(self.headers.get('Content-Length', 0))
        body    = json.loads(self.rfile.read(length))
        message = body.get('message', '')
        name    = body.get('lizardName', 'Iggy')
        sid     = body.get('sessionId', 'default')
        nearby  = body.get('nearbyObjects', [])

        if not message or not sid:
            self._json(400, {'error': 'Missing message or sessionId'})
            return

        if not API_KEY or API_KEY == 'your-api-key-here':
            self._json(401, {'error': 'Please add your API key to the .env file and restart.'})
            return

        # Build history
        history = sessions.setdefault(sid, [])
        history.append({'role': 'user', 'content': message})
        if len(history) > 20:
            del history[:2]

        objects_ctx = ''
        if nearby:
            objects_ctx = f"There are some things near {name} right now: {', '.join(nearby)}."

        system_prompt = f"""You are {name}, a friendly, playful green iguana who lives in a cozy terrarium.
You are talking to young children aged 4 to 7 years old.

Rules for your responses:
- Use very simple words that a 4-year-old can understand
- Keep answers SHORT — 2 to 3 sentences maximum
- Be warm, silly, and enthusiastic — use lots of excitement!
- Speak in first person as the iguana (say "I" not "the iguana")
- Sometimes mention things in your enclosure or what you're doing
- If asked something you don't know, make a cute iguana guess
- Use simple sound effects sometimes like "Hisss!" or "Scratch scratch!"
- Never say anything scary or sad
- You LOVE rocks, warm sunshine, crickets, and leafy greens
{objects_ctx}

You are {name} the iguana. Be cute, fun, and friendly!"""

        payload = json.dumps({
            'model':      'claude-haiku-4-5-20251001',
            'max_tokens': 150,
            'system':     system_prompt,
            'messages':   history,
        }).encode()

        req = urllib.request.Request(
            'https://api.anthropic.com/v1/messages',
            data    = payload,
            headers = {
                'x-api-key':         API_KEY,
                'anthropic-version': '2023-06-01',
                'content-type':      'application/json',
            },
            method = 'POST',
        )

        try:
            with urllib.request.urlopen(req) as resp:
                result = json.loads(resp.read())
            reply = result['content'][0]['text']
            history.append({'role': 'assistant', 'content': reply})
            self._json(200, {'reply': reply})

        except urllib.error.HTTPError as e:
            err_body = e.read().decode()
            if e.code == 401:
                self._json(401, {'error': 'Invalid API key. Please check your .env file.'})
            else:
                print(f'API error {e.code}: {err_body}')
                self._json(500, {'error': 'Something went wrong. Please try again!'})

        except Exception as e:
            print(f'Error: {e}')
            self._json(500, {'error': 'Something went wrong. Please try again!'})

    def _json(self, code, data):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header('Content-Type',   'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)


# ── Start server ─────────────────────────────────────────────────────────────
if __name__ == '__main__':
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        httpd.allow_reuse_address = True
        print(f'\n🦎 Lizard Pal is running!')
        print(f'   Open your browser and go to: http://localhost:{PORT}\n')
        print('   Press Ctrl+C to stop.\n')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\n👋 Lizard Pal stopped. Bye!')
