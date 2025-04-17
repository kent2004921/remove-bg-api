from flask import Flask, request, jsonify
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Background Removal API Running"

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    input_path = f'static/{file.filename}'
    output_path = f'static/processed_{file.filename}'

    file.save(input_path)

    # 模拟去背景处理（此处应接 PyMatting 等）
    img = Image.open(input_path).convert("RGBA")
    img.save(output_path)

    return jsonify({'success': True, 'url': output_path})

if __name__ == '__main__':
    app.run()
