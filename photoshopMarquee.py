# 올가미도구 사용 코드
# 이거 동작 안됨 (ps.DialogModes이 속성이 없다함)
from photoshop import Session

def create_marquee_selection(top_left, bottom_right):
    with Session() as ps:
        app = ps.app

        # Marquee 도구를 활성화합니다.
        marquee_tool = app.charIDToTypeID("MqT ")  # Marquee Tool의 ID
        desc = ps.ActionDescriptor()
        desc.putClass(app.charIDToTypeID("null"), marquee_tool)
        app.executeAction(app.charIDToTypeID("slct"), desc, ps.DialogModes.NO)

        # Marquee 선택 영역의 좌표를 설정합니다.
        marquee_descriptor = ps.ActionDescriptor()
        marquee_descriptor.putUnitDouble(app.charIDToTypeID("Top "), app.charIDToTypeID("#Pxl"), top_left[1])
        marquee_descriptor.putUnitDouble(app.charIDToTypeID("Left"), app.charIDToTypeID("#Pxl"), top_left[0])
        marquee_descriptor.putUnitDouble(app.charIDToTypeID("Btom"), app.charIDToTypeID("#Pxl"), bottom_right[1])
        marquee_descriptor.putUnitDouble(app.charIDToTypeID("Rght"), app.charIDToTypeID("#Pxl"), bottom_right[0])

        # Marquee 선택 영역을 만듭니다.
        app.executeAction(app.charIDToTypeID("setd"), marquee_descriptor, ps.DialogModes.NO)

# 예제: (100, 100)에서 (300, 300)까지의 Marquee 선택 영역을 만듭니다.
create_marquee_selection((100, 100), (300, 300))