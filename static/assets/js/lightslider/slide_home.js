/* source : http://sachinchoolur.github.io/lightslider */
$(document).ready(function() {
   
    /* slide for movie selection */
    $(".content-slider").lightSlider({
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
                breakpoint:1200,
                settings: {
                    item:3,
                    slideMove:3,
                    slideMargin:30,
                    autoWidth: true,
                }
            },
            {
                breakpoint:991,
                settings: {
                    item:2,
                    slideMove:2,
                    slideMargin:30,
                    autoWidth: true,
                }
            },
            {
                breakpoint:768,
                settings: {
                    item:2,
                    slideMove:1,
                    slideMargin:6,
                    autoWidth: true,
                }
            },
            {
                breakpoint:480,
                settings: {
                    item:1,
                    slideMove:1,
                    autoWidth: true,
                }
            },
            {
                breakpoint:321,
                settings: {
                    item:1,
                    slideMove:1,
                }
            }
        ],
        pager: false
    });
});

