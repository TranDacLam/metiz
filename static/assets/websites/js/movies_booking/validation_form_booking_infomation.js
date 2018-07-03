// Can enter 0 number at the end or middle but not at the beginning.
// Check the first characters and remove if it equal == 0
// Then replace input with new value
// use modal, profile, register

//Prevent to enter 0(zero) number at the second character
$(document).ready(function() {
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

    // validate phone only number
    // Form Guest modal schedule
    var selectorPhone_guest_form = $("#guest_form input[name=phone]");
    // Call back validOnlyNumber layout.js 
    validOnlyNumber(selectorPhone_guest_form, selectorPhone_guest_form.val());

    //checkbox for form guest
    $('#agree_term').on('click', function() {
        if ($('#agree_term').prop("checked")) {
            $('#confirm-user-information .form-popup #submit_guest_form').prop('disabled', false);
        } else {
            $('#confirm-user-information .form-popup #submit_guest_form').prop('disabled', true);
        }
    });

    //dont allow key e in input phone
    $("#modal-movie-showtimes input[type=number]").on("keydown", function(e) {
        return e.keyCode == 69 ? false : true;
    });


    // Register validation for phone number
    $.validator.addMethod(
        "validatePhone",
        function(value, element) {
            // put your own logic here, this is just a (crappy) example 
            return value.match(/^(01[2689]|09|[0-9]|[0-9]{2})[0-9]{8}$/);
        },
        message_translate.phone
    );

    // validate password
    $.validator.addMethod(
        "regex",
        function(value, element) {
            return this.optional(element) || (value.match(/[a-z]/) && value.match(/[!@#$%^&*()_+A-Z]/) && value.match(/[0-9]/));
        },
        message_translate.validatePassword
    );


    //validate guest form, confirm user information booking form
    $("#guest_form").validate({
        rules: {
            name: {
                required: true,
                rangelength: [1, 70],
            },
            email: {
                email:{
                    depends:function(){
                        $(this).val($.trim($(this).val()));
                        return true;
                    }
                },
            },
            phone: {
                required: true,
                validatePhone: true,
                number: true,
                minlength: 9,
            },
        },
        messages: {
            name: {
                required: message_translate.required,
                rangelength: message_translate.rangelength_1_70,
            },
            email: {
                email: message_translate.email
            },
            phone: {
                required: message_translate.required,
                validatePhone: message_translate.phone,
                number: message_translate.number,
                minlength: message_translate.phone,
            }
        },
        // append input has info film to form then submit
        submitHandler: function(form) {
            // event.preventDefault();
            $('.modal-schedule input[name=id_server]').appendTo(form);
            $('.modal-schedule input[name=id_showtime]').appendTo(form);
            $('.modal-schedule input[name=movie_api_id]').appendTo(form);
            $('.modal-schedule input[name=id_movie_name]').appendTo(form);
            $('.modal-schedule input[name=id_movie_time]').appendTo(form);
            $('.modal-schedule input[name=id_movie_date_active]').appendTo(form);
            form.submit();
        }
    });

    $('#member_form').validate({
        rules: {
            email: {
                required: {
                    depends:function(){
                        $(this).val($.trim($(this).val()));
                        return true;
                    }
                },
                email: true
            },
            password: {
                required: true,
                minlength: 8,
                regex: true
            },
        },
        messages: {
            email: {
                required: message_translate.required,
                email: message_translate.email
            },
            password: {
                required: message_translate.required,
                minlength: message_translate.validatePassword,
            }
        },
        submitHandler: function(form) {
            $.ajax({
                    url: '/login/',
                    type: 'POST',
                    dataType: 'json',
                    data: $(form).serialize() + "&is_popup_schedule=1",
                })
                .done(function(data) {
                    window.location.href = '/booking?id_showtime=' + $('.modal-schedule input[name=id_showtime]').val() + '&id_server=' + $('.modal-schedule input[name=id_server]').val() +
                        '&id_movie_name=' + $('.modal-schedule input[name=id_movie_name]').val() + '&id_movie_time=' + $('.modal-schedule input[name=id_movie_time]').val() +
                        '&id_movie_date_active=' + $('.modal-schedule input[name=id_movie_date_active]').val() + '&movie_api_id=' + $('.modal-schedule input[name=movie_api_id]').val();
                })
                .fail(function(data) {
                    if (data.responseJSON.code == 400) {
                        $.each(data.responseJSON.errors, function(index, val) {
                            $('#error').html(val);
                        });
                    } else {
                        $('#error').html(data.responseJSON.message);
                    }
            });
        }
    });


});