$(document).ready(function() {
    $('#btn-sync').on('click', function(e){
        e.preventDefault();
        $.ajax({
            url: '/movies/synchronize/',
            type: 'POST',
            crossDomain:false,
        })
        .done(function(response) {
           $('.msg-result-js').html(msgResult("Successfully", "success"));
        })
        .fail(function() {
            displayMsg();
            $('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
        });
    });
});