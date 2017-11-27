$(document).ready(function() {
	//action for show map in footer 
    $('.map-trigger').click(function(event) {
        event.preventDefault();
        $('#content-map').slideToggle();
        $('.map-trigger').toggleClass('show');
        if ($('.map-trigger').hasClass('show')) {
        	$('html,body').animate({ scrollTop: $('#content-map').offset().top }, 500);
        }
       
    });
});
