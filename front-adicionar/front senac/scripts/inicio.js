const userIcon = document.getElementById('user-icon');
const dropdownMenu = document.getElementById('user-dropdown');

userIcon.addEventListener('click', function(e) {
    e.preventDefault();
    dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
});

document.addEventListener('click', function(e) {
    if (!userIcon.contains(e.target) && !dropdownMenu.contains(e.target)) {
        dropdownMenu.style.display = 'none';
    }
});
