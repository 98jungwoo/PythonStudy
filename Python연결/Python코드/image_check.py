import cv2
from matplotlib import pyplot as plt

def detect_and_draw_faces(image_path):
    # 이미지 불러오기
    image = cv2.imread(image_path)

    # 얼굴 감지
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

    # 감지된 얼굴에 사각형 그리기
    face_coordinates = []
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face_coordinates.append({"x": x, "y": y, "width": w, "height": h})

    #딕셔너리를 통으로 문자열로 변경
    str_dict = str(face_coordinates) 


    # 결과 이미지 출력
    #plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    #plt.axis('off')
    #plt.show()

    return str_dict

# 이미지 경로
image_path = 'C:/workspace/sample.jpeg'

# 얼굴 감지 및 그리기
detect_and_draw_faces(image_path)