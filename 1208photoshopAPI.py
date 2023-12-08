import photoshop.api as ps


app = ps.Application() # 포토샵 응용프로그램에 대한 인스턴스를 생성
doc = app.documents.add() # 새 문서 추가
new_doc = doc.artLayers.add() # 새로운 아트 레이어를 추가

# text 색상 설정 (0, 255, 0)
text_color = ps.SolidColor() 
text_color.rgb.red = 0 
text_color.rgb.green = 255 
text_color.rgb.blue = 0 

# 
new_text_layer = new_doc # 새로운 아트 레이어를 추가
new_text_layer.kind = ps.LayerKind.TextLayer # 텍스트 레이어로 설정 
# new_text_layer.kind = 2 # 텍스트 레이어로 설정하는게 TextLayer와 2방법 두가지가 있음

new_text_layer.textItem.contents = 'Hello, World!' 
new_text_layer.textItem.position = [160, 167] # 텍스트레이어의 위치 설정
new_text_layer.textItem.size = 40 
new_text_layer.textItem.color = text_color 
options = ps.JPEGSaveOptions(quality=5) # 압축 품질을 5로 설정한 JPEG 저장 옵션을 생성  # 품질0 높은압축,높은손실 / 품질100 낮은압축, 거의손실없음

# # save to jpg
jpg = 'C:/workspace/2_작업/2023.12.08/hello_world.jpg'
doc.saveAs(jpg, options, asCopy=True) # 이미지의 저장옵션을 jpeg로 설정하고, 원본문서를 유지한 채로 저장
app.doJavaScript(f'alert("save to jpg: {jpg}")') #JavaScript 코드를 실행하여 경고 창을 띄웁니다. 이 창에는 저장된 JPEG 파일의 경로가 포함




# from photoshop import Session

# # 이 세션을 ps라는 이름으로 사용하겠다.
# # action="new_document" : Photoshop 세션을 열 때 새로운 문서를 만들라는 명령
# with Session(action="new_document") as ps: 
#     doc = ps.active_document

      # 텍스트 색상을 설정
#     text_color = ps.SolidColor()
#     text_color.rgb.green = 255

      # 새로운 텍스트 레이어 추가
#     new_text_layer = doc.artLayers.add()
#     new_text_layer.kind = ps.LayerKind.TextLayer

#     # 텍스트 레이어 속성 설정
#     new_text_layer.textItem.contents = 'Hello, World!'
#     new_text_layer.textItem.position = [160, 167]
#     new_text_layer.textItem.size = 40
#     new_text_layer.textItem.color = text_color

#     # JPEG 형식으로 저장하는 옵션 설정
#     options = ps.JPEGSaveOptions(quality=5)
#     jpg = 'C:/workspace/2_작업/2023.12.08/hello_world.jpg'
#     doc.saveAs(jpg, options, asCopy=True)
#     ps.app.doJavaScript(f'alert("save to jpg: {jpg}")')