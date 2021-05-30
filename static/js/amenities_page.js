document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.carousel');
    var instances = M.Carousel.init(elems, {
        numVisible: 3,
    });

    if (window.innerWidth < 600) {
        document.querySelectorAll('.horizontal').forEach(function (elem) {
            elem.classList.remove('horizontal')
        });
    }

});