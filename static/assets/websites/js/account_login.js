
	function toggleRememberMePopup() {
		var formParent = jQuery(this).parents('form:first');
		formParent.find('.remember-me-box a').toggleClass('hide');
		formParent.find('.remember-me-popup').toggleClass('show');
		return false;
	}
	var rememberMeToggleSetup = false;
	jQuery(document).ready(function(){
		if (!rememberMeToggleSetup) {
			jQuery('.remember-me-box a, .remember-me-popup a').on('click', toggleRememberMePopup);
			rememberMeToggleSetup = true;
	}
	});
	


	function toggleRememberMePopup() {
		var formParent = jQuery(this).parents('form:first');
		formParent.find('.remember-me-box a').toggleClass('hide');
		formParent.find('.remember-me-popup').toggleClass('show');
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
								
	