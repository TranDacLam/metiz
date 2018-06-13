
function trigger_warning_rated(element)
{
     // Get content warning 
    var rated = element.parents('.lot-table').attr('data-rated');
    if (rated == 'null' || rated == 'p'|| rated == 'P') {
        // Skip modal warning
        $('#confirm-user-information').modal('show');
    } else {
        // Show modal warning
        content_warning = JSON.parse($('#content_warning').text());
        $('#warning #content-warnning').text(content_warning[rated]);
        $('#warning').modal('show');
    }
}

function show_popup_user_information(element){
    // get movie information when click showtime then append info to list fields hidden using store post to server process
    var id_showtime = element.children('input[name=id_showtime]').val();
    var id_movie_name = element.children('input[name=id_movie_name]').val();
    var movie_api_id = element.children('input[name=movie_api_id]').val();
    var id_movie_time = element.children('span[class=time]').text();
    var id_server = $('#data-id-server').val();

    $('.modal-schedule input[name=id_server]').val(id_server);
    $('.modal-schedule input[name=id_showtime]').val(id_showtime);
    $('.modal-schedule input[name=movie_api_id]').val(movie_api_id);
    $('.modal-schedule input[name=id_movie_name]').val(id_movie_name);
    $('.modal-schedule input[name=id_movie_time]').val(id_movie_time);
    $('.modal-schedule input[name=id_movie_date_active]').val($("li.active-date").attr("movie-day-selected"));

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

    // Check movie rated before show user information
    trigger_warning_rated(element);
}