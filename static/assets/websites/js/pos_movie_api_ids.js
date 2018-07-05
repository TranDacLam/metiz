$(document).ready(function(){
    $(".btn-get-movie-api-id").on('click', function(){
        console.log("CLICK BUTTOMN ");
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
            console.log("#response ",response);
            $.each(response.lst_movie_api, function(key, value) {
                $("#body-display-movies").append('<tr>'+
                                                    '<td>'+value+'</td>'+
                                                    '<td>'+key+'</td>'+
                                                '</tr>');
                // do something with `item` (or `this` is also `item` if you like)
            });
        })
        .fail(function() {
            alert("error");
        });
    
    });
    
});