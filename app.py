
# AudioPro v1.0 - By D3F4ULT
from flask import Flask, request, send_file
from gtts import gTTS
import io

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>AudioPro</title>
    <style>
        body { font-family: sans-serif; background: #E0F2FE; text-align: center; padding: 20px; margin: 0; }
        .box { background: white; border-radius: 30px; padding: 30px; max-width: 400px; margin: auto; box-shadow: 0 8px 20px rgba(0,0,0,0.2); }
        h2 { color: #1a1a2e; }
        textarea { width: 100%; padding: 14px; margin: 15px 0; border-radius: 20px; border: 2px solid #ddd; font-size: 18px; box-sizing: border-box; height: 120px; }
        button { width: 100%; padding: 14px; margin: 10px 0; border-radius: 50px; border: none; font-size: 18px; font-weight: bold; cursor: pointer; background: #3B82F6; color: white; }
        button:hover { background: #2563EB; }
        audio { width: 100%; margin-top: 20px; }
        .speed { display: flex; align-items: center; justify-content: center; gap: 10px; margin: 10px 0; color: #1a1a2e; font-size: 14px; }
        input[type=range] { width: 60%; accent-color: #3B82F6; }
    </style>
</head>
<body>
    <div class="box">
        <h2>🎙️ AudioPro</h2>
        <textarea id="text" placeholder="أكتب أي نص..."></textarea>
        <button onclick="speak()">🔊 استمع للصوت</button>
        <div class="speed">
            <span>🐢 عادي</span>
            <input type="range" id="speed" min="0.5" max="2.0" value="1.0" step="0.1" oninput="changeSpeed()">
            <span>🐿️ كرتوني</span>
        </div>
        <audio id="audio" controls style="display:none;"></audio>
    </div>

    <script>
        function speak() {
            const text = document.getElementById('text').value;
            if (!text) return alert('أكتب نصاً أولاً');
            const audio = document.getElementById('audio');
            audio.src = '/speak?text=' + encodeURIComponent(text);
            audio.style.display = 'block';
            audio.play();
            changeSpeed();
        }
        function changeSpeed() {
            const speed = document.getElementById('speed').value;
            const audio = document.getElementById('audio');
            audio.playbackRate = parseFloat(speed);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return HTML_PAGE

@app.route('/speak')
def speak():
    text = request.args.get('text', '')
    tts = gTTS(text=text, lang='ar')
    mp3 = io.BytesIO()
    tts.write_to_fp(mp3)
    mp3.seek(0)
    return send_file(mp3, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
