$(document).ready(function(){

    $(".btn-get-movie-api-id").on('click', function(){

        $.ajax({
            url: '/movie/api/ids/',
            type: 'post',
            dataType: 'json',
            data: {
                'request_date': $("#input-request-date").val()
            },
            crossDomain:false,
            context: this,
        })
        .done(function(response) {
            //set error valdiate

            html = '';
            $('.table-display-movie-api').css('opacity', 1)
            $.each(response.lst_movie_api, function(key, value) {
                html += '<tr>'+
                            '<td>'+value+'</td>'+
                            '<td>'+key+'</td>'+
                        '</tr>';
                // do something with `item` (or `this` is also `item` if you like)
            });
            $("#body-display-movies").html(html)
        })
        .fail(function() {
            alert("error");
        });
    
    });

    // get date yyyy-mm-dd
    var date_now = new Date();
    var date_day = ("0" + date_now.getDate()).slice(-2);
    var date_month = ("0" + (date_now.getMonth() + 1)).slice(-2);
    var date_today = date_now.getFullYear() + "-" + (date_month) + "-" + (date_day);

    // datebox js
    $('#input-request-date').datebox({
        mode: "calbox",
        overrideDateFormat: '%Y-%m-%d',
        useFocus: true,
        useButton: false,
        useHeader: false,
        calShowDays: false,
        calUsePickers: true,
        calHighToday:true,
        themeDatePick: 'warning',
        defaultValue: date_today,
        calYearPickMax: 'NOW',
        calYearPickMin: 100,
    });
    
});