// 예시: 탐색 도구 (Move Tool)를 선택하는 코드
$.level = 1;
try{

var move_tool = app.charIDToTypeID("ObjT");
var desc = new ActionDescriptor();
desc.putClass(app.charIDToTypeID("null"), move_tool);
app.executeAction(app.charIDToTypeID("slct"), desc, DialogModes.NO);

}catch(e){
    $.writeln ("Error: " + e);
    alert (e);
  }