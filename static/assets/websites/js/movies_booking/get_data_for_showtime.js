// Call server get data movie showtime

function getDataPopupMovieSchedule(element) {
    var id_server = $('#data-id-server').val();
    var movie_api_id = $('#data_movie_api_id').val();


    if ($(element).attr("movie-day-selected")) {
        var date_query = $(element).attr("movie-day-selected");
        // Active Date Selected on List Schedule
        $('#modal-movie-showtimes .days-movie-showing [movie-day-selected = ' + date_query + ']').addClass('active-date');

    } else {
        // Handle When exception get data but date query is empty
        var date_query = new Date().toJSON().slice(0, 10).replace(/-/g, '-');
        // Active First Day in List Schedules
        $('#modal-movie-showtimes .days-movie-showing li:first').addClass('active-date');
        // Add month from first day in List Schedule
        $('#center-month').text($('.days-movie-showing li:first').children('.hide-month').text());
    }

    // Call Ajax get movie show time with current date
    // cinema_id is equal id_server
    data = {
        "date": date_query,
        "cinema_id": id_server,
        "movie_api_id": movie_api_id

    }

    $.ajax({
        url: "/movie/show/times",
        type: 'get',
        data: data,
        dataType: 'json',
        crossDomain: false,
        context: this,
    })
    .done(function(response) {
        var html = '';
        $.each(response, function(key, value) {
            if (value.lst_times.length > 0) {
                 // Ignore movie Test to server production
                if (document.domain == "metiz.vn" && movieIdTest == value.movie_id ) {
                    return;
                }
                // Call action from file build_html_movie_showtime.js . Using render html list movies showtime from 
                html += render_schedule_html(value);
            }
        });
        
        if( html !== '' ){
            $("#modal-movie-showtimes").find('.list-movies-showtime-by-day').html(html);    
            trigger_click_showtime();
        }else{
            $("#modal-movie-showtimes").find('.list-movies-showtime-by-day').html('<p class="empty-schedule">Ngày Bạn Chọn Hiện Không Có Lịch Chiếu Nào. Vui Lòng Chọn Ngày Khác.<p/>');
        }
    })
    .fail(function() {
        displayMsg();
        $('.msg-result-js').html(msgResult("Error schedule film!", "danger"));
    });

}

function trigger_click_showtime() 
{        
    // TH2: Click đặt vé a movie
    
    $('.sold-out a').on('click', function(event) {
        if (navigator.userAgent.match(/iPhone|iPod|iPad|Android|Windows Phone|BlackBerry/i)) {
            /* change background for schedule firm on mobile */
            $(this).addClass('mobile-schedule');
            $('.modal-schedule').on('hide.bs.modal', function() {
                $('.sold-out a').removeClass('mobile-schedule');
            });
        }
        // *** Check Movie allow booking ***
        var allow_booking = $(this).children('input[name=allow_booking]').val();
        if (allow_booking == 'false') {
            $('#alert_allow_booking').modal('show');
            return;
        }
        
        
        // Call action from file validation_showtime.js . Using validation movie start time remain 15 minutes
        if(validate_time_remain($(this))){
            // Call action from file showtimes_handle_show_popup.js . Using show popup user information
            show_popup_user_information($(this));
        }
    });
    
}