$(document).ready(function() {
    // active menu profile
    $('#info-member-card').addClass('active');

    setBarcode();

    function setBarcode(){
        var settings = {
            output: 'css',
            bgColor: '#FFFFFF',
            color: '#000000',
            barWidth: '1',
            barHeight: '50'
        };
        var type = 'code128';
        var barcode = $('input[name=barcode_member_card]').val();

        $('#barcode-member-card').barcode(
            barcode, // Value barcode (dependent on the type of barcode)
            type, // type (string)
            settings
        );
    }

    $.ajax({
        url: '/api/gift/claiming_points/',
        type: 'GET',
        dataType: 'json',
        crossDomain:false,
        context: this,
    })
    .done(function(response) {
        console.log("claiming_points", response);
        
    })
    .fail(function(error) {
        console.log(error);
    })

    $('#btn-link-card').click(function(){
        $(this).prop('disabled', true);
        var card_member = $("#form-member-card input[name=card_member]").val();

        $.ajax({
            url: '/api/card_member/link/',
            type: 'POST',
            data: {"card_member": card_member},
            dataType: 'json',
            crossDomain:false,
            context: this,
        })
        .done(function(response) {
            console.log(response);
            $(this).prop('disabled', false);
            location.reload();
        })
        .fail(function(error) {
            $(this).prop('disabled', false);
            console.log(error);
            displayMsg();
            if(error.status == 400){
                $('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
            }else{
                $('.msg-result-js').html(msgResult("Error link card", "danger"));
            }
        })
    });

});