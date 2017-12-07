$(document).ready(function() {
 	$('.skip-link').click(function(event) {
 		/* Act on the event */
 		$('.icon-nav').removeClass('bg-icon');
 		$(this).children('.icon-nav').toggleClass('bg-icon');
 	});

 	//closed menu navbar when login navbar opened
 	$('#login-btn').click(function(event) {
 		if ($('#menuNavbar').hasClass('collapse in') || $('#menuNavbar').hasClass('collapsing')) {
		 	$('#menuNavbar').collapse('hide');
		}
		//closed menu navbar in contact page
		if ($('#bs-sidebar-navbar-collapse-1').hasClass('collapse in') || $('#bs-sidebar-navbar-collapse-1').hasClass('collapsing')) {
	 		$('#bs-sidebar-navbar-collapse-1').collapse('hide');
 		}
 	});

 	//closed login navbar when menu navbar opened
 	$('#menu-btn').click(function(event) {
 		if ($('#loginNavbar').hasClass('collapse in') || $('#loginNavbar').hasClass('collapsing')) {
	 		$('#loginNavbar').collapse('hide');
 		}
 		//closed menu navbar in contact page
 		if ($('#bs-sidebar-navbar-collapse-1').hasClass('collapse in') || $('#bs-sidebar-navbar-collapse-1').hasClass('collapsing')) {
	 		$('#bs-sidebar-navbar-collapse-1').collapse('hide');
 		}
 	});
 	//close menu when click lich chieu
 	$('.open-popup-link').click(function(event) {
 		$('#menuNavbar').collapse('hide');
 	});
});