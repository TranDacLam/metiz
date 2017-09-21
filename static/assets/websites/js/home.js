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
    // (64-91) function click tab slide
    function openMovie(evt, movie) {
        var i, tabcontent, tablinks;
        tabcontent = document.getElementsByClassName("tabcontent");
        for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
        }
        tablinks = document.getElementsByClassName("tablinks");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        
        document.getElementById(movie).style.display = "block";
        evt.currentTarget.className += " active";
    }
            
    function openCategory(evt, category) {
        var i, tabcontent1, tablinks1;
        tabcontent1 = document.getElementsByClassName("tabcontent1");
        for (i = 0; i < tabcontent1.length; i++) {
            tabcontent1[i].style.display = "none";
        }
        tablinks1 = document.getElementsByClassName("tablinks1");
        for (i = 0; i < tablinks1.length; i++) {
            tablinks1[i].className = tablinks1[i].className.replace(" active", "");
        }
        document.getElementById(category).style.display = "block";
        evt.currentTarget.className += " active";
    }
            
        
});