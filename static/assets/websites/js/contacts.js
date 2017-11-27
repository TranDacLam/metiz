$(document).ready(function() {
    // validate phone only number
    var selectorPhone = $("#contactForm input[name=phone]");
    // Call back validOnlyNumber layout.js 
    validOnlyNumber(selectorPhone, '');

    $("#contactForm").validate({
        rules: {
            name: { 
                required: true,
            },
            email:{
                required: true,
                email: true
            },
            phone:{
                required: true,
                rangelength:[10, 12],
                number: true
            },
            message:{
                required: true,
            }
        },
        messages:{
            name: {
                required: "Vui lòng nhập tên",
            },
            email: {
                required: "Vui lòng nhập email",
                email: "Email không hợp lệ"
            },
            phone: {
                required: "Vui lòng nhập số điện thoại",
                rangelength: "Số điện thoại không hợp lệ",
                number: "Vui lòng chỉ nhập chữ số"
            },
            message: {
                required: "Vui lòng nhập nội dung",
            }
        }
    });
});