from flask import Flask, request, send_file
from flask_cors import CORS
from PIL import Image
import os
import io

app = Flask(__name__)

# ✅ 开放所有跨域请求，或你可限定指定域名
CORS(app)  # 或用：CORS(app, resources={r"/*": {"origins": "https://sage-flan-6ca7e7.netlify.app"}})

# 创建 static 文件夹用于临时文件
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/')
def home():
    return "✅ Background Removal API Running"

# ✅ 使用 /remove 作为对外提供的 endpoint
@app.route('/remove', methods=['POST'])
def remove_bg():
    if 'file' not in request.files:
        return {"error": "No file provided"}, 400

    file = request.files['file']
    input_path = os.path.join('static', file.filename)

    try:
        # 保存上传的图片
        file.save(input_path)

        # 打开并转换为 RGBA（假设还没真实去背景逻辑）
        img = Image.open(input_path).convert("RGBA")

        # 输出到内存 buffer
        output_buffer = io.BytesIO()
        img.save(output_buffer, format="PNG")
        output_buffer.seek(0)

        return send_file(output_buffer, mimetype='image/png')
    
    except Exception as e:
        return {"error": str(e)}, 500
    
    finally:
        # 清理临时文件
        if os.path.exists(input_path):
            os.remove(input_path)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
