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


function openModal(src) {
    // Get the modal and image content elements
    const modal = document.getElementById("modal_img");
    const imgContent = document.getElementById("modal_img_content");

    // Set the image source to the clicked image's source
    imgContent.src = src;

    // Show the modal
    modal.style.display = "block";
    document.body.classList.add("modal-open");
}

function closeModal() {
    // Get the modal element
    const modal = document.getElementById("modal_img");

    // Hide the modal
    document.body.classList.remove("modal-open");
    modal.style.display = "none";
}