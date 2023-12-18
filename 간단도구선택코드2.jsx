$.level = 1;
try{
var idslct = charIDToTypeID( "slct" );
var desc = new ActionDescriptor();
var idnull = charIDToTypeID( "null" );
var idmoveTool = stringIDToTypeID( "moveTool" ); // "moveTool"은 개체 선택 도구입니다.
desc.putClass( idnull, idmoveTool );
executeAction( idslct, desc, DialogModes.NO );

}catch(e){
    $.writeln ("Error: " + e);
    alert (e);
    }