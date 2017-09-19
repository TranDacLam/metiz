       
        $j(document).ready(function() {
        
        $j('#image-gallery').lightSlider({
            gallery:true,
            item:1,
            thumbItem:9,
            slideMargin: 0,
            speed:500,
            pause:4000,
            auto:true,
            loop:true,
            onSliderLoad: function() {
                $j('#image-gallery').removeClass('cS-hidden');
            }  
        });
       
        $j(".content-slider").lightSlider({
            item:4,
            loop:false,
            keyPress:true,
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
                    }
                },
                {
                    breakpoint:768,
                    settings: {
                        item:2,
                        auto:true,
                        slideMove:1,
                        slideMargin:6,
                    }
                },
                {
                    breakpoint:480,
                    settings: {
                        item:1,
                        auto:true,
                        slideMove:1
                    }
                }
            ],
            pager: false
        });
        
});
     