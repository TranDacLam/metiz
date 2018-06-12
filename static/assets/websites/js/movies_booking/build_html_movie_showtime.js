// *** POPUP MOVIE SCHEDULE ***
// Get list movie, show time
// * Step 1:
// - TH1: Click Lịch chiếu (header) or Đổi xuất chiếu (page Booking)
// --- Set movie_api_id = null -> let get list movie
// - TH2: Click đặt vé a movie
// --- get movie_api_id movie selected -> let get a movie selected
// * Step 2:
// - TH1: Click Lịch chiếu (header)
// --- get date_query = date current
// - TH2: Click Đổi xuất chiếu (page Booking)
// --- get data-date-seat, get date schedule user selected
// --- Show popup movie schedule date selected
// - TH3: Click đặt vé a movie
// --- get movie-api-id movie selected
// * Step 3:
// - function listShedule: list show time of 1 movie
// - function listFilm: list movie of date selected

// list show time of a movie, callback from function listFilm
function listShedule(shedule) {
    var htmlShedule = '';
    $.each(shedule.lst_times, function(key, value) {

        //set end time for film schedule
        // TODO : USING TimeDelta jquery
        var startTime = value.time.split(':').map(Number);
        console.log("startTime ",value);
        var minute = (shedule.time_running + startTime[1]) % 60;
        var hour = startTime[0] + Math.floor((shedule.time_running + startTime[1]) / 60);
        if (minute < 10) {
            minute = '0' + minute;
        }
        if (hour > 23) {
            hour -= 24;
        }
        var endTime = '-' + hour + ':' + minute;
        htmlShedule += '<li class="sold-out">' +
            '<a href="javascript:void(0);" >' +
            '<input type="hidden" name="id_showtime" value="' + value.id_showtime + '">' +
            '<input type="hidden" name="id_movie_id" value="' + shedule.movie_id + '">' +
            '<input type="hidden" name="id_movie_name" value="' + shedule.movie_name + '">' +
            '<input type="hidden" name="movie_api_id" value="' + shedule.movie_id + '">' +
            '<input type="hidden" name="allow_booking" value="' + shedule.allow_booking + '">' +
            '<span class="time">' + value.time + endTime +'</span>' +
            '<span class="ppnum">Phòng chiếu</span>' +
            '<span class="ppnum">' + value.room_name + '</span>' + // room chiếu phim
            '</a>' +
            '</li>';

    });
    return htmlShedule;
}

// list movie 
function render_schedule_html(film) {

    return '<div class="movie-time-line-box clearfix" data-control="movie-code">' +
        '<h3 class="movie-name">' + film.movie_name + '</h3>' +
        '<div class="lot-table clearfix" data-rated="' + film.rated + '" >' +
        '<ul class="list-inline list-unstyled theater_time">' +
        listShedule(film) +
        '</ul>' +
        ' </div>' +
        ' </div>';
}