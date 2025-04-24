import cv2
import mediapipe as mp

def crop_face(input_path, output_path):
    image = cv2.imread(input_path)
    mp_face_detection = mp.solutions.face_detection
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if not results.detections:
            raise ValueError("No face detected")
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape
            x = int(bboxC.xmin * iw)
            y = int(bboxC.ymin * ih)
            w = int(bboxC.width * iw)
            h = int(bboxC.height * ih)
            cropped_face = image[y:y+h, x:x+w]
            cv2.imwrite(output_path, cropped_face)
            break
