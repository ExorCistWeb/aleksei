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