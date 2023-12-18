// 포토샵 2024 버전에서 도구를 선택하는 코드 수정
$.level = 1;

try {
    var moveToolID = stringIDToTypeID("moveTool");
    var desc = new ActionDescriptor();
    var ref = new ActionReference();
    ref.putClass(moveToolID);
    desc.putReference(charIDToTypeID("null"), ref);

    // 새로운 코드로 도구를 직접 선택
   // desc.putBoolean(stringIDToTypeID("dontRecord"), true);
   
    // 여기서 "Y"는 할당할 키보드 단축키입니다. 원하는 키로 변경하세요.
    desc.putString(charIDToTypeID("T   "), "Y");
    
    // "select" 대신 "set"을 사용하여 도구를 설정합니다.
    executeAction(stringIDToTypeID("set"), desc, DialogModes.NO);

} catch (e) {
    $.writeln("Error: " + e);
    alert(e);
}