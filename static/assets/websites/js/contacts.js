	
	// active menu (dòng 3-14)
	$j(".block-cms-menu li").each(function(){
		var self = this;
		href = $j(this).find('a');
		for(var i = 0 ; i < href.length ; i++){
			var harray = $j(href[i]).attr('href').split("/");
			var charray = window.location.href.split("/");
			if(harray[harray.length-2] == charray[charray.length-2]){
				$j(self).addClass('active');
				break;
			}
		}
	});


	var message = 'vui lòng cung cấp thông tin rạp, email và số điện thoại thành viên mà bạn đã dùng để đặt vé.';
	var contactForm = new VarienForm('contactForm', true);
	var hoadd = $j('.address-contact-cgv-block-content').html();
	var holocation = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25615.906364793133!2d106.70663701731654!3d10.78025381605616!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xf16ffaa20e46e87f!2sCJ+CGV+Vietnam!5e0!3m2!1sen!2s!4v1459915713967';
	$j('.location-ho-cgv iframe').attr('src',holocation);
	function inquiriyf(obj) {
		if( $j(obj).find('option:selected').attr('data-value') == 2) {
			$j('#comment').attr('placeholder', message);
		}
		else {
			$j('#comment').attr('placeholder','');
		}
	}
	