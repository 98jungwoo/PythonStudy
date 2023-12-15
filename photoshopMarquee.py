# 올가미도구 사용 코드
# 이거 동작 안됨 (ps.DialogModes이 속성이 없다함)
from photoshop import Session

def create_marquee_selection(top_left, bottom_right, file_path):
    with Session() as ps:
        app = ps.app
        doc = app.documents.add()

        # 이미지를 불러옵니다.
        app.load(file_path)
        new_doc = doc.artLayers.add()

        # Marquee 도구를 활성화합니다.
        marquee_tool = app.charIDToTypeID("MqT ") #  "MqT "라는 문자열을 특정 ID로 변환합니다. 이 ID는 Photoshop 내에서 Marquee 도구를 나타냅니다.

        desc = ps.ActionDescriptor()  # Photoshop 액션 디스크립터를 생성합니다. 이는 Photoshop에게 수행할 작업에 대한 명령을 나타냅니다.

        desc.putClass(app.charIDToTypeID("null"), marquee_tool) # "null" 클래스와 Marquee 도구 ID를 설정합니다. 이것은 선택 도구를 설정하는 부분입니다.

        app.executeAction(app.charIDToTypeID("slct"), desc, ps.DialogModes.NO)   # 'slct'는 선택 동작을 나타냅니다. # DialogModes.NO대화 상자 모드 없이 실행합니다.


        # Marquee 선택 영역의 좌표를 설정합니다.
        marquee_descriptor = ps.ActionDescriptor()
        marquee_descriptor.putUnitDouble(app.charIDToTypeID("Top "), app.charIDToTypeID("#Pxl"), top_left[1])
        marquee_descriptor.putUnitDouble(app.charIDToTypeID("Left"), app.charIDToTypeID("#Pxl"), top_left[0])
        marquee_descriptor.putUnitDouble(app.charIDToTypeID("Btom"), app.charIDToTypeID("#Pxl"), bottom_right[1])
        marquee_descriptor.putUnitDouble(app.charIDToTypeID("Rght"), app.charIDToTypeID("#Pxl"), bottom_right[0])

        # Marquee 선택 영역을 만듭니다.
        app.executeAction(app.charIDToTypeID("setd"), marquee_descriptor, ps.DialogModes.NO)


# 예제: (100, 100)에서 (300, 300)까지의 Marquee 선택 영역을 만듭니다.
create_marquee_selection((100, 100), (300, 300), 'C:/workspace/1_요청/sample.jpeg')
