$(document).ready(function() {
	// Play trailer for each movie page home
    $('.play-button').on('click', function (event) {
    	$.magnificPopup.open({
		    items: {
		        src: $(this).find('a').attr("href"),
		    },
		    disableOn: 700,
	        type: 'iframe',
	        mainClass: 'mfp-fade',
	        removalDelay: 160,
	        preloader: false,
	        fixedContentPos: false
		  });
    });
    $('.new-img').mouseenter(function(event) {
    	/* Act on the event */
    	$(this).children('.bg_hover').css('display', 'block');
    });
    $('.new-img').mouseleave(function(event) {
    	/* Act on the event */
    	$(this).children('.bg_hover').css('display', 'none');
    });
});