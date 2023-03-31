var swiper = new Swiper(".mySwiper", {
    speed: 600,
    parallax: true,

    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});

var swiper = new Swiper(".myDocument", {
    slidesPerView: 3.5,
    centeredSlides: true,
    spaceBetween: 30,
    grabCursor: true,
    loop: true,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});