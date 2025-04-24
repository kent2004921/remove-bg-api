from flask import Flask, request, jsonify, send_file
import os
from utils.background_removal import remove_background
from utils.face_crop import crop_face

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'API is working!'})

@app.route('/remove-background', methods=['POST'])
def remove_background_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image = request.files['image']
    input_path = os.path.join(UPLOAD_FOLDER, image.filename)
    output_path = os.path.join(UPLOAD_FOLDER, f"bg_removed_{image.filename}")

    image.save(input_path)
    remove_background(input_path, output_path)

    return send_file(output_path, mimetype='image/png')

@app.route('/crop-face', methods=['POST'])
def crop_face_api():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image = request.files['image']
    input_path = os.path.join(UPLOAD_FOLDER, image.filename)
    output_path = os.path.join(UPLOAD_FOLDER, f"face_cropped_{image.filename}")

    image.save(input_path)
    crop_face(input_path, output_path)

    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
