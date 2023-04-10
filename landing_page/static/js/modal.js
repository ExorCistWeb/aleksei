$(document).ready(function() {

    $('.openModal').click(function() {

        $('.modal').show();

        $('body').addClass('modal-open');

    });

    $('.modal-close').click(function() {

        $('.modal').hide();

        $('body').removeClass('modal-open');

    });

    $('.modal').click(function(e) {

        if (e.target == this) {

            $('.modal').hide();

            $('body').removeClass('modal-open');

        }

    });

});





// Get the modal and image content elements
const modal = document.getElementById("modal_img");
const imgContent = document.getElementById("modal_img_content");
const images = document.querySelectorAll(".swiper_doc .swiper-slide img");
let currentImageIndex = 0;

// Set the image source to the clicked image's source
function openModal(src) {
    imgContent.src = src;

    // Show the modal
    modal.style.display = "flex";
    document.body.classList.add("modal-open");

    // Get the index of the clicked image in the images array
    currentImageIndex = Array.from(images).indexOf(src);
}

// Close the modal window when close button is clicked
function closeModal() {
    // Hide the modal
    document.body.classList.remove("modal-open");
    modal.style.display = "none";

    // Reset the current image index to 0 when closing the modal window 
    currentImageIndex = 0;
}

// Show the previous image when prev button is clicked 
function prevImage() {
    if (currentImageIndex > 0) {
        currentImageIndex--;

        imgContent.src = images[currentImageIndex].src;

    } else {

        // If it's the first image, show the last one 
        currentImageIndex = images.length - 1;

        imgContent.src = images[currentImageIndex].src;

    }
}

// Show the next image when next button is clicked 
function nextImage() {

    if (currentImageIndex < images.length - 1) {

        currentImageIndex++;

        imgContent.src = images[currentImageIndex].src;

    } else {

        // If it's the last image, show the first one 

        currentImageIndex = 0;

        imgContent.src = images[currentImageIndex].src;

    }
}