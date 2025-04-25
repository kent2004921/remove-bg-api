from flask import Flask, request, send_file
from rembg import remove
import io

app = Flask(__name__)

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
    app.run(host='0.0.0.0', port=5000)
