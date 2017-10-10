$(document).ready(function() {
    $("#form-validate").validate({
        rules: {
            new_password1: { 
                minlength: 8,
                maxlength: 16,

            }, 
             new_password2: { 
                equalTo: '[name="new_password1"]'
               }
        },
        messages:{
            new_password1: {
                required: 'Mật khẩu không được để trống.',
                minlength: 'Mật khẩu ít nhất 8 ký tự.',
                maxlength: 'Mật khẩu không quá 16 ký tự.'
            },
            new_password2: { 
                equalTo:"Hai trường mật khẩu không giống nhau.",
                required: 'Xác nhận mật khẩu không được để trống.',
            }
        }
    });
});