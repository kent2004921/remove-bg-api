from flask import Flask, request, jsonify
from flask_cors import CORS  # 导入 flask-cors
from PIL import Image
import os

app = Flask(__name__)
# 启用 CORS，允许特定来源
CORS(app, resources={r"/*": {"origins": "https://sage-flan-6ca7e7.netlify.app"}})

# 确保 static 目录存在
if not os.path.exists('static'):
    os.makedirs('static')

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

    # 保存上传的文件
    file.save(input_path)

    try:
        # 模拟去背景处理（此处应接 PyMatting 等）
        img = Image.open(input_path).convert("RGBA")
        img.save(output_path)

        # 返回相对路径供前端访问
        return jsonify({'success': True, 'url': output_path})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # 清理临时文件
        if os.path.exists(input_path):
            os.remove(input_path)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # 使用 Render 提供的 PORT 环境变量
    app.run(host="0.0.0.0", port=port)
