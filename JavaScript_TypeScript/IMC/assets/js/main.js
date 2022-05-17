function calcular(){
    var peso = document.getElementById("Peso").value
    var altura = document.getElementById("Altura").value

    imc = peso/(altura*altura);
    alert(imc)
}