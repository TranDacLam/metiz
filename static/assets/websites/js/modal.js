$(document).ready(function() {
    // active popup
    $('.open-popup-link').magnificPopup({
          type: 'inline',
          midClick: true,
    });

    startMonth();

    function listShedule(shedule){
        var htmlShedule = '';
        $.each(shedule.lst_times, function(key, value) {
            htmlShedule +=  '<li class="sold-out">'
                                +'<a href="#" data-toggle="modal" data-target="#warning">'
                                    +'<input type="hidden" name="id_showtime" value="'+ value.id_showtime +'">'
                                    +'<span class="time">'+ value.time +'</span>'
                                    +'<span class="clock">'+ value.time +'<span>~1:15</span></span>'
                                    +'<span class="ppnum">43</span>' // Số ghế trống
                                    +'<span class="ppnum">Room 2</span>' // room chiếu phim
                                    +'<span class="pp-early" title="Suất chiều đầu"></span>'
                                +'</a>'
                            +'</li>';
        });
        return htmlShedule;
    }

    function listFilm(film){
        return  '<div class="movie-time-line-box clearfix" data-control="movie-code">'
                    +'<h3 class="movie-name">'+ film.movie_name +'</h3>'
                    +'<div class="lot-table clearfix">'
                        +'<ul class="list-inline list-unstyled theater_time">'
                            + listShedule(film)
                        +'</ul>'
                   +' </div>'
               +' </div>';
    }

    $(document).on('click', '.popup-movie-schedule', function () { 
        $('.days-popup li').removeClass('active-date');
        if($(this).attr("data-date-seat")){
            var date_seat = $(this).attr("data-date-seat");
            $('.days-popup [data-date-select = '+ date_seat +']').addClass('active-date');
            var date_query = date_seat;
        }else{
            if($(this).attr("data-date-select")){
                var date_query = $(this).attr("data-date-select");
                $(this).addClass('active-date');
            }else{
                var date_query = new Date().toJSON().slice(0,10).replace(/-/g,'-');
                $('.days-popup li:first').addClass('active-date');
            }
        }
        
        // Call Ajax get movie show time with current date
        data = {
            "date": date_query,
            "cinema_id": 1 // get cinema_id from hidden field in popup movie schedule
        }
        $.ajax({
            url: "/movie/show/times",
            type: 'get',
            data: data,
            dataType: 'json',
            crossDomain:false,
            context: this,
        })
        .done(function(response) {
            var html = '';
            $.each(response, function(key, value) {
                html += listFilm(value);
            });
            $('.list-schedule').html(html);
        })
        .fail(function() {
            alert("error schedule film");
        });
    });
});

function startMonth(){
    // $(".badge:contains('1')").parent().addClass('start-month');
    $('.days-popup li span').each(function() {
        if ($(this).text() == 1) {
            $(this).parent().addClass('start-month');
        }
    });
}