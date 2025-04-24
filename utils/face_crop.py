import cv2
import numpy as np

def crop_face(input_stream, output_stream):
    input_stream.seek(0)
    file_bytes = np.asarray(bytearray(input_stream.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)

    # 这里写你的人脸裁剪逻辑，下面是示例（直接返回原图）
    # TODO: 替换为真正的人脸检测和裁剪
    result = image

    # 保存结果到 BytesIO
    is_success, buffer = cv2.imencode('.png', result)
    output_stream.write(buffer.tobytes())
    output_stream.seek(0)
