



// Seleciona o botão e a div da mensagem
const botao = document.getElementById('btn-criado');
const mensagemDiv = document.getElementById('conta-criada');

// Define a função a ser executada quando o botão for clicado
botao.addEventListener('click', () => {
    // Define a mensagem de sucesso para o alert
    const mensagemAlert = 'Conta criada com sucesso!!!';
    alert(mensagemAlert); // Exibe o alert

    // Define a mensagem de sucesso para a div
    const contacriada = 'Ação realizada com sucesso!!!';

    // Define o conteúdo da div da mensagem como a mensagem de sucesso
    mensagemDiv.textContent = contacriada;

    // Limpa a mensagem após um tempo (opcional)
    setTimeout(() => {
        mensagemDiv.textContent = '';
    }, 3000); // Limpa a mensagem após 3 segundos (ajuste conforme necessário)
});



function buscaCep(){
    let cep = document.getElementById('inputCep').value;
    if(cep !== ""){
        let url = "https://brasilapi.com.br/api/cep/v1/" + cep;

        let req = new XMLHttpRequest();
        req.open("GET", url);
        req.send();

        req.onload = function(){
            if(req.status === 200){
                let endereco = JSON.parse(req.response);
                document.getElementById("inputEndereco").value = endereco.street;
                document.getElementById("inputBairro").value = endereco.neighborhood;
                document.getElementById("inputCidade").value = endereco.city;
                document.getElementById("inputEstado").value = endereco.state;
            }
            else if(req.status === 404){
                alert("CEP inválido");
            }
            else{
                alert("Erro ao fazer a requisição");
            }
        }
    }
}

window.onload = function (){
    let cep = document.getElementById("inputCep");
    cep.addEventListener("blur", buscaCep);
};



var hamburguers = document.getElementById('hamburguers');

hamburguers.addEventListener('click', function(){
    var hamburguer_atual = window.getComputedStyle(hamburguers);

    if(hamburguer_atual.display === 'none'){
        hamburguers.style.display = 'block'
    }else{
        hamburguers.style.display = 'none'
    }
});