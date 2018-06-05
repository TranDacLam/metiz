$(document).ready(function() {
    // *** MOVIE SCHEDULE ***
    // inherit getDataPopupMovieSchedule function in model.js
    // Get list movie, show time
    // - TH1: Click show schedule (on header)
    // --- auto click first day
    // - TH2: Click day ( on date show )
    // --- chang month, addClass active-date

    // - TH2: Click day ( on date show )
    $(document).on('click', '#schedule-film .popup-movie-schedule', function() {
        getDataMovieSchedule(this);
    })

    // Call server get data
    function getDataMovieSchedule(element) {

        //set data for Month
        $('#schedule-film #center-month').text($(element).children('.hide-month').text());
        $('#schedule-film .days-popup li').removeClass('active-date');

        var id_server = $('#schedule-film .list-cinema .active').attr('data-id-server');
        $(element).addClass('active-date');
    }
    // TH1: Click show time (on header)
    $('#schedule-film .days-popup li:first').click();
        
    //dont allow key e in input phone
    $("#schedule-film input[type=number]").on("keydown", function(e) {
        return e.keyCode == 69 ? false : true;
    });
});