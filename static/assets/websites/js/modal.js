    $(document).ready(function() {
        // active popup
        $('.open-popup-link').magnificPopup({
              type: 'inline',
              midClick: true,
        });

        $('.available:first').addClass('active');
        startMonth();

        $('.open-popup-link').click(function(event) {
            loadSlideCalendar();

            // show  present movies
            var date= $('li.available.active').attr('data-play-date');
            $(".movieslide[data-play-date='" + date + "']").css('display', 'block');

            // slick slider go to today
            var number= $(".active").attr('data-slick-index');
            $("#play-date-slider").slick('slickGoTo',  number);

        });

        // funtion for choose day
        $('.available').click(function(event) {
            $('.days-popup li').removeClass('active');
            $(this).addClass('active');

            var date= $(this).attr('data-play-date');
            $(".movieslide").css('display', 'none');
            $(".movieslide[data-play-date='" + date + "']").css('display', 'block');
        });
    });
    function startMonth(){
        // $(".badge:contains('1')").parent().addClass('start-month');
        $('.days-popup li span').each(function() {
            if ($(this).text() == 1) {
                $(this).parent().addClass('start-month');
            }
        });
    }
    // funcion load slider
    function loadSlideCalendar(){
        $("#play-date-slider").slick({
            slidesToShow: 10,
            slidesToScroll: 10,
            dots: false,
            autoplay: false,
            infinite: false,
            speed: 500,
            arrows: true,
            focusOnSelect: false,
            autoplaySpeed: 4000,
            fade: false,
            centerMode: false,
            responsive: [
                {
                  breakpoint: 1170,
                  settings: {
                    slidesToShow: 8,
                    slidesToScroll: 8
                  }
                },
                {
                  breakpoint: 1024,
                  settings: {
                    slidesToShow: 8,
                    slidesToScroll: 8
                  }
                },
                {
                  breakpoint: 768,
                  settings: {
                    slidesToShow: 5,
                    slidesToScroll: 5
                  }
                },
                {
                  breakpoint: 480,
                  settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                  }
                }],
            prevArrow: "<div class='slick-prev'><img  src='/static/assets/websites/images/btn_m_prev_on.png'></div>",
            nextArrow: "<div class='slick-next'><img  src='/static/assets/websites/images/btn_m_next_on.png'></div>"
        });
    }

