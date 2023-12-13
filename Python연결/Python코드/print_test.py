import cv2

def detect_faces():
    # 이미지 불러오기
    image_path = "C:/workspace/1_요청/sample.jpeg"  # 이미지 파일의 경로를 직접 지정
    # 이미지 파일의 경로를 직접 지정
    image = cv2.imread(image_path)

    # 얼굴 감지
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

    # 감지된 얼굴의 좌표 반환
    face_coordinates = []
    for (x, y, w, h) in faces:
        face_coordinates.append({"x": x, "y": y, "width": w, "height": h})
    
    print("Type of face_coordinates:", face_coordinates.__class__)

    return str(({"x": 270, "y": 50, "width": 300, "height": 300}))


result = detect_faces()
print(result)
print(type(result))