$(document).ready(function() {

    // check image exist?
    if($(".image_home_ads").length > 0){
        $('#popup_advertise').modal('show');
        $("#popup_advertise .modal-dialog").velocity("transition.flipYIn", {
            duration: 2000
        });

        // Set css overflow = hidden, disable scroll
        $('#popup_advertise').on('shown.bs.modal', function() {
            $('.modal-open, #popup_advertise').css("overflow","hidden");
        });

        // Set css overflow = auto, could scroll
        $('#popup_advertise').on('hide.bs.modal', function() {
            $('.modal-open, #popup_advertise').css("overflow","auto");
        });
    }

    // Hide arrow next, pre when quantity image < 2 
    function hideArrowPopupSlide(){
        var count_image = $('#popup_advertise #jssor_2 .jssor_1_slides a>img').length;
        if(count_image < 2){
            $('#popup_advertise .jssora106').css('opacity', 0);
        }
    }
    hideArrowPopupSlide();

    // turn off play slide film showin and comsoon when show poup adversite 
    $('#popup_advertise').mouseleave(function() {
        $('#movie-tab-1 .owl-carousel, .owl-carousel.style2').trigger('play.owl.autoplay',[1000]);
    }).mouseover(function() {
        $('#movie-tab-1 .owl-carousel, .owl-carousel.style2').trigger('stop.owl.autoplay');
    });
});