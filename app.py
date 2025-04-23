from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io
import os

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return {"error": "No image provided"}, 400

    file = request.files['image']
    input_image = Image.open(file.stream)

    # 使用 rembg 去除背景
    output_image = remove(input_image)

    # 保存到内存
    output_buffer = io.BytesIO()
    output_image.save(output_buffer, format="PNG")
    output_buffer.seek(0)

    return send_file(output_buffer, mimetype='image/png')

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
