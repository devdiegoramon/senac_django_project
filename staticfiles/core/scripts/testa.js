let currentIndex = 0;
const items = document.querySelectorAll('.carousel-item');
const totalItems = items.length;

function updateCarousel() {
    const offset = -currentIndex * 100; // Desloca a posição das imagens
    document.querySelector('.carousel').style.transform = `translateX(${offset}%)`;
}

function moveSlide(direction) {
    currentIndex += direction;
    if (currentIndex < 0) {
        currentIndex = totalItems - 1; // Volta para o último item se for o primeiro
    } else if (currentIndex >= totalItems) {
        currentIndex = 0; // Volta para o primeiro item se for o último
    }
    updateCarousel();
}

// Inicialização
updateCarousel();
