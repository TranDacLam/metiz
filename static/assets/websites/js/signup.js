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
				date: true
			},
			phone:{
				required: true,
				number: true
			},
			email:{
				required: true,
				email: true
			},
			personal_id:{
				required: true,
				number: true
			},
			password1:{
				required: true,
				minlength: 6
			},
			password2:{
				required: true,
				minlength: 6,
				equalTo: "#password1"
			},
			address:{
				required: true,
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
	$.datetimepicker.setLocale('vi');
	$('#birth_date').datetimepicker({
		timepicker:false,
		format:'d/m/Y',
		formatDate:'Y/m/d',
	});
	
});