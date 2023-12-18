// 특정 도구에 키보드 단축키 할당하는 코드
try {
    var desc = new ActionDescriptor();
    var ref = new ActionReference();
    ref.putProperty(charIDToTypeID("Prpr"), charIDToTypeID("Tool"));
    ref.putEnumerated(charIDToTypeID("capp"), charIDToTypeID("Ordn"), charIDToTypeID("Trgt"));
    desc.putReference(charIDToTypeID("null"), ref);

    // 여기서 "Y"는 할당할 키보드 단축키입니다. 원하는 키로 변경하세요.
    desc.putString(charIDToTypeID("T   "), "Y");
    executeAction(stringIDToTypeID("set"), desc, DialogModes.NO);

} catch (e) {
    $.writeln("Error: " + e);
    alert(e);
}