var swiper = new Swiper(".mySwiper", {
    speed: 600,
    parallax: true,
    loop: true,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});

var swiper = new Swiper(".myDocument", {
    slidesPerView: 3.5,
    centeredSlides: true,
    speed: 600,
    spaceBetween: 30,
    grabCursor: true,
    loop: true,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        320: {
            slidesPerView: 1.5,
        },
        500: {
            slidesPerView: 1.5,
        },
        1280: {
            slidesPerView: 3.5,
        }
    }
});
var swiper = new Swiper(".myAwards", {
    slidesPerView: 3.5,
    centeredSlides: true,
    speed: 600,
    spaceBetween: 30,
    grabCursor: true,
    loop: true,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        320: {
            slidesPerView: 1.8,
        },
        500: {
            slidesPerView: 2.5,
        },
        1280: {
            slidesPerView: 3.5,
        }
    }
});