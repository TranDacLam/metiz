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

    jssor_1_slider_init();
        
});