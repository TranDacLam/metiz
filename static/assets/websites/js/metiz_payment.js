$(document).ready(function() {

    // set defaut number_verify, disable re-sendOtp next page
    sessionStorage.setItem('number_verify', 1);

    // validate phone, persional only number
    var selectorCardBarcode = $("#metiz_payment_form input[name=card_barcode]");

    // Call back validOnlyNumber layout.js 
    validOnlyNumber(selectorCardBarcode, selectorCardBarcode.val());

    $("#metiz_payment_form").validate({
        rules: {
            card_barcode: { 
                required: true
            }
        },
        messages:{
            card_barcode: {
                required: 'Mã thẻ không được để trống.'
            }
        },
        submitHandler: function(form) {
            $('#btn-payment-continute').button('loading');
            form.submit();
        }
    });

    // display error card_barcode when keyup, Bug: server rsp error, input value, 2 times click submit form.
    $('#metiz_payment_form input').keyup(function(){
        $(this).attr('aria-invalid', false);
        $('#card_barcode-error').attr('style', 'display: none;');
    });

    // format money
    var money_total = $('#total').text();
    $('#total').text(money_total.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1."));

});