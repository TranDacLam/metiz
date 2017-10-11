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

    $('.owl-carousel').owlCarousel({
        margin: 10,
        dots: false,
        nav: true,
        navText: ["<img src='static/assets/websites/images/left-arrow.png'>","<img src='static/assets/websites/images/right-arrow.png'>"],
        navClass: ['lSPrev','lSNext'],
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                autoWidth: true,
            },
            421: {
                autoWidth: true,
                margin: 5,
            },
            769: {
                items: 3,
                margin: 5,
            },
            1024: {
                items: 4,
                margin: 20,
            }
        }
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