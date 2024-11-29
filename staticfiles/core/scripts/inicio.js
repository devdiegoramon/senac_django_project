// Seleciona o ícone do usuário e o menu dropdown
const userIcon = document.getElementById('user-icon');
const dropdownMenu = document.getElementById('user-dropdown');

// Função para alternar a visibilidade do dropdown
userIcon.addEventListener('click', function(e) {
    e.preventDefault(); // Impede o comportamento padrão do link
    dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
});

// Fecha o menu dropdown se o clique ocorrer fora do ícone ou do menu
document.addEventListener('click', function(e) {
    if (!userIcon.contains(e.target) && !dropdownMenu.contains(e.target)) {
        dropdownMenu.style.display = 'none'; // Esconde o dropdown
    }
});


document.getElementById('formulario').addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o envio do formulário

    // Captura os dados do formulário
    var nome = document.getElementById('nome').value;
    var email = document.getElementById('email').value;
    var cpf = document.getElementById('cpf').value;

    // Exibe as informações na tela
    document.getElementById('resultado-nome').textContent = nome;
    document.getElementById('resultado-email').textContent = email;
    document.getElementById('resultado-cpf').textContent = cpf;

    // Mostra a área de resultados
    document.getElementById('resultado').style.display = 'block';
});

const prevButton = document.getElementById('prev');
const nextButton = document.getElementById('next');
const carrossel = document.querySelector('.carrossel');
let currentIndex = 0;
const totalImages = document.querySelectorAll('.carrossel-image').length;

prevButton.addEventListener('click', () => {
    currentIndex = (currentIndex === 0) ? totalImages - 1 : currentIndex - 1;
    carrossel.style.transform = `translateX(-${currentIndex * 100}%)`;
});

nextButton.addEventListener('click', () => {
    currentIndex = (currentIndex === totalImages - 1) ? 0 : currentIndex + 1;
    carrossel.style.transform = `translateX(-${currentIndex * 100}%)`;
});


