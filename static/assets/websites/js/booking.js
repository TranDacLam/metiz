$(document).ready(function() {

    // Validate member_card only input alpha
    $("#member_card").on("input", function(){
        var regexp = /[^a-zA-Z0-9]/g;
        if($(this).val().match(regexp)){
            $(this).val( $(this).val().replace(regexp,'') );
        }
    });

    //fix background scroll in modals on mobile
    if (navigator.userAgent.match(/iPhone|iPod|iPad|Android|Windows Phone|BlackBerry/i)) {
        // back scroll when close popup member card
        $('#member_card_modal').on('hide.bs.modal', function() {
            $('html, body').animate({
                scrollTop: $(".name-movie-booking").offset().top
            }, 10);
        });
    }

    // format date movie
    $('.date-movie-booking').text(getDate());
    
    function getDate(){
        var date_shedule = $('.date-movie-booking').text();
        return date_shedule.replace(/([0-9]{4})\-([0-9]{2})\-([0-9]{2})/g, '$3-$2-$1');
    }
});
