const display = document.getElementbyID("display");

function appendToDIsplay(input){
    display.avlue += input;
}

funtion clearDisplay(){
    display.value = "";
}

function calculate(){
    try{
        display.value = eval(display.value);
    }
    catch(error){
        display.value = "Error"
    }
}

