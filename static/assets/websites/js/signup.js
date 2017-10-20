$(document).ready(function() {
	// validate forml
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
				minlength: 8
			},
			password2:{
				required: true,
				minlength: 8,
				equalTo: "#password1"
			},
		},
		messages:{
			full_name:{
			}
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
				minlength: 8
			},
		}
	});
	$.validator.addMethod(
      "validateDate",
      function (value, element) {
        // put your own logic here, this is just a (crappy) example
        return value.match(/^\d\d?\-\d\d?\-\d\d\d\d$/);
      },
      "Please enter a date in the format dd-mm-yyyy"
    );

	// demo data
	var list_city = {'Da Nang': [' Hải Châu', 'Thanh Khê', ' Sơn Trà', 'Ngũ Hành Sơn', 'Liên Chiểu', 'Hòa Vang', ' Cẩm Lệ', ' Hoàng Sa'],
	'Ha Noi': [' Hoàn Kiếm', 'Ba Đình', 'Hai Bà Trưng'],
	'HCM': ['1','2','3', '4', '5', '6', 'Tân Bình'], 'khac': ['khac']};

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
