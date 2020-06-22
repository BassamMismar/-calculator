function getHistory() {
    return document.getElementById("history-value").innerText;   
}
function printHistory(num) {
    document.getElementById("history-value").innerText = num;
       
}
function getHoutput() {
    return document.getElementById("output-value").innerText;   
}

function printoutput(num) {
    if(num == ""){
        document.getElementById("output-value").innerText =num;
    
        }else{
            document.getElementById("output-value").innerText =getFormattedNumber(num);    
        }
}
    
function getFormattedNumber(num) {
    var n = Number(num);
    var value =n.toLocaleString("en");
    return value;
}
printoutput("")