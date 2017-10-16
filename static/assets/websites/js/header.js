$(document).ready(function() {
	var link_account = 'login';          
        if(window.location.href.indexOf(link_account) > -1){
            $('.skip-account .icon-nav').addClass('bg-icon');
        }
 	$('.skip-link').click(function(event) {
 		/* Act on the event */
 		$('.icon-nav').removeClass('bg-icon');
 		$(this).children('.icon-nav').toggleClass('bg-icon');
 	});

});