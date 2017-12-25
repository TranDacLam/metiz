$(document).ready(function() {
    $(".resend-activation").validate({
        rules: {
            email: {
                required:true,
                email:true,
            },
        },
        messages:{
            email: {
                required: "Email không được để trống",
                email: "Email không hợp lệ",
            }
        }
    });
});