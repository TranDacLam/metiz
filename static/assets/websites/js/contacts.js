$(document).ready(function() {
    // validate phone, persional only number
    $('#contactForm input[name=phone]').keyup(function(e) {
        if (/\D/g.test(this.value)) {
            // Filter non-digits from input value.
            this.value = this.value.replace(/\D/g, '');
        }
    });

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