$(document).ready(function() {
    //dont allow key e in input phone
    $("#modal-movie-showtimes input[type=number]").on("keydown", function(e) {
        return e.keyCode == 69 ? false : true;
    });

    $('#modal-movie-showtimes').removeClass("mfp-hide");
    // getDataPopupMovieSchedule();
    $('#modal-movie-showtimes .days-popup li:first').click();
});