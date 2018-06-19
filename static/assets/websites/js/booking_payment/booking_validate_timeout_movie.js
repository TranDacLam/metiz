function bookingValidateTimeOutMovie(){
    var id_movie_time = $('.time-movie-booking').text().replace('~', '-');
    var id_movie_date_active = $('.date-movie-booking').text();

    // calculated current movie showtime is expired (less than to current datetime)
    var movie_start_time = id_movie_time.split("-")[0].split(":");
    // Convert date and startTime to Jquery DateTime, funtion convertStringToDate from layout.js
    var date_time_movie_start = convertStringToDate(id_movie_date_active, movie_start_time);

    if(new Date() >= date_time_movie_start)
    {
        return true;
    }
    return false;
}