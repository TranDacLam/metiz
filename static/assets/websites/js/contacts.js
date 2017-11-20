$(document).ready(function() {
    $("#contactForm").validate({
        rules: {
            name: { 
                required: true,
            },
            email:{
                required: true,
            },
            phone:{
                required: true,
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
            },
            phone: {
                required: "Vui lòng nhập số điện thoại",
            },
            message: {
                required: "Vui lòng nhập nội dung",
            }
        }
    });
});