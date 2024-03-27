const border = document.getElementById('border');
const popup = document.getElementById('popup');

// Profile popup logic
border.addEventListener('click', () => {
    popup.style.display = 'block';
});

popup.addEventListener('mouseleave', () => {
    popup.style.display = 'none';
});

document.addEventListener('mousemove', (event) => {
    if (event.clientX < window.innerWidth / 1.4 || event.clientY > window.innerHeight / 1.4)
        popup.style.display = 'none';
});


function log_out() {
    alert('Logging out');
}

function main_menu() {
    alert('going to main menu');
}