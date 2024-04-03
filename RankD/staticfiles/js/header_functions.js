const border = document.getElementById('border');
const popup = document.getElementById('popup');

// My friends popup logic
my_friends.addEventListener('click', () => {
    friends_popup.style.display = 'block';
});

friends_popup.addEventListener('mouseleave', () => {
    friends_popup.style.display = 'none';
});


// Profile popup logic
border.addEventListener('click', () => {
    profile_popup.style.display = 'block';
});

profile_popup.addEventListener('mouseleave', () => {
    profile_popup.style.display = 'none';
});

// Hide all popups
document.addEventListener('mousemove', (event) => {
    if (event.clientX < window.outerWidth / 2 || event.clientY > window.outerHeight / 2) {
        profile_popup.style.display = 'none';
        friends_popup.style.display = 'none';
    }
});


function log_out() {
    alert('Logging out');
}

function main_menu() {
    alert('going to main menu');
}