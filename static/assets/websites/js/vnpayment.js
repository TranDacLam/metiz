$(document).ready(function() {

    $("#btnPopup").click(function (event) {
        // event.preventDefault();
        // var postData = JSON.stringify($("#create_form").serializeArray());
        var postData = $("#create_form").serialize();
        console.log("postData ",postData);
        var submitUrl = $("#create_form").attr("action");
        $.ajax({
            type: "POST",
            url: submitUrl,
            data: postData,
            dataType: "JSON",
            success: function (x) {
                console.log("success ",x);
                if (x.code === '00') {
                    if (window.vnpay) {
                        vnpay.open({width: 768, height: 600, url: x.data});
                    }
                    else {
                        location.href = x.data;
                    }
                    return false;
                } else {
                    alert(x.Message);
                }
            },
            crossDomain: false
        });
        return false;
    });

    // validate form
    var val_required = 'Trường này là bắt buộc';
    $("#create_form").validate({
        rules: {
            amount: { 
                number: true,
                required: true,
            },
            bank_code: { 
                required: true,
            },
            order_id: {
                required: true,
            }
        },
        messages:{
            amount: {
                number: 'Vui lòng chỉ nhập số',
                required: val_required,
            },
            bank_code: {
                required: val_required,
            },
            order_id: {
                required: val_required,
            }
        }
    });
});