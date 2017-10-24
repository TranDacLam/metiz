$(document).ready(function() {
	var lang = $('html').attr('lang');
    if ( lang == 'vi') {
    	message = {'required': 'Trường này bắt buộc', 
    	'minlength_6' :'Nhập ít nhất 6 kí tự',
    	'minlength_8' :'Nhập ít nhất 8 kí tự',
    	'email': 'Email không hợp lệ',
    	'number': 'Nhập các chữ số',
    	'equalTo': 'Mật khẩu không khớp. Vui lòng nhập lại',
    	'validatePassword': 'Mật khẩu phải chứa ít nhất 1 kí tự đặc biệt và có cả chữ và số',
    	'validateDate': 'Nhập ngày theo định dạng dd-mm-yyyy',}
    } else {
    	message = {'required': 'This field is required', 
    	'minlength_6' :'Please enter at least 6 characters',
    	'minlength_8' :'Please enter at least 8 characters',
    	'email': 'Please enter a valid email address',
    	'number': 'Please enter a valid number',
    	'equalTo': "Password don't same. Please enter again",
    	'validatePassword': 'Passwords must contain characters, numbers and at least 1 special character',
    	'validateDate': 'Please enter a date in the format dd-mm-yyyy'}
    }

	// validate form
	$('#signup_form').validate({
		rules:{
			full_name:{
				minlength: 6,
	        	required: true
			},
			birth_date:{
				required: true,
				validateDate: true
			},
			phone:{
				required: true,
				number: true
			},
			email:{
				required: true,
				email: true
			},
			password1:{
				required: true,
				minlength: 8,
				validatePassword: true
			},
			password2:{
				required: true,
				equalTo: "#password1"
			},
		},
		messages:{
			full_name:{
				required: message.required,
				minlength: message.minlength_6
			},
			birth_date:{
				required: message.required,
				validateDate: message.validateDate
			},
			phone:{
				required: message.required,
				number: message.number
			},
			email:{
				required: message.required,
				email: message.email
			},
			password1:{
				required: message.required,
				minlength: message.minlength_8
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

	$('#signin_form').validate({
		rules:{
			email:{
				required: true,
				email: true
			},
			password:{
				required: true,
				minlength: 8,
				validatePassword: true
			},
		},
		messages:{
			email:{
				required: message.required,
				email: message.email
			},
			password:{
				required: message.required,
				minlength: message.minlength_8,
			}
		},
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
   

	// demo data 
	var list_city = {'Đà Nẵng': [' Hải Châu', 'Thanh Khê', ' Sơn Trà', 'Ngũ Hành Sơn', 'Liên Chiểu', 'Hòa Vang', ' Cẩm Lệ', ' Hoàng Sa'], 
	'Hà Nội': [' Hoàn Kiếm', 'Ba Đình', 'Hai Bà Trưng'], 
	'Hồ Chí Minh': ['1','2','3', '4', '5', '6', 'Tân Bình'], 'Khác': ['Khác']};
	
	// load city and district but district hide
	$.each(list_city, function(index, val) {
		var name_city= index;
		$('.list-city').append('<option value="' + name_city + '">' +name_city + '</option>');
		$.each(val, function(index, val) {
	 		$('.list-district').append('<option value="' + val + '" class = "' + name_city + '">' +val + '</option>');
	 	});
	 	$('.list-district').children().hide();

	});

	// funtion show district for each city
	function selectDistrict(list_city){
		var name_city= $('.list-city').val();
		$.each(list_city, function(index, val) {
			if (index == name_city ) {
				$('.list-district').children().hide();
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

	// set datetimepicker
	// $.datetimepicker.setLocale('vi');
	$('#birth_date').datetimepicker({
		timepicker:false,
		format:'d-m-Y',
	});

	// checkbox dieu khoan register
	$('#is_agree').on('click', function(){
		if($('#is_agree').prop("checked")){
			$('#signup_form button').prop('disabled', false);
		}else{
			$('#signup_form button').prop('disabled', true);
		}
	});
});