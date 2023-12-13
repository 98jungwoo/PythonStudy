# Python 코드
def get_data():
    ui_dict = {'x': 275, 'y': 230, 'width': 278, 'height': 278}
    str_dict = str(ui_dict)
    return str_dict


# get_data 함수 호출
result = get_data()

# 딕셔너리를 UIPATH에서 처리할 수 있도록 변환
#ui_dict = {key: str(value) for key, value in result.items()}


# 변환된 딕셔너리 출력
print(result)

