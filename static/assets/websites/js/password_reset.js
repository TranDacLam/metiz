$(document).ready(function() {
    var valid_pass = "Mật khẩu chứa ít nhất 8 ký tự, bao gồm chữ, số và ký tự hoa hoặc ký tự đặc biệt";
    $.validator.addMethod(
        "regex",
         function(value, element) {
            return this.optional(element) || (value.match(/[a-z]/) && value.match(/[!@#$%^&*()_+A-Z]/) && value.match(/[0-9]/));
        },
        valid_pass
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
                minlength: valid_pass,
            },
            new_password2: { 
                equalTo:"Hai trường mật khẩu không giống nhau.",
                required: 'Xác nhận mật khẩu không được để trống.',
            }
        }
    });
});