function calcular(){
    
    var peso = document.getElementById("Peso").value
    var altura = document.getElementById("Altura").value

    if(altura == null || peso == null || altura == 0 || peso == 0){
        alert('Não é possível calcular o IMC, digite algum valor!!!!')
    } else{
        imc = peso/(altura*altura);
        alert(imc)
    }


}