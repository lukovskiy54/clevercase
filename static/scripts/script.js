

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



const burgerButton = document.querySelector('.menu-container')
const openBurger = document.querySelector('.burger-open')

if (burgerButton) {
    burgerButton.addEventListener('click', function () {
        openBurger.classList.toggle('is-active');
    });
}
