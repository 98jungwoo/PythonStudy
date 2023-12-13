import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
import urllib.request

# Caffe 모델 파일 다운로드
caffe_prototxt_url = "https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/opencv_face_detector.prototxt"
caffe_model_url = "https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel"

urllib.request.urlretrieve(caffe_prototxt_url, "deploy.prototxt")
urllib.request.urlretrieve(caffe_model_url, "res10_300x300_ssd_iter_140000.caffemodel")

# 다운로드한 파일의 경로를 변수에 할당
caffe_prototxt = "deploy.prototxt"
caffe_model = "res10_300x300_ssd_iter_140000.caffemodel"


def detect_faces_in_folder(folder_path):
    # 얼굴 감지 모델 로딩 (예: Caffe 모델)
    net = cv2.dnn.readNetFromCaffe(caffe_prototxt, caffe_model)

    # 폴더 내 모든 파일에 대해 반복
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.webp')):
            # 이미지 파일 경로
            image_path = os.path.join(folder_path, filename)

            # 이미지 불러오기
            image = cv2.imread(image_path)

            # 이미지의 높이와 너비 얻기
            (h, w) = image.shape[:2]

            # 이미지 전처리 및 얼굴 감지
            blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
            net.setInput(blob)
            detections = net.forward()

            # 얼굴에 대한 bounding box 그리기
            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]

                if confidence > 0.5:  # confidence 조절 가능
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

            # 결과 이미지 출력
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.title(f"Detected Faces in {filename}")
            plt.show()

            str_dict = str({'x': startX, 'y': startY, 'width': endX, 'height': endY}) 
    return str_dict

# 이미지 폴더 경로
#folder_path = r'C:\workspace\boy2'  # r 접두어로 원시 문자열로 지정
folder_path = r"C:/workspace/Character_Image/boy/"

# 얼굴 감지 및 그리기
detect_faces_in_folder(folder_path)
