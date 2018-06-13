$(document).ready(function() {
    //dont allow key e in input phone
    $("#modal-movie-showtimes input[type=number]").on("keydown", function(e) {
        return e.keyCode == 69 ? false : true;
    });

    $('#modal-movie-showtimes').removeClass("mfp-hide");
    // getDataPopupMovieSchedule();
    $('.white-popup .calendar-popup li:first').click();
   	// disable show schedule film
	$('.open-movie-showtime').magnificPopup({
        disableOn: function() {
			return false;
		}
    });
    // prevent href a
    $('.open-movie-showtime').click(function(event) {
    	return false;
    });
});