$(document).ready(function() {
    var id_server = $('#data-id-server').val();
    
    // Trigger event when user click showtime movie schedule (lich chieu)
    $('.open-movie-showtime').magnificPopup({
        type: 'inline',
        midClick: true,
        enableEscapeKey: false,
        fixedContentPos: true,
        callbacks: {
            beforeOpen: function() {
                // Load data before popup open load first time
                getDataPopupMovieSchedule(this.st.el);
            },
            close: function() {
            }
        }
    });


    $("#modal-movie-showtimes").on('click', '.day-showing-item', function() {
        getDataPopupMovieSchedule(this);
    })

    // Call server get data movie showtime
    
    function getDataPopupMovieSchedule(element) {
        var id_server = $('.list-cinema .active').attr('data-id-server');


        if ($(element).attr("movie-day-selected")) {
            var date_query = $(element).attr("movie-day-selected");
            // Active Date Selected on List Schedule
            $('#modal-movie-showtimes .days-movie-showing [movie-day-selected = ' + date_query + ']').addClass('active-date');

        } else {
            var date_query = new Date().toJSON().slice(0, 10).replace(/-/g, '-');
            // Active First Day in List Schedules
            $('#modal-movie-showtimes .days-movie-showing li:first').addClass('active-date');
        }

        // Call Ajax get movie show time with current date
        // cinema_id is equal id_server
        data = {
            "date": date_query,
            "cinema_id": id_server
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
            console.log("document.domain ",document.domain);
            $.each(response, function(key, value) {
                if (value.lst_times.length > 0) {
                     // Ignore movie Test to server production
                    if (document.domain == "metiz.vn" && movieIdTest == value.movie_id ) {
                        return;
                    }
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
        // Show popup warning or confirm
        function showPopup(element){
            // get movie information when click showtime then append info to list fields hidden using store post to server process
            var id_showtime = element.children('input[name=id_showtime]').val();
            var id_movie_name = element.children('input[name=id_movie_name]').val();
            var movie_api_id = element.children('input[name=movie_api_id]').val();
            var id_movie_time = element.children('span[class=time]').text();
            

            $('.modal-schedule input[name=id_server]').val(id_server);
            $('.modal-schedule input[name=id_showtime]').val(id_showtime);
            $('.modal-schedule input[name=movie_api_id]').val(movie_api_id);
            $('.modal-schedule input[name=id_movie_name]').val(id_movie_name);
            $('.modal-schedule input[name=id_movie_time]').val(id_movie_time);
            $('.modal-schedule input[name=id_movie_date_active]').val($("li.active-date").attr("movie-day-selected"));

            //set content for modal #warnning or skip
            var rated = element.parents('.lot-table').attr('data-rated');
            $('#confirm-user-information').on('show.bs.modal', function() {
                $('#confirm-user-information').css("overflow-y","auto");
                // remove tabindex of magnifix popup trigger for input confirm form
                $(".mfp-ready").removeAttr("tabindex");
                $(".mfp-ready").css("overflow-y","hidden");
                if (navigator.userAgent.match(/iPhone|iPod|iPad|Android|Windows Phone|BlackBerry/i)) {

                    // add attr autocomplete for every input
                    // *** BUG *** : show suggest when focus input, suggest moving when scroll
                    $('#confirm-user-information input').attr('autocomplete', 'off');

                    // set scroll to tocuh
                    $("#confirm-user-information").css("-webkit-overflow-scrolling", "touch !important");
                }
            });

            // Set attr style when hide modal confirm
            $('#confirm-user-information').on('hide.bs.modal', function() {
                $(".mfp-ready").attr("style","overflow-x: hidden; overflow-y: auto;");
            });
            // Show popup warning or confirm
            if (rated == 'null' || rated == 'p'|| rated == 'P') {
                $('#confirm-user-information').modal('show');
            } else {
                content = JSON.parse($('#rated').text());
                $('#warning #content-warnning').text(content[rated]);
                $('#warning').modal('show');
            }
        }
        // TH2: Click đặt vé a movie
        /* change background for schedule firm on mobile */
        if (navigator.userAgent.match(/iPhone|iPod|iPad|Android|Windows Phone|BlackBerry/i)) {
            $('.sold-out a').on('click', function(event) {
                // *** Allow booking ***
                var allow_booking = $(this).children('input[name=allow_booking]').val();
                if (allow_booking == 'false') {
                    $('#alert_allow_booking').modal('show');
                    return;
                }
                // *** End Allow booking ***
                $(this).addClass('mobile-schedule');
                if(validate_time_remain($(this))){
                    showPopup($(this));
                }
            });
            $('.modal-schedule').on('hide.bs.modal', function() {
                $('.sold-out a').removeClass('mobile-schedule');

            });
        }else{
            // on web
            $('.sold-out a').click(function(event) {
                event.preventDefault();
                // *** Allow booking ***
                var allow_booking = $(this).children('input[name=allow_booking]').val();
                if (allow_booking == 'false') {
                    $('#alert_allow_booking').modal('show');
                    return;
                }
                // *** End Allow booking ***
                if(validate_time_remain($(this))){
                    showPopup($(this));
                }
            });
        }
    }

});