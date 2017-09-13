	// Chọn rạp và thể loại phim yêu thích (dòng 3-19)
	//Chọn rạp yêu thích
	jQuery('.prefersite').on('change', function() {
		var site1=jQuery('#prefersite').find(":selected").val();
		var site2=jQuery('#prefersite2').find(":selected").val();
		if(site1 == site2){
			alert('Prefered sites cannot be same!');
			jQuery(this).val('');
		}
	});
	// Chọn thể loại phim ưa thích
	jQuery('.prefergenre').on('change', function() {
		var site1=jQuery('#prefergenre').find(":selected").val();
		var site2=jQuery('#prefergenre2').find(":selected").val();
		if(site1 == site2){
			alert('Prefered genres cannot be same!');
			jQuery(this).val('');
		}
	});

	// show/hide class được tìm thấy
	function toggleRememberMePopup() {
		var formParent = jQuery(this).parents('form:first'); // select element đầu tiên của form
		formParent.find('.remember-me-box a').toggleClass('hide'); // ẩn element của class .remember-me-box a
		formParent.find('.remember-me-popup').toggleClass('show'); // show element của class .remember-me-popup
		return false;
	}

	var rememberMeToggleSetup = false;
	jQuery(document).ready(function(){
		if (!rememberMeToggleSetup) {
		jQuery('.remember-me-box a, .remember-me-popup a').on('click', toggleRememberMePopup);
		rememberMeToggleSetup = true;
	}
	});

	// translation
	var Translator = new Translate({"Use letter & number, min. 6 characters.":"Ít nhất 6 ký tự, bao gồm chữ và số.","Please enter numbers (0-9) starting from 0. For example 0123456789.":"Vui lòng nhập đúng số điện thoại.","Please enter 6 or more characters without leading or trailing spaces.":"Vui lòng nhập 6 ký tự trở lên, không khoảng trắng hoặc dấu cách dẫn","Please enter a valid email address. For example johndoe@domain.com.":"Vui lòng nhập đúng địa chỉ email. Ví dụ: johndoe@domain.com","Please make sure your passwords match.":"Vui lòng đảm bảo mật khẩu phù hợp.","This is a required field.":"Phải nhập thông tin.","This date is a required value.":"Phải nhập thông tin.","Please enter a valid full date":"Vui lòng nhập đúng định dạng ngày sinh"});
	var dataForm = new VarienForm('form-validate', true);
	Form.getElements('form-validate').each(function(element) {
		element.setAttribute('autocomplete', 'off');
	});

	// load Quan/Huyen theo Tinh/TP (dòng 45-70)
	function loadDistrict(provinceObj, districtId){
		if( jQuery(provinceObj).val() == '' ){
			jQuery('#'+districtId).empty();
			return;
		}
		jQuery.ajax({
			type: 'post',
			url: '#',
			data: 'region_id='+ jQuery(provinceObj).val()+'&empty=true',
			success: function(_province_data){
				jQuery('#city').empty();
				select='';
				for(i=0;i<_province_data.length;i++) {
					if (_province_data[i].label =="Vui lòng chọn..."){
						jQuery('#city').append('<option data-id="" value="">'+_province_data[i].label+'</option>');
					} else {
						// if(jQuery(provinceObj).val() == _province_data[i].id+)
							// select=' selected';
						jQuery('#city').append('<option data-id='+_province_data[i].value+' value="'+_province_data[i].label+'"'+select+'>'+_province_data[i].label+'</option>');
					}
				}
				jQuery('#city').attr('disabled', false);
			}
		});
		//jQuery('#city').attr('disabled', false);
	}


	var customer_dob = new Varien.DOB('.customer-dob', true, '%d/%m/%Y');
							
	
							