    const menu = document.querySelector('.menu');
    const menuOptions = document.querySelector('.menu-options');

    menu.addEventListener('click', () => {
        menuOptions.style.display =
            menuOptions.style.display === 'block' ? 'none' : 'block';
    });