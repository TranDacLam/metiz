$(document).ready(function() {
	// Play trailer for each movie page home
    $('.popup-youtube').on('click', function (event) {
        event.preventDefault();
        
    	$.magnificPopup.open({
		    items: {
		        src: $(this).attr("href"),
		    },
		    disableOn: 700,
	        type: 'iframe',
	        mainClass: 'mfp-fade',
	        removalDelay: 160,
	        preloader: false,
	        fixedContentPos: false
		  });
    });

    // handle tooogle with Owl carousel
    $.fn.extend({
        toggleOwl: function(selector, options, destroy){
            return this.each(function(){
                $(this).find(selector).filter(function(){
                    return $(this).parent().is(':visible');
                }).owlCarousel(options);
          
                $(this).on('shown.bs.tab', function(event){
                    var target = $(event.target.getAttribute('href')).find(selector);
                    if(!target.data('owlCarousel')){
                        var owl = target.owlCarousel(options).data("owlCarousel");
                    }
                });
                if(destroy === true){
                    $(this).on('hide.bs.tab', function(event){
                        var target = $(event.target.getAttribute('href')).find(selector);
                        if(target.data('owl.carousel')){
                            target.data('owl.carousel').destroy();
                        }
                    });        
                }
            });
        }
    });

    // Carousel slide movie page Home
    function initOwlOption(total_item) {
        return control_owl = {
            margin: 10,
            dots: false,
            // loop:true,
            autoplay:true,
            smartSpeed:1000,
            autoplayTimeout:2000,
            // autoplayHoverPause:true,
            nav: true,
            navText: ["<img width='100%' src='static/assets/websites/images/left-arrow.png'>","<img width='100%' src='static/assets/websites/images/right-arrow.png'>"],
            navClass: ['lSPrev','lSNext'],
            responsiveClass: true,
            responsive: {
                0: {
                    items: 2,
                    loop: total_item > 2 ? true : false,
                },
                421: {
                    autoWidth: true,
                    margin: 20,
                    loop: total_item > 2 ? true : false,
                },
                767: {
                    items: 3,
                    margin: 20,
                    loop: total_item > 3 ? true : false,
                },
                992: {
                    items: 4,
                    margin: 20,
                    loop: total_item > 4 ? true : false,
                },
                1025: {
                    items: 4,
                    margin: 35,
                    loop: total_item > 4 ? true : false,
                }
            }
        }
    }

    function initOwl(element) {
        total_item = $(element).children(".item").length;
        $('.tabs-format-metiz').toggleOwl(element, initOwlOption(total_item));
    }
    initOwl('#movie-tab-1 .owl-carousel');
    initOwl('.owl-carousel.style2');
    /* 
        fix bug auto play not working when reactive tab
        step1: when leave tab then stop autoplay
        step2: when comeback to tab then play autoplay
    */
    document.addEventListener("visibilitychange", function() {
        if (document.hidden){
            $('#movie-tab-1 .owl-carousel').trigger('stop.owl.autoplay');
            $('.owl-carousel.style2').trigger('stop.owl.autoplay');
        } else {
            $('#movie-tab-1 .owl-carousel').trigger('play.owl.autoplay',[1000]);
            $('.owl-carousel.style2').trigger('play.owl.autoplay',[1000]);
        }
    });

    $('#movie-tab-1 .owl-carousel, .owl-carousel.style2').mouseleave(function() {
        $(this).trigger('play.owl.autoplay',[1000]);
    }).mouseover(function() {
        $(this).trigger('stop.owl.autoplay');
    });
});