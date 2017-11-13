$(document).ready(function() {

	// *** Validate form and set data city, district ***
	//message for validate
	var lang = $('html').attr('lang');
    if ( lang == 'vi') {
    	message = {'required': 'Trường này bắt buộc',
    	'phone': 'số điện thoại không hợp lệ',
    	'minlength_2' :'Nhập ít nhất 2 kí tự', 
    	'minlength_6' :'Nhập ít nhất 6 kí tự',
    	'minlength_8' :'Nhập ít nhất 8 kí tự',
    	'email': 'Email không hợp lệ',
    	'number': 'Nhập các chữ số',
    	'equalTo': 'Mật khẩu không khớp. Vui lòng nhập lại',
    	'validatePassword': 'Mật khẩu chứa ít nhất 8 ký tự, bao gồm chữ, số và ký tự hoa hoặc ký tự đặc biệt.',
    	'validateDate': 'Nhập ngày theo định dạng dd-mm-yyyy',}
    } else {
    	message = {'required': 'This field is required', 
    	'phone': 'invalid telephone number',
    	'minlength_2' :'Please enter at least 2 characters', 
    	'minlength_6' :'Please enter at least 6 characters',
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

	// validate form
	$('#signup_form').validate({
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
				validatePhone: message.phone
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
		},
		success: function(element) {
			element.text('OK!').addClass('valid');
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
	$.validator.addMethod(
      "validatePassword",
      function (value, element) {
        // put your own logic here, this is just a (crappy) example 
        return value.match(/[^a-z0-9 ]/);
      },
      message.validatePassword
    );
    $.validator.addMethod(
      "validatePhone",
      function (value, element) {
        // put your own logic here, this is just a (crappy) example 
        return value.match(/^(01[2689]|09|[0-9]|[0-9]{2})[0-9]{8}$/);
      },
      message.phone
    );

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
    
    if(isIE > 0){
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
	
   
	// set datetimepicker
	$('#birth_date').datetimepicker({
		timepicker:false,
		format:'d-m-Y',
        maxDate:'0'
	});

    // *end*

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
});