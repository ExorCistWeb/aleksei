$(document).ready(function() {

    $('#openModal').click(function() {

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