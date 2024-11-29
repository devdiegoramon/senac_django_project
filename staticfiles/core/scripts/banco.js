// Função para exibir o campo "Outro Banco" caso o usuário escolha a opção "Outro Banco"
function mostrarOutroBanco() {
    var bancoSelecionado = document.getElementById('banco').value;
    var outroBancoDiv = document.getElementById('outroBanco');
    
    if (bancoSelecionado === '999') {
        outroBancoDiv.style.display = 'block';
    } else {
        outroBancoDiv.style.display = 'none';
    }
}

// Função para exibir/ocultar o formulário de feedback
document.getElementById('feedback-btn').addEventListener('click', function() {
    var feedbackFormContainer = document.getElementById('feedback-form-container');
    feedbackFormContainer.style.display = 'block';
});

// Função para fechar o formulário de feedback
document.getElementById('close-feedback').addEventListener('click', function() {
    var feedbackFormContainer = document.getElementById('feedback-form-container');
    feedbackFormContainer.style.display = 'none';
});

// Função para enviar o feedback
document.getElementById('submit-feedback').addEventListener('click', function() {
    var feedbackText = document.getElementById('feedback-text').value;
    if (feedbackText.trim() === '') {
        alert('Por favor, insira seu feedback antes de enviar.');
    } else {
        // Aqui você pode implementar o envio do feedback, como uma chamada para o backend (por exemplo, usando fetch ou AJAX)
        alert('Feedback enviado: ' + feedbackText);
        document.getElementById('feedback-text').value = ''; // Limpa o campo de feedback
        document.getElementById('feedback-form-container').style.display = 'none'; // Fecha o formulário de feedback
    }
});

// Validação do formulário bancário (para garantir que todos os campos estão preenchidos corretamente)
document.getElementById('formBancario').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário por padrão para realizar a validação

    var banco = document.getElementById('banco').value;
    var agencia = document.getElementById('agencia').value;
    var conta = document.getElementById('conta').value;
    var autenticacao = document.getElementById('autenticacao').value;

    // Verificar se todos os campos obrigatórios foram preenchidos
    if (!banco || !agencia || !conta || !autenticacao) {
        alert('Por favor, preencha todos os campos obrigatórios.');
        return;
    }

    // Se o banco selecionado for "Outro Banco", verificar se o nome foi informado
    if (banco === '999') {
        var outroBancoInput = document.getElementById('outroBancoInput').value;
        if (!outroBancoInput) {
            alert('Por favor, informe o nome do banco.');
            return;
        }
    }

    // Se tudo estiver correto, enviar o formulário (aqui você pode realizar a lógica de envio real, por exemplo, usando fetch)
    alert('Formulário enviado com sucesso!');
    // Para fins de demonstração, você pode submeter o formulário aqui, se necessário:
    // this.submit();
});
