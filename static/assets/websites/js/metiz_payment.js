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
                required: 'Card barcode không được để trống.'
            }
        }
    });
});