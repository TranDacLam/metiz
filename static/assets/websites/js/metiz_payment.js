$(document).ready(function() {

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
        }
    });

    // format money
    var money_total = $('#total').text();
    $('#total').text(money_total.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1."));
});