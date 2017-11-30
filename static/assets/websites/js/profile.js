$(document).ready(function() {
    var val_required = 'Trường này là bắt buộc';
    var val_date = 'Nhập ngày theo định dạng dd-mm-yyyy';
    var valid_pass = "Mật khẩu chứa ít nhất 8 ký tự, bao gồm chữ, số và ký tự hoa hoặc ký tự đặc biệt.";

    // validate phone, persional only number
    var selectorPhone = $("#profile-validate input[name=phone]");
    var selectorPersonal = $("#profile-validate input[name=personal_id]");
    // Call back validOnlyNumber layout.js 
    validOnlyNumber(selectorPhone, selectorPhone.val());
    validOnlyNumber(selectorPersonal, selectorPersonal.val());

    // page profile
    $("#profile-validate").validate({
        rules: {
            full_name: { 
                required: true,
            },
            birth_date: { 
                required: true,
                validateDate: true,
            },
            phone: {
                required: true,
                number: true,
                minlength: 9,
                validatePhone: true,
            },
            email:{
                required: true,
            },
            personal_id: {
                number: true,
                rangelength:[9, 9],
            }
        },
        messages:{
            full_name: {
                required: val_required,
            },
            birth_date: {
                required: val_required,
                validateDate: val_date,
            },
            phone: {
                required: val_required,
                number: 'Vui lòng chỉ nhập số',
                minlength: "Số điện thoại không hợp lệ",
                validatePhone: "Số điện thoại không hợp lệ",
            },
            email: {
                required: val_required,
            },
            personal_id: {
                number: 'Vui lòng chỉ nhập số',
                rangelength: 'Vui lòng nhập CMND gồm 9 chữ số'
            }  
        }
    });
    // format birthday
    $.validator.addMethod(
      "validateDate",
      function (value, element) {
        // put your own logic here, this is just a (crappy) example 
        return value.match(/^\d\d?\-\d\d?\-\d\d\d\d$/);
      },
      message.validateDate
    );

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