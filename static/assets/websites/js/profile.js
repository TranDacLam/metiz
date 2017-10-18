$(document).ready(function() {
    var val_required = 'Trường này là bắt buộc';

    // page profile
    $("#profile-validate").validate({
        rules: {
            username: { 
                required: true,
            },
            birth_date: { 
                required: true,
            },
            phone: {
                required: true,
            },
            email:{
                required: true,
            },
        },
        messages:{
            username: {
                required: val_required,
            },
            birth_date: {
                required: val_required,
            },
            phone: {
                required: val_required,
            },
            email: {
                required: val_required,
            }    
        }
    });

    // page change password
    $.validator.addMethod(
        "regex",
         function(value, element) {
            return this.optional(element) || (value.match(/[a-z]/) && value.match(/[!@#$%^&*()_+A-Z]/) && value.match(/[0-9]/));
        },
        "Mật khẩu có ít nhất một số, một ký tự thường và một ký tự hoa (hoặc ký tự đặc biệt)"
    );

    $("#change-pass-validate").validate({
        rules: {
            password1: { 
                minlength: 8,
                required: true,
            }, 
            password2: { 
                minlength: 8,
                required: true,
                regex: true,
            }, 
             password3: { 
                equalTo: '[name="password2"]'
               }
        },
        messages:{
            password1: {
                required: 'Mật khẩu không được để trống.',
                minlength: 'Mật khẩu ít nhất 8 ký tự.',
            },
            password2: {
                required: 'Mật khẩu không được để trống.',
                minlength: 'Mật khẩu ít nhất 8 ký tự.',
            },
            password3: { 
                equalTo:"Hai trường mật khẩu không giống nhau.",
                required: 'Xác nhận mật khẩu không được để trống.',
            }
        }
    });
});