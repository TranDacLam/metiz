$(document).ready(function() {

    function checkOtpReSend(){
        if(sessionStorage.getItem('number_verify')){
            // get number_verify from sessionStorage
            var number_verify = parseInt(sessionStorage.getItem('number_verify'));
            // if number_verify > 3 then undisabled else disabled button reSend otp
            if(number_verify > 3){
                $('#btn-reSend-otp').prop('disabled', false);
            }else{
                $('#btn-reSend-otp').prop('disabled', true);
            }
        }else{
            // set number_verify = 1, disable button reSend otp
            sessionStorage.setItem('number_verify', 1);
            $('#btn-reSend-otp').prop('disabled', true);
        }
    }

    checkOtpReSend();

    // Event click, + 1 number_verify
    $('#btn-payment-continute').click(function(e){
        var number_verify_event = parseInt(sessionStorage.getItem('number_verify'));
        number_verify_event += 1;
        sessionStorage.setItem('number_verify', number_verify_event);
    });

    $('#btn-reSend-otp').click(function(e){
        e.preventDefault();

        // set number_verify = 1, disable button reSend otp
        sessionStorage.setItem('number_verify', 1);
        
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
            number_verify = 0;
            
        })
        .fail(function(response) {
            if(response.responseJSON.code == 403){
                window.location.href = '/timeout/booking/';
            }
            $('#btn-reSend-otp').prop('disabled', false);
        })
    });

    // format money
    var money_total = $('#metiz_payment_verify_otp_form .payment_amount').text();
    $('#metiz_payment_verify_otp_form .payment_amount').text(money_total.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1."));

})