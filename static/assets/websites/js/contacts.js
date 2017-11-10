$(document).ready(function() {
    $("#contactForm").validate({
        rules: {
            name: { 
                required: true,
            },
            email:{
                required: true,
            },
            telephone:{
                required: true,
            },
            subject:{
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
            telephone: {
                required: "Vui lòng nhập số điện thoại",
            },
            subject:{
                required: "Vui lòng nhập chủ đề",
            },
        }
    });
});