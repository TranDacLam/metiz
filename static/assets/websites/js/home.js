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

    // auto-customizable width
    // begin
    $(window).bind("load", function() {
        var width = $(window).width();
        if (width >= 979) {
            reinitCycle(4);
        } else if (width >= 770) {
            reinitCycle(3);
        } else if (width >= 479) {
            reinitCycle(2);
        } else {
            reinitCycle(1);
        }
    });

    $(window).on('resize', function() {
        var width = $(window).width();
        $('.feature_slide_show').cycle('destroy');
        if (width >= 979) {
            reinitCycle(4);
        } else if (width >= 770) {
            reinitCycle(3);
        } else if (width >= 479) {
            reinitCycle(2);
        } else {
            reinitCycle(1);
        }
    });

    function reinitCycle(visibleSlides) {
        try {
            $('.feature_slide_show').cycle({
                "carouselSlideDimension": "240px",
                "carouselVisible": visibleSlides,
                "fx": "carousel",
                "timeout": 0,
                "next": ".feature_slide_show_next",
                "prev": ".feature_slide_show_prev",
                "slideActiveClass": "active",
                "slides": "li",
                "allowWrap": false,
            });
        } catch (err) {
            console.log(err.message);
        }
    }
});