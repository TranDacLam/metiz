/* source : http://sachinchoolur.github.io/lightslider */
$(document).ready(function() {
     $(".special-items li a").each(function(){   
        var name = $(this).attr("href");           
        if(window.location.href.indexOf(name) > -1){
            $(this).parent().addClass('actived');
        }
    });
    /* slide for movie selection and event*/
    var slider = $(".content-slider").lightSlider({
        item:4,
        loop:false,
        keyPress:true,
        slideMove:4,
        auto:true,
        rtl:false,
        speed:1000,
        pause:9000,
        responsive : [
            {
                breakpoint:991,
                settings: {
                    item:2,
                    auto:true,
                    slideMove:1,
                    slideMargin:50,
                    autoWidth: true,
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
                }
            },
            {
                breakpoint:480,
                settings: {
                    item:1,
                    auto:true,
                    slideMove:1,
                    autoWidth: true,
                }
            }
        ],
        pager: false
    });
});

