$(document).ready(function() {
    //Handle press esc
    $("body").on("keyup", function(e) {
        var key = e.which;
        if (key == 27) {
            e.preventDefault();
            // Close modal first
            if ($('.modal').hasClass('in')) {
                $('.modal').modal('hide');
            } else {
                // Close schedule
                $.magnificPopup.close();
            }
        }
    });

    // Trigger event when user click showtime movie schedule (lich chieu)
    $('.open-movie-showtime').magnificPopup({
        type: 'inline',
        midClick: true,
        enableEscapeKey: false,
        fixedContentPos: true,
        callbacks: {
            beforeOpen: function() {
                // set movie api id for input
                $('#data_movie_api_id').val($(this.st.el).attr("data-movie-api-id"));
                // Load data before popup open load first time
                getDataPopupMovieSchedule(this.st.el);
            },
            close: function() {
                // clear movie_api_id
                $('#data_movie_api_id').val('');
                $('.days-movie-showing li').removeClass('active-date');
            }
        }
    });

    // Handle when click each day
    $("#modal-movie-showtimes").on('click', '.day-showing-item', function() {
        // Remove Active Date Befor add new active 
        $('.days-movie-showing li').removeClass('active-date');

        getDataPopupMovieSchedule(this);
    })   

});