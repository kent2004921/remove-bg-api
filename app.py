from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import io
from PIL import Image
from utils.background_removal import remove_background
from utils.face_crop import crop_face

app = Flask(__name__)
CORS(app)  # 允许所有跨域

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'API is working!'})

@app.route('/remove-background', methods=['POST'])
def remove_background_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image = request.files['image']
    try:
        input_image = Image.open(image)
        input_path = io.BytesIO()
        input_image.save(input_path, format=input_image.format)
        input_path.seek(0)

        output_path = io.BytesIO()
        remove_background(input_path, output_path)
        output_path.seek(0)

        return send_file(output_path, mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/crop-face', methods=['POST'])
def crop_face_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image = request.files['image']
    try:
        input_image = Image.open(image)
        input_path = io.BytesIO()
        input_image.save(input_path, format=input_image.format)
        input_path.seek(0)

        output_path = io.BytesIO()
        crop_face(input_path, output_path)
        output_path.seek(0)

        return send_file(output_path, mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
