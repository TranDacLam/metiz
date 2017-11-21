$(document).ready(function() {
 	$('.skip-link').click(function(event) {
 		/* Act on the event */
 		$('.icon-nav').removeClass('bg-icon');
 		$(this).children('.icon-nav').toggleClass('bg-icon');
 	});

 	$('#login-btn').click(function(event) {
 		if ($('#menuNavbar').hasClass('collapse in') || $('#menuNavbar').hasClass('collapsing')) {
		 	$('#menuNavbar').collapse('hide');
		 }
 	});

 	$('#menu-btn').click(function(event) {
 		if ($('#loginNavbar').hasClass('collapse in') || $('#loginNavbar').hasClass('collapsing')) {
	 		$('#loginNavbar').collapse('hide');
 		}
 	});
 	//close menu when click lich chieu
 	$('.open-popup-link').click(function(event) {
 		$('#menuNavbar').collapse('hide');
 	});
});