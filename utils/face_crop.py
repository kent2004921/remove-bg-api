import cv2
import numpy as np

def remove_background(input_stream, output_stream):
    # 读取 BytesIO 流为 OpenCV 图像
    input_stream.seek(0)
    file_bytes = np.asarray(bytearray(input_stream.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)

    # 模拟背景移除逻辑（这里可以替换为 U^2-Net 模型推理）
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.circle(mask, (image.shape[1]//2, image.shape[0]//2), min(image.shape[:2])//3, 255, -1)
    result = cv2.bitwise_and(image, image, mask=mask)

    # 保存结果到 BytesIO
    is_success, buffer = cv2.imencode('.png', result)
    output_stream.write(buffer.tobytes())
    output_stream.seek(0)
