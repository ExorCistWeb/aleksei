// Для авто-высоты
var aboutBoxQest = document.querySelector('.about_box_qest');
var aboutBoxAbs = document.querySelector('.about_box_abs');

aboutBoxAbs.style.height = getComputedStyle(aboutBoxQest).height;

// Вопросы
new Accordion('.accordion-container');

// Табы
function openTab(evt, tabName) {
    $(".tabcontent").hide();
    $(".tablinks").removeClass("active");
    $("#" + tabName).show();
    evt.currentTarget.className += " active";
}
$(document).ready(function() {
    $("#Tab1").show();
    $(".tablinks:first").addClass("active");
    $(".tablinks:first").click(function() {
        $(".tabcontent").hide();
        $("#Tab1").show();
        $(".tablinks").removeClass("active");
        $(".tablinks:first").addClass("active");
    });
});

// Скролл

// выбираем все ссылки на странице
const links = document.querySelectorAll('a[href^="#"]');

// добавляем обработчик клика на каждую ссылку
links.forEach(link => {
    link.addEventListener('click', function(event) {
        // отменяем стандартное поведение ссылки
        event.preventDefault();

        // получаем целевой элемент, к которому нужно проскроллить страницу
        const targetElement = document.querySelector(this.getAttribute('href'));

        // вычисляем расстояние от начала страницы до целевого элемента
        const targetOffset = targetElement.offsetTop;

        // задаем плавную прокрутку до целевого элемента
        window.scrollTo({
            top: targetOffset,
            behavior: 'smooth'
        });
    });
});