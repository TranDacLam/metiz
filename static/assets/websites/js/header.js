$(document).ready(function() {
 	$('.skip-link').click(function(event) {
 		/* Act on the event */
 		$('.icon-nav').removeClass('bg-icon');
 		$(this).children('.icon-nav').toggleClass('bg-icon');
 	});
 	$('#login-btn').click(function(event) {
 		/* Act on the event */
 		if ($('#myNavbar').hasClass('collapse in')) {
 			$('#myNavbar').removeClass('in');
 		}
 	});
 	$('#menu-btn').click(function(event) {
 		/* Act on the event */
 		if ($('#loginNavbar').hasClass('collapse in')) {
 			$('#loginNavbar').removeClass('in');
 		}
 	});
});