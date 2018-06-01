$(document).ready(function() {

    // active menu profile
    $('#change-password').addClass('active');

    var valid_pass = "Mật khẩu chứa ít nhất 8 ký tự, bao gồm chữ, số và ký tự hoa hoặc ký tự đặc biệt.";

    // page change password
    $.validator.addMethod(
        "regex",
         function(value, element) {
            return this.optional(element) || (value.match(/[a-z]/) && value.match(/[!@#$%^&*()_+A-Z]/) && value.match(/[0-9]/));
        },
        valid_pass
    );

    $("#change-pass-validate").validate({
        rules: {
            old_password: { 
                minlength: 8,
                required: true,
                regex: true,
            }, 
            new_password: { 
                minlength: 8,
                required: true,
                regex: true,
            }, 
             new_password2: { 
                equalTo: '[name="new_password"]',
                required: true,
               }
        },
        messages:{
            old_password: {
                required: 'Mật khẩu không được để trống.',
                minlength: valid_pass,
            },
            new_password: {
                required: 'Mật khẩu mới không được để trống.',
                minlength: valid_pass,
            },
            new_password2: { 
                equalTo:"Hai trường mật khẩu không giống nhau.",
                required: 'Nhập lại mật khẩu mới không được để trống.',
            }
        }
    });
});