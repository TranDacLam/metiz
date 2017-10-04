
/* source : http://sachinchoolur.github.io/lightslider */
$(document).ready(function() {
     $(".special-items li a").each(function(){   
        var name = $(this).attr("href");           
        if(window.location.href.indexOf(name) > -1){
            $(this).parent().addClass('actived');
        }
    });

    /* slide for movie selection */
    var content_slider = {
        item:4,
        loop:false,
        keyPress:true,
        slideMove:4,
        auto:true,
        rtl:false,
        speed:1000,
        pause:9000,
        controls: false,
        responsive : [
            {
                breakpoint:1366,
                settings: {
                    item:4,
                    auto:true,
                    slideMove:1,
                    slideMargin:50,
                    autoWidth: true,
                    controls: true,
                }
            },
            {
                breakpoint:1024,
                settings: {
                    item:3,
                    auto:true,
                    slideMove:1,
                    slideMargin:50,
                    autoWidth: true,
                    controls: true,
                }
            },
            {
                breakpoint:991,
                settings: {
                    item:2,
                    auto:true,
                    slideMove:1,
                    slideMargin:50,
                    autoWidth: true,
                    controls: true,
                }
            },
            {
                breakpoint:768,
                settings: {
                    item:2,
                    auto:true,
                    slideMove:1,
                    slideMargin:6,
                    autoWidth: true,
                    controls: true,
                }
            },
            {
                breakpoint:480,
                settings: {
                    item:1,
                    auto:true,
                    slideMove:1,
                    autoWidth: true,
                    controls: true,
                }
            }
        ],
        pager: false
    }
    var slider_showing = $("#content-slider-showing").lightSlider(content_slider);
    var slider_comming_soon= $("#content-slider-comming-soon").lightSlider(content_slider);

    $('#goToPrevSlide-showing').on('click', function () {
        slider_showing.goToPrevSlide();
    });
    $('#goToNextSlide-showing').on('click', function () {
        slider_showing.goToNextSlide();
    }); 

    $('#goToPrevSlide-comming-soon').on('click', function () {
        slider_comming_soon.goToPrevSlide();
    });
    $('#goToNextSlide-comming-soon').on('click', function () {
        slider_comming_soon.goToNextSlide();
    });

    $('#goToPrevSlide-comming-soon, #goToNextSlide-comming-soon').hide();
    $('.metiz-movie-tabs li:last span').on('click', function () {
        $('#goToPrevSlide-showing, #goToNextSlide-showing').hide();
        $('#goToPrevSlide-comming-soon, #goToNextSlide-comming-soon').show();
    });

    $('.metiz-movie-tabs li:first span').on('click', function () {
        $('#goToPrevSlide-showing, #goToNextSlide-showing').show();
        $('#goToPrevSlide-comming-soon, #goToNextSlide-comming-soon').hide();
    });
});

