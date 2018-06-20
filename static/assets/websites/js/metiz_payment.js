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

    // format money
    var money_total = $('#total').text();
    $('#total').text(money_total.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1."));

});