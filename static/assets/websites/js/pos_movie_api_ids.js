$(document).ready(function(){

    $(".btn-get-movie-api-id").on('click', function(){
        var input = $('#input-request-date').val();
        if (input != '' && input.match(/^([0-9]{4}[-]?((0[13-9]|1[012])[-]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-]?31|02[-]?(0[1-9]|1[0-9]|2[0-8]))|([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00)[-]?02[-]?29)$/) == null) {
            // show validate
            $('.error_date').html('Vui lòng nhập định dạng ngày yyyy-mm-dd')
            $("#body-display-movies").html('')
            return;
        }

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
            $('.error_date').html('');

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
    
});