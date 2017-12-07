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
                rangelength: [1, 70],
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
                rangelength: "Họ và tên chứa ít nhất 1 kí tự và nhiều nhất 70 kí tự",
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
    // Validate phone number
    // Can enter 0 number at the end or middle but not at the beginning.
    // Check the first characters and remove if it equal == 0
    // Then replace input with new value
    // Use profile
    
    //Prevent to enter 0(zero) number at the second character
    $('.textPhone').on('keydown',function(event){
        var caretPos = this.selectionStart;
        var keyCode = event.which || event.keyCode;
        var isZero = keyCode == 48 || keyCode == 96;
        var valPhone = $(this).val();
        if (caretPos < 2 && valPhone.startsWith("0") && isZero) {
            return false;
        } 
    });
    // Call event Paste 
     $('.textPhone').bind('paste', function(e) {
        var pasteText = e.originalEvent.clipboardData.getData('Text');
        $(this).val(removeBeforePhoneNumber(pasteText)); 
        return false;
    });
    $('.textPhone').on('blur',function(event){ 
        var valPhone = $(this).val();
        $(this).val(removeBeforePhoneNumber(valPhone));
    });
});