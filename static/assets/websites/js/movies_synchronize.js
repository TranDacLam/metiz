$(document).ready(function() {
    $('#btn-sync').on('click', function(e){
        e.preventDefault();
        $.ajax({
            url: '/movies/synchronize/',
            type: 'POST',
            crossDomain:false,
        })
        .done(function(response) {
            $('#msg-sync').show();
            setTimeout(function(){ 
                
                $('#msg-sync').hide();

        }, 6000);
           
           $('.msg-result-js').html(msgResult("Successfully", "success"));
        })
        .fail(function() {
            displayMsg();
            $('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
            $('#msg-sync-error').show();
                setTimeout(function(){ 
                    
                    $('#msg-sync-error').hide();

            }, 6000);
        });
    });
});