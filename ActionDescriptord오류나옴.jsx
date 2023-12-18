// 포토샵 2024 버전에서 도구를 선택하는 코드
// 이거는 선택 못한다는 오류가 아닌 // Result: [ActionDescriptor] // Error: 오류: 필요한 값이 없습니다. 이런 오류가나옴
$.level = 1;

try {
    var moveToolID = stringIDToTypeID("moveTool");
    var desc = new ActionDescriptor();
    var ref = new ActionReference();
    ref.putClass(moveToolID);
    desc.putReference(charIDToTypeID("null"), ref);

    // 새로운 코드로 도구를 직접 선택
    desc.putBoolean(stringIDToTypeID("dontRecord"), true);
    executeAction(stringIDToTypeID("select"), desc, DialogModes.NO);

var currentTool = app.activeDocument.activeTool;
alert("현재 선택된 도구: " + currentTool);

} catch (e) {
    $.writeln("Error: " + e);
    alert(e);
   
}