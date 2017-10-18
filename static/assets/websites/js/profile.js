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
    $("#change-pass-validate").validate({
        rules: {
            password1: { 
                minlength: 8,
                maxlength: 16,
                required: true,
            }, 
            password2: { 
                minlength: 8,
                maxlength: 16,
                required: true,
            }, 
             password3: { 
                equalTo: '[name="new_password1"]'
               }
        },
        messages:{
            password1: {
                required: 'Mật khẩu không được để trống.',
                minlength: 'Mật khẩu ít nhất 8 ký tự.',
                maxlength: 'Mật khẩu không quá 16 ký tự.'
            },
            password2: {
                required: 'Mật khẩu không được để trống.',
                minlength: 'Mật khẩu ít nhất 8 ký tự.',
                maxlength: 'Mật khẩu không quá 16 ký tự.'
            },
            password3: { 
                equalTo:"Hai trường mật khẩu không giống nhau.",
                required: 'Xác nhận mật khẩu không được để trống.',
            }
        }
    });
});