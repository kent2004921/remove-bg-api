import os
from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
import io

# 指定 rembg 使用本地模型目录
os.environ["U2NET_HOME"] = os.path.join(os.path.dirname(__file__), "models")

app = Flask(__name__)
CORS(app)  # 允许所有跨域请求

@app.route('/api/remove', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return {'error': 'No image file provided'}, 400
    file = request.files['image']
    input_bytes = file.read()
    output_bytes = remove(input_bytes)
    return send_file(
        io.BytesIO(output_bytes),
        mimetype='image/png'
    )

@app.route('/')
def index():
    return 'rembg API is running.'

if __name__ == '__main__':
    # 打印 models 目录内容，方便 Render 日志排查
    print("models 目录内容：", os.listdir(os.path.join(os.path.dirname(__file__), "models")))
    app.run(host='0.0.0.0', port=5000)
