$(document).ready(function() {
    $('#btn-reSend-otp').prop('disabled', true);
    $('#btn-reSend-otp').click(function(e){
        console.log("CLICK ReSend", );
        
        e.preventDefault();
        
        var working_id = $("#working_id").val();
        
        $.ajax({
            url: '/payment/otp/resend/',
            type: 'POST',
            data: {"working_id": working_id},
            dataType: 'json',
            crossDomain:false,
            context: this,
        })
        .done(function(response) {
            $('#btn-reSend-otp').prop('disabled', true);
            
        })
        .fail(function(response) {

            console.log("response ",response);
            console.log("response ",response.responseJSON.message);
            if(response.responseJSON.code == 403){
                window.location.href = '/timeout/booking/';
            }
            $('#btn-reSend-otp').prop('disabled', false);
        })
    });

})