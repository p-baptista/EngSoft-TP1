document.addEventListener("DOMContentLoaded", function() {
    var my_friends = document.getElementById('my_friends');
    var friends_pop_up = document.getElementById('friends_pop_up');
    var search_friends = document.getElementById('search_friends');
    var add_friends_pop_up = document.getElementById('add_friends_pop_up');
    var add_friend_form = document.getElementById('add_friend_form');
    var profile_btn = document.getElementById('profile_btn');
    var profile_pop_up = document.getElementById('profile_pop_up');
    

    my_friends.addEventListener('click', function() {
        if (profile_pop_up.style.display == 'block') {
            profile_pop_up.style.display = 'none';
        }
        if (add_friends_pop_up.style.display == 'block') {
            add_friends_pop_up.style.display = 'none';
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
        if (add_friends_pop_up.style.display == 'block') {
            add_friends_pop_up.style.display = 'none';
        }
        if (profile_pop_up.style.display == 'block') {
            profile_pop_up.style.display = 'none';
        }
        else { profile_pop_up.style.display = 'block'; }
    });

    search_friends.addEventListener('click', function() {
        if (profile_pop_up.style.display == 'block') {
            profile_pop_up.style.display = 'none';
        }
        if (add_friends_pop_up.style.display == 'none') {
            add_friends_pop_up.style.display = 'block';
        }
        else { add_friends_pop_up.style.display = 'block'; }
    });
});

function log_out() {
    alert('Logging out');
}

function main_menu() {
    alert('going to main menu');
}