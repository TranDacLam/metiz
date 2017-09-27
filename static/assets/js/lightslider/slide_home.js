       
        /* source : http://sachinchoolur.github.io/lightslider */
        $(document).ready(function() {
            $(".special-items li a").each(function(){   
                var name = $(this).attr("href");           
                if(window.location.href.indexOf(name) > -1){
                    $(this).parent().addClass('actived');
                }
            });
        /* slide for special movie*/
            $('#image-gallery').lightSlider({
                    gallery:true,
                    item:1,
                    thumbItem:9,
                    slideMargin: 0,
                    speed:500,
                    auto:true,
                    loop:true,
                    onSliderLoad: function() {
                        $('#image-gallery').removeClass('cS-hidden');
                    }  
                });
            /* slide for movie selection and event*/
            $(".content-slider").lightSlider({
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
     


