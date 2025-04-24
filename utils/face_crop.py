import cv2
import dlib

def crop_face(input_path, output_path):
    # 加载图片
    image = cv2.imread(input_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 加载 dlib 的人脸检测器
    detector = dlib.get_frontal_face_detector()
    faces = detector(gray)

    if len(faces) == 0:
        raise ValueError("No face detected")

    # 裁切第一个检测到的人脸
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cropped_face = image[y:y+h, x:x+w]
        cv2.imwrite(output_path, cropped_face)
        break