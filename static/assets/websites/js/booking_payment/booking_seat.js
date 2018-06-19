$(document).ready(function() {
    var id_server = $('#id_server').val();
    var id_showtime = $('#id_showtime').val();
    var movie_api_id = $('#movie_api_id').val();
    // variable setTimeout
    var timer;

    // Get list seats
    $.ajax({
        url: "/movie/seats",
        type: 'GET',
        data: {
            "id_showtime": id_showtime,
            "id_server": id_server
        },
        dataType: 'json',
        crossDomain:false,
        context: this,
        beforeSend: function( ) {
            // add image loader
            $('.ajax-loader').addClass('ajax-loader-booking');
        }
    })
    .done(function(response) {
        // remove image loader
        $('.ajax-loader').removeClass('ajax-loader-booking');
        // Check List seat 
        if(response.List && response.List.length > 0){
            // function from booking_create_seat.js
            bookingSeat(response.List, id_showtime, id_server, movie_api_id);

            // disable select seat when keydown key space
            // Step 1: Turn off keydown (key space), override event keydown (key space) in library seat-charts.
            // Step 2: Turn on keydown and handle event prevenDefault
            $("#seat-map .seatCharts-row div.seatCharts-seat.seatCharts-cell.available").off("keydown");
            $("#seat-map .seatCharts-row div.seatCharts-seat.seatCharts-cell.available").on("keydown", function(e){
                if (e.which == 32) {
                    e.preventDefault();
                }        
            });
            // Disable forcus outside  area choice seat 
            $('#seat-map').unbind("focus");
        }else{
            // show message when List seat empty, setTimeout 10s back home
            displayMsg();
            $('.msg-result-js').html(msgResult("Lỗi hệ thống! Vui lòng liên hệ "
                +"với admin để được hỗ trợ, hệ thống sẽ quay lại trang chủ sau 10 giây. Cảm ơn!", "danger"));
            timer = setTimeout(function(){ 
                window.location ='/';
            }, 10000);
        }
        
    })
    .fail(function(error) {
        displayMsg();
        if(error.status == 400){
            $('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
        }else{
            $('.msg-result-js').html(msgResult("Error get seats", "danger"));
        }
    });

    // Clear setTimeout when click show popup schedule in 10s back home
    $('.popup-movie-schedule').on('click', function(){
        window.clearTimeout(timer);
    });
});