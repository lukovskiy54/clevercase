

const menuButton = document.querySelector('.menu-container')
const openMenu = document.querySelector('.open-menu')

if (menuButton) {
    menuButton.addEventListener('click', function () {
        openMenu.classList.toggle('is-active');
    });
}

const profileButton = document.querySelector('.add-account-container')
const openAddAccount = document.querySelector('.add-account')

if (profileButton) {
    profileButton.addEventListener('click', function () {
        openAddAccount.classList.toggle('is-active');
    });
}

function playSound() {
    var sound = document.getElementById("mySound");
    sound.currentTime = 0;
    sound.play();
}