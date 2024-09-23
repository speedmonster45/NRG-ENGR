function loadHamburgerMenu() {
    fetch('/_includes/hamburgerMenu.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('hamburger-container').innerHTML = data;
            HamburgerMenu.initialize(); // Initialize the HamburgerMenu object after loading
        })
        .catch(error => console.error('Error loading the hamburger menu:', error));
}

const HamburgerMenu = {
    menuElement: null,
    hamburgerElement: null,

    toggleMenu: function() {
        this.menuElement.classList.toggle('hidden');
    },

    closeMenuOnLinkClick: function() {
        const links = this.menuElement.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', () => {
                this.menuElement.classList.add('hidden');
            });
        });
    },

    initialize: function() {
        this.menuElement = document.getElementById('menu');
        this.hamburgerElement = document.getElementById('hamburger');
        this.hamburgerElement.addEventListener('click', () => {
            this.toggleMenu();
        });
        this.closeMenuOnLinkClick();
    }
};

document.addEventListener('DOMContentLoaded', loadHamburgerMenu);
