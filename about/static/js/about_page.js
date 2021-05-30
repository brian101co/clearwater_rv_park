document.addEventListener('DOMContentLoaded', function() {
    var paras = document.querySelectorAll('.main-text');

    paras.forEach(para => {
        para.classList.add('flow-text')
    });
});