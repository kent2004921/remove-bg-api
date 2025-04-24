import cv2
import numpy as np

def remove_background(input_path, output_path):
    # 加载图片
    image = cv2.imread(input_path)
    # 模拟背景移除逻辑（这里可以替换为 U^2-Net 模型推理）
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    cv2.circle(mask, (image.shape[1]//2, image.shape[0]//2), min(image.shape[:2])//3, 255, -1)
    result = cv2.bitwise_and(image, image, mask=mask)

    # 保存结果
    cv2.imwrite(output_path, result)