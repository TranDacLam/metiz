$(document).ready(function() {
	// Play trailer for each movie page home
    $('.play-button').on('click', function (event) {
    	$.magnificPopup.open({
		    items: {
		        src: '<div class="mfp-iframe-scaler">'+
                    '<button title="Close (Esc)" type="button" class="mfp-close">×</button>'+
                    '<iframe class="mfp-iframe" src="'+$(this).find('a').attr("href")+'?rel=0&amp;showinfo=0&amp;autoplay=1" frameborder="0" allowfullscreen></iframe>'+
                    '</div>',
		    },
		    disableOn: 700,
	        type: 'inline',
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