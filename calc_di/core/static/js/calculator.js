/*
*Author: Daniel Ilaro da Silva
*/

var listOperation = ['/', '*', '-', '+'];
var calc = 0;
var locationOperationG = -1;

function addNumber(value, screenCalc){
    var oper = false;

    for(o in listOperation){ 
        if(listOperation[o] == value){oper=true;} 
    }
    if (screenCalc.val() == '0' || (calc == 2 && !oper)){
        screenCalc.val(value);
        calc = 0;
    }
    else{
        screenCalc.val(screenCalc.val() + value);
        if (calc == 2){calc=0;}
    }
}

function preparedCalc(screenCalc, posOperation){
    operation = screenCalc.val()[posOperation];
    number1 = parseInt(screenCalc.val().substr(0,posOperation));
    number2 = parseInt(screenCalc.val().substr(posOperation+1,screenCalc.val().length));

    if(isNaN(number1) || isNaN(number2)){
        screenCalc.val(screenCalc.val());
    }

    resultado = calculator(operation, number1, number2);
    screenCalc.val('');
    calc=2;
    addNumber(resultado, screenCalc);
}

function searchOperation(screenCalc){

    if (calc == 0){ 
        for (o in listOperation){
            locationOperation = screenCalc.val().indexOf(listOperation[o]);
            
            if (locationOperation != -1) {
                calc=1;
                break
            }
        }
        locationOperationG =locationOperation;
    }
    else {
        for (o in listOperation){
            locationOperation = screenCalc.val().indexOf(listOperation[o], locationOperationG+1);

            if (locationOperation != -1) {
                preparedCalc(screenCalc, locationOperationG);
                break
            }
        }
    }    
}

function calculator(operation, n1, n2){
    resultado = 0;
    
    if (operation == '/') { resultado = n1 / n2; }

    else if (operation == '*') { resultado = n1 * n2; }
    
    else if (operation == '-') { resultado = n1 - n2; }
    
    else if (operation == '+') { resultado = n1 + n2; }

    return resultado;
}

function main(value){
    var screenCalc = $("#screenCalc"); 

    if (value == 'clean'){
        screenCalc.val(0);
    }
    else if(value == '='){
        preparedCalc(screenCalc, locationOperationG);
    }
    else {
        addNumber(value, screenCalc); 
        searchOperation(screenCalc);
    }
}

$(document).ready(function (){

    $('Button').click(function () {  
        main($(this).attr('id'));
    })
});