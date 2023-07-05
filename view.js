

async function  run(){
    template1='<tr>\n<th>${SNO}<th>\n<input type="checkbox" id="${SNO}">\n<th>${dataWeb}</th>\n${data}</tr>'
    template2='<td><a href="${link}">${link_shot}</a><input type="checkbox" id="${SNO_i}"></td>\n'
    maintext=''
    data=await fetch("./newData.json");
    data=await data.json()
    window.data=data
    console.log(data)
    table=document.getElementsByTagName("table")[0]
    key=Object.keys(data)
    for (let index = 0; index < key.length; index++) {
        mainPoop=data[key[index]]
        tempMainText=''
        for (let index2 = 0; index2 < mainPoop.length; index2++) {
            link=mainPoop[index2]
           tempMainText=tempMainText+template2.replace("${link}",link).replace("${link_shot}",link.replace("https://","").replace("http://","").replace(key[index],"").slice(0,35)).replace("${SNO_i}",index+"_"+index2)

        }
        maintext=maintext+template1.replace("${data}",tempMainText).replace("${dataWeb}",key[index]).replaceAll("${SNO}",index+1);
        table.innerHTML=maintext;
}}
window.onload=function(){

    setTimeout(run,1000)
}
function downloadObjectAsJson(exportObj, exportName){
    var dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(exportObj));
    var downloadAnchorNode = document.createElement('a');
    downloadAnchorNode.setAttribute("href",     dataStr);
    downloadAnchorNode.setAttribute("download", exportName + ".json");
    document.body.appendChild(downloadAnchorNode); // required for firefox
    downloadAnchorNode.click();
    downloadAnchorNode.remove();
  }

function down(){
    data=window.data
    table=document.getElementsByTagName("table")[0]
    key=Object.keys(data)
    for (let index = 0; index < key.length; index++) {
        mainPoop=data[key[index]]
        ischecked=document.getElementById(index+1+"").checked
        whichChecked=-1
        for (let index2 = 0; index2 < mainPoop.length; index2++) {
            ischeckedV2=document.getElementById(index+"_"+index2).checked
            if (ischeckedV2){
                whichChecked=index2;
                break;
            }
        }
        data[key[index]]={
            urls:mainPoop,
            ischecked:ischecked,
            whichChecked:whichChecked
        }

}
downloadObjectAsJson(Object(data),document.getElementsByTagName("input")[0].value)
}