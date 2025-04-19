from flask import Flask, request, send_file
from flask_cors import CORS
from PIL import Image
import os
import io

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://sage-flan-6ca7e7.netlify.app"}})

if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/')
def home():
    return "Background Removal API Running"

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'file' not in request.files:
        return {"error": "No file provided"}, 400

    file = request.files['file']
    input_path = f'static/{file.filename}'

    # 保存上传的文件
    file.save(input_path)

    try:
        # 模拟去背景处理（此处应接 PyMatting 等）
        img = Image.open(input_path).convert("RGBA")

        # 将图像保存到内存
        output_buffer = io.BytesIO()
        img.save(output_buffer, format="PNG")
        output_buffer.seek(0)

        # 返回图像数据
        return send_file(
            output_buffer,
            mimetype='image/png',
            as_attachment=False
        )
    except Exception as e:
        return {"error": str(e)}, 500
    finally:
        # 清理临时文件
        if os.path.exists(input_path):
            os.remove(input_path)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
