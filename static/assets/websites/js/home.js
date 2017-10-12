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
    var control_owl = {
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
    }
    $('.tabs-format-metiz').toggleOwl(' #movie-tab-1 .owl-carousel', control_owl);
    $('.tabs-format-metiz').toggleOwl('.owl-carousel.style2', control_owl);

    $('.new-img').mouseenter(function(event) {
    	/* Act on the event */
    	$(this).children('.bg_hover').css('display', 'block');
    });
    $('.new-img').mouseleave(function(event) {
    	/* Act on the event */
    	$(this).children('.bg_hover').css('display', 'none');
    });
});