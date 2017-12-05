$(document).ready(function() {

	// *** Validate form and set data city, district ***
	//message for validate
	var lang = $('html').attr('lang');
    if ( lang == 'vi') {
    	message = {'required': 'Trường này bắt buộc',
    	'phone': 'Số điện thoại không hợp lệ',
    	'minlength_2' :'Nhập ít nhất 2 kí tự', 
    	'minlength_9' :'Nhập ít nhất 9 kí tự',
    	'minlength_8' :'Nhập ít nhất 8 kí tự',
    	'email': 'Email không hợp lệ',
    	'number': 'Vui lòng chỉ nhập các chữ số',
    	'equalTo': 'Mật khẩu không khớp. Vui lòng nhập lại',
    	'validatePassword': 'Mật khẩu chứa ít nhất 8 ký tự, bao gồm chữ, số và ký tự hoa hoặc ký tự đặc biệt.',
    	'validateDate': 'Nhập ngày theo định dạng dd-mm-yyyy',}
    } else {
    	message = {'required': 'This field is required', 
    	'phone': 'invalid telephone number',
    	'minlength_2' :'Please enter at least 2 characters', 
    	'minlength_9' :'Please enter at least 9 characters',
    	'minlength_8' :'Please enter at least 8 characters',
    	'email': 'Please enter a valid email address',
    	'number': 'Please enter a valid number',
    	'equalTo': "Password don't same. Please enter again",
    	'validatePassword': 'Passwords must contain characters, numbers and at least 1 special character',
    	'validateDate': 'Please enter a date in the format dd-mm-yyyy'}
    }

    // validate password
    $.validator.addMethod(
        "regex",
         function(value, element) {
            return this.optional(element) || (value.match(/[a-z]/) && value.match(/[!@#$%^&*()_+A-Z]/) && value.match(/[0-9]/));
        },
        message.validatePassword
    );

    // validate phone, persional only number
    var selectorPhone = $("#signup_form input[name=phone]");
    var selectorPersonal = $("#signup_form input[name=personal_id]");
    // Call back validOnlyNumber layout.js 
    validOnlyNumber(selectorPhone, '');
    validOnlyNumber(selectorPersonal, '');

    // Submit form check validate captcha
    $('#signup_form').on('submit', function(e) {
        var res = grecaptcha.getResponse(widId);

        if (res == "" || res == undefined || res.length == 0){
            e.preventDefault();
            $('.captcha-error').text("Vui lòng xác nhận captcha");
            return false;
        }
        //recaptcha passed validation 
        return true;
    });

	// validate form
	$('#signup_form').validate({
        focusInvalid: false,
		rules:{
			full_name:{
				minlength: 2,
	        	required: true
			},
			birth_date:{
				required: true,
				validateDate: true
			},
			phone:{
				required: true,
				validatePhone: true,
                number: true,
                minlength:9,
			},

			email:{
				required: true,
				email: true
			},
			password1:{
				required: true,
				minlength: 8,
				regex: true
			},
			password2:{
				required: true,
				equalTo: "#password1"
			},
            personal_id:{
                required: false,
                minlength: 9,
                number: true
           }
		},
		messages:{
			full_name:{
				required: message.required,
				minlength: message.minlength_2
			},
			birth_date:{
				required: message.required,
				validateDate: message.validateDate
			},
			phone:{
				required: message.required,
				validatePhone: message.phone,
                number: message.number,
                minlength: message.phone,
			},
			email:{
				required: message.required,
				email: message.email
			},
			password1:{
				required: message.required,
				minlength: message.validatePassword
			},
			password2:{
				required: message.required,
				equalTo: message.equalTo
			},
            personal_id:{
                minlength: message.minlength_9,
                number: message.number
           }
		},
		success: function(element) {
            //personal_id is null,it don't add class valid
            if($('#personal_id').val() == ''){
                element.not('#personal_id-error').addClass('valid');
            }else{
                element.addClass('valid');
            }
		},
        invalidHandler: function() {
            //don't focus input birth_date
            $(this).find("input.error").not('#birth_date').focus();
        }
	});

	$('#login_form').validate({
		rules:{
			email:{
				required: true,
				email: true
			},
			password:{
				required: true,
				minlength: 8,
				regex: true
			},
		},
		messages:{
			email:{
				required: message.required,
				email: message.email
			},
			password:{
				required: message.required,
				minlength: message.validatePassword,
			}
		}
	});
	$.validator.addMethod(
      "validateDate",
      function (value, element) {
        // put your own logic here, this is just a (crappy) example
        return value.match(/^\d\d?\-\d\d?\-\d\d\d\d$/);
      },
      message.validateDate
    );


    // set datetimepicker for signup and profile

    // Get current date 5 year ago
    var date_now = new Date();
    var date_day = ("0" + date_now.getDate()).slice(-2);
    var date_month = ("0" + (date_now.getMonth() + 1)).slice(-2);
    var date_today = (date_now.getFullYear() - 5) + "-" + (date_month) + "-" + (date_day);

    $('#birth_date').datebox({
            mode: "calbox",
            beforeToday: true,
            useFocus: true,
            useButton: false,
            useHeader: false,
            calShowDays: false,
            calUsePickers: true,
            calHighToday:true,
            themeDatePick: 'warning',
            defaultValue: date_today,
            calYearPickMax: 'NOW',
            calYearPickMin: 100,
            beforeOpenCallback: function(){
                //if having error hide errortext 
                if($('#birth_date-error').length){
                    $('.input-group #birth_date-error').css('display', 'none');// of jquery validate
                    $('#birth_date').css('color','#555');
                }
            },
            closeCallback: function(){
                //if date valid show tick image
                if($('#birth_date').val() != ''){
                    $('.birthday-inline #birth_date_valid').css('display', 'inline-block');
                }else{
                    $('.input-group #birth_date-error').css('display', 'inline-block');
                }
            },
        });

    if( navigator.userAgent.match(/iPhone|iPad|iPod|Android/i)){
        $('#birth_date').datebox({
            mode: "flipbox",
            beforeToday: true,
            useFocus: true,
            useButton: false,
            useHeader: true,
            defaultValue: date_today,
        });
    }
    $('#birth_date').attr("readonly", false);
    // *end*

   	// CHOOSE CITY AND DISTRICT
	// Step 1: Load data for city and district, but district hide
	// Step 2: Choose city, hide all district, show district appropriate, 
	// Step 3: Change city, hide all district, show district appropriate, 

    // *** User for Page profile and signup ***
    // *begin*
	// data city 
	var list_city = {'Đà Nẵng': ['Hải Châu', 'Thanh Khê', ' Sơn Trà', 'Ngũ Hành Sơn', 'Liên Chiểu', 'Hòa Vang', ' Cẩm Lệ', ' Hoàng Sa'], 
	'Hà Nội': [' Hoàn Kiếm', 'Ba Đình', 'Hai Bà Trưng'], 
	'Hồ Chí Minh': ['1','2','3', '4', '5', '6', 'Tân Bình'], 'Khác': ['Khác']};
	
	// load city and district but district hide
    var current_city = $("#id_city").val();
    var current_district = $("#id_district").val();

    // Check browser there must be IE
    var isIE = window.navigator.userAgent.indexOf("Trident");
    var isIOS = navigator.userAgent.match(/(\(iPod|\(iPhone|\(iPad)/);
    if(isIE > 0 || isIOS){
        // Browser IE

        // *** CHOOSE CITY AND DISTRICT ***
        // Step 1: Get current city and current district
        // Step 2: 
        // - TH1: load first page, call function selectDistrict
        // --- Get all district of current city
        // - TH2: change city
        // --- Remove all list city and dictrict, not remove "Chon Quan" (disavled).
        // --- callback function selectDictrict, back TH1.

        selectDistrict(list_city, current_city);
        // funtion show district for each city
        function selectDistrict(list_city, current_name_city){
            $.each(list_city, function(index, val) {
                var name_city= index;
                if(current_name_city && name_city==current_name_city){
                    $('.list-city').append('<option value="' + name_city + '" selected>' +name_city + '</option>');
                }else{
                    $('.list-city').append('<option value="' + name_city + '">' +name_city + '</option>');    
                }

                if(current_name_city && name_city==current_name_city){
                    $.each(val, function(index, val) {
                        if(current_district && val==current_district){
                            $('.list-district').append('<option value="' + val + '" class = "' + name_city + '" selected>' +val + '</option>');
                        }else{
                            $('.list-district').append('<option value="' + val + '" class = "' + name_city + '">' +val + '</option>');     
                        }
                    });
                }
            });
        };

        $('.list-city').on('change', function(event) {
            event.preventDefault();
            var name_city= $('.list-city').val();
            $('.list-city option').remove();
            $('.list-district option').not(":disabled").remove();
            $('.list-district option').attr('selected', 'selected');
            selectDistrict(list_city, name_city);
        });
    }else{
        // Browser not IE
        $.each(list_city, function(index, val) {
            var name_city= index;
            if(current_city && name_city==current_city){
                $('.list-city').append('<option value="' + name_city + '" selected>' +name_city + '</option>');
            }else{
                $('.list-city').append('<option value="' + name_city + '">' +name_city + '</option>');    
            }
            
            $.each(val, function(index, val) {
                if(current_city && name_city==current_city){
                    if(current_district && val==current_district){
                        $('.list-district').append('<option value="' + val + '" class = "' + name_city + ' show-district" selected>' +val + '</option>');
                    }else{
                        $('.list-district').append('<option value="' + val + '" class = "' + name_city + ' show-district">' +val + '</option>');     
                    }
                }
                else{
                    if(current_district && val==current_district){
                        $('.list-district').append('<option value="' + val + '" class = "' + name_city + '" selected>' +val + '</option>');
                    }else{
                        $('.list-district').append('<option value="' + val + '" class = "' + name_city + '">' +val + '</option>');     
                    }
                }
            });
        });
        $('.list-district').children().hide();
        $('.list-district .show-district').css('display','block');

        // funtion show district for each city
        function selectDistrict(list_city){
            var name_city= $('.list-city').val();
            $('.list-district').children().hide();
            $('.list-district option').first().css('display', 'block').prop("selected", true);
            $.each(list_city, function(index, val) {
                if (index == name_city ) {
                    $('.list-district option').each(function(index, el) {
                        if ($(this).hasClass(name_city)) {
                            $(this).show();
                        }
                    });
                }
             });
        };

        $('.list-city').on('change', function(event) {
            event.preventDefault();
            selectDistrict(list_city);
        });
    }
	


	// checkbox dieu khoan register
	$('#is_agree').on('click', function(){
		if($('#is_agree').prop("checked")){
			$('#signup_form button').prop('disabled', false);
		}else{
			$('#signup_form button').prop('disabled', true);
		}
	});

	//delete old error message when fill input in register form
	$('#myTabContent .form-group input').click(function(event) {
		$(this).parent().children('.errorlist').hide();
	});

	//dont allow key e in input phone
	$("#myTabContent input[type=number]").on("keydown", function(e){
		return e.keyCode == 69 ? false : true;
	});

	//set null for password when return error form
	if ($('#password1').val() && $('#password2').val()){
		$('#password1').one("click",function(event) {
			$('#password1').val(null);
		});
		$('#password2').one("click",function(event) {
			$('#password2').val(null);
			
		});
	}
});

// load recaptcha 
var widId = "";
// device IOS
var isIOS = navigator.userAgent.match(/(\(iPod|\(iPhone|\(iPad)/);
// scroll to form conactForm
var focusWhatever = function (response) {
    // check device
    if(isIOS){
        $("html, body").animate({ scrollTop: $("#scroll-captcha").offset().top }, "slow");
    }
};

// on load captcha
var onloadCallback = function ()
{
    widId = grecaptcha.render('re-captcha', {
        'sitekey': recaptchaKey,
        'theme': "light",
        'callback' : focusWhatever
    });
};