document.addEventListener('DOMContentLoaded', function() {
    var mobileMenu = document.querySelector('.sidenav');
    var copyrightYear = document.querySelector('.copyright-year');
    var mobileMenuInstance = M.Sidenav.init(mobileMenu);

    copyrightYear.innerText = new Date().getFullYear();

    for (let menuItem of mobileMenu.children) {
        menuItem.addEventListener("click", function() {
            mobileMenuInstance.close();
        });
    }
});