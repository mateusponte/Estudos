class Cadastro{
    constructor(nome, sobrenome, altura, peso){
        this.nome;
        this.sobrenome;
        this.altura;
        this.personalbar;
    }

    validarDados(){
        for(let i in this){
            if (this[i] == underfined || this[i] =='' || this[i] == null){
                return false
            }

            return true
        }
    }

}


