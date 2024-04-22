document.addEventListener("DOMContentLoaded", function() {
    var my_friends = document.getElementById('my_friends');
    var friends_pop_up = document.getElementById('friends_pop_up');
    var profile_btn = document.getElementById('profile_btn');
    var profile_pop_up = document.getElementById('profile_pop_up');

    my_friends.addEventListener('click', function() {
        if (profile_pop_up.style.display == 'block') {
            profile_pop_up.style.display = 'none';
        }
        if (friends_pop_up.style.display == 'block') {
            friends_pop_up.style.display = 'none';
        }
        else { friends_pop_up.style.display = 'block'; }
    });

    profile_btn.addEventListener('click', function() {
        if (friends_pop_up.style.display == 'block') {
            friends_pop_up.style.display = 'none';
        }
        
        if (profile_pop_up.style.display == 'block') {
            profile_pop_up.style.display = 'none';
        }
        else { profile_pop_up.style.display = 'block'; }
    });
});

// Hide all popups
document.addEventListener('mousemove', (event) => {
    if (event.clientX < window.outerWidth / 2 || event.clientY > window.outerHeight / 2) {
        profile_pop_up.style.display = 'none';
        friends_pop_up.style.display = 'none';
    }
});

function log_out() {
    alert('Logging out');
}

function main_menu() {
    alert('going to main menu');
}