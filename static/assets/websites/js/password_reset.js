$(document).ready(function() {
    $.validator.addMethod(
        "regex",
         function(value, element) {
            return this.optional(element) || (value.match(/[a-z]/) && value.match(/[!@#$%^&*()_+A-Z]/) && value.match(/[0-9]/));
        },
        "Mật khẩu có ít nhất một số, một ký tự thường và một ký tự hoa (hoặc ký tự đặc biệt)"
    );

    $("#form-validate").validate({
        rules: {
            new_password1: { 
                minlength: 8,
                required: true,
                regex: true,
            }, 
             new_password2: { 
                equalTo: '[name="new_password1"]',
                required: true,
               }
        },
        messages:{
            new_password1: {
                required: 'Mật khẩu không được để trống.',
                minlength: 'Mật khẩu ít nhất 8 ký tự.',
            },
            new_password2: { 
                equalTo:"Hai trường mật khẩu không giống nhau.",
                required: 'Xác nhận mật khẩu không được để trống.',
            }
        }
    });
});