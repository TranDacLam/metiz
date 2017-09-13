	
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
	

	var dataForm = new VarienForm('login-form', true);
								
	