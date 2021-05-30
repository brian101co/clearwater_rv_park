document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var mobileMenu = document.querySelectorAll('.sidenav');

    

    var mobileMenuInstances = M.Sidenav.init(mobileMenu);
    var instances = M.Dropdown.init(elems, {
        coverTrigger: false,
        hover: true,
    });

    console.log(instances);
});