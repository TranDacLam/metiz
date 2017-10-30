$(document).ready(function() {
    // active popup
    $('.open-popup-link').magnificPopup({
          type: 'inline',
          midClick: true,
    });

    startMonth();

    function listShedule(shedule){
        var htmlShedule = '';
        $.each(shedule.lst_times, function(key, value) {
            htmlShedule +=  '<li class="sold-out">'
                                +'<a href="#" data-toggle="modal" data-target="#warning">'
                                    +'<input type="hidden" name="id_showtime" value="'+ value.id_showtime +'">'
                                    +'<span class="time">'+ value.time +'</span>'
                                    +'<span class="clock">'+ value.time +'<span>~1:15</span></span>'
                                    +'<span class="ppnum">43</span>' // Số ghế trống
                                    +'<span class="ppnum">Room 2</span>' // room chiếu phim
                                    +'<span class="pp-early" title="Suất chiều đầu"></span>'
                                +'</a>'
                            +'</li>';
        });
        return htmlShedule;
    }

    function listFilm(film){
        return  '<div class="movie-time-line-box clearfix" data-control="movie-code">'
                    +'<h3 class="movie-name">'+ film.movie_name +'</h3>'
                    +'<div class="lot-table clearfix">'
                        +'<ul class="list-inline list-unstyled theater_time">'
                            + listShedule(film)
                        +'</ul>'
                   +' </div>'
               +' </div>';
    }

    $(document).on('click', '.popup-movie-schedule', function () { 
        $('.days-popup li').removeClass('active-date');
        if($(this).attr("data-date-seat")){
            var date_seat = $(this).attr("data-date-seat");
            $('.days-popup [data-date-select = '+ date_seat +']').addClass('active-date');
            var date_query = date_seat;
        }else{
            if($(this).attr("data-date-select")){
                var date_query = $(this).attr("data-date-select");
                $(this).addClass('active-date');
            }else{
                var date_query = new Date().toJSON().slice(0,10).replace(/-/g,'-');
                $('.days-popup li:first').addClass('active-date');
            }
        }
        
        // Call Ajax get movie show time with current date
        data = {
            "date": date_query,
            "cinema_id": 1 // get cinema_id from hidden field in popup movie schedule
        }
        $.ajax({
            url: "/movie/show/times",
            type: 'get',
            data: data,
            dataType: 'json',
            crossDomain:false,
            context: this,
        })
        .done(function(response) {
            var html = '';
            $.each(response, function(key, value) {
                if(value.lst_times.length > 0){
                    html += listFilm(value);
                }
            });
            $('.list-schedule').html(html);
            getValue();
        })
        .fail(function() {
            displayMsg();
            $('.msg-result-js').html(msgResult("Error schedule film!", "danger"));
        });
    });

    function getValue(){
         $('.sold-out a').click(function(event) {
            event.preventDefault();
            var id_showtime = $(this).children('input').val();
            console.log(id_showtime);
            $('.modal input[name=id_showtime]').val(id_showtime);
        });
    }

    // message for validate form
    var lang = $('html').attr('lang');
    if ( lang == 'vi') {
        message = {'required': 'Trường này bắt buộc', 
        'minlength_6' :'Nhập ít nhất 6 kí tự',
        'minlength_8' :'Nhập ít nhất 8 kí tự',
        'email': 'Email không hợp lệ',
        'number': 'Nhập các chữ số',
        'equalTo': 'Mật khẩu không khớp. Vui lòng nhập lại',
        'validatePassword': 'Mật khẩu phải chứa ít nhất 1 kí tự đặc biệt và có cả chữ và số',
        'validateDate': 'Nhập ngày theo định dạng dd-mm-yyyy',}
    } else {
        message = {'required': 'This field is required', 
        'minlength_6' :'Please enter at least 6 characters',
        'minlength_8' :'Please enter at least 8 characters',
        'email': 'Please enter a valid email address',
        'number': 'Please enter a valid number',
        'equalTo': "Password don't same. Please enter again",
        'validatePassword': 'Passwords must contain characters, numbers and at least 1 special character',
        'validateDate': 'Please enter a date in the format dd-mm-yyyy'}
    }

    //handle form 
    function validateForm(form){
        $(form).validate({
            rules:{
                name:{
                    required: true,
                },
                email:{
                    email: true
                },
                phone:{
                    required: true,
                    number: true,
                    minlength: 8
                },
            },
            messages:{
                name:{
                    required: message.required,
                },
                email:{
                    email: message.email
                },
                phone:{
                    required: message.required,
                    number: message.number,
                    minlength: message.minlength_8,
                }
            },
            submitHandler: function (form) {
                data= $(form).serialize();
                $.ajax({
                    url: '/booking/',
                    type: 'POST',
                    dataType: 'json',
                    data: data,
                })
                .done(function(data) {
                     $('label.form-error').html('');
                    if(data.errors){
                        $.each(data.errors, function (field, error) {
                            $('label.form-error[for='+ field +']').html(error);
                        });
                    }
                    else{
                        window.location.href = '/booking/' +data.id_sever + '/' + data.id_showtime;
                    }
                })
                .fail(function(data) {
                    $('#error').html(data.message);
                });
            }
        });
    }

    $('#signin_form').validate({
        rules:{
            email:{
                required: true,
                email: true
            },
            password:{
                required: true,
                minlength: 8,
                validatePassword: true
            },
        },
        messages:{
            email:{
                required: message.required,
                email: message.email
            },
            password:{
                required: message.required,
                minlength: message.minlength_8,
            }
        },
        submitHandler: function (form) {
        }
    });

    $.validator.addMethod(
      "validatePassword",
      function (value, element) {
        return value.match(/[^a-z0-9 ]/);
      },
      message.validatePassword
    );

    $('#update_form').submit(function(event) {
        event.preventDefault();
        validateForm($(this));
    });

    $('#guest_form').submit(function(event) {
        event.preventDefault();
        validateForm($(this));
    });
    
    //checkbox for form guest
    $('#agree_term').on('click', function(){
        if($('#agree_term').prop("checked")){
            $('.form-popup button').prop('disabled', false);
        }else{
            $('.form-popup button').prop('disabled', true);
        }
    });

    //active slide for 7 day if browser width < 480
    $('.open-popup-link').click(function(event) {
        loadSlideCalendar();
    });

    $(window).resize(function(event) {
        loadSlideCalendar();
    });
    
    function loadSlideCalendar(){
        if ($( window ).width() < 480 ) {
            $("#play-date-slider").slick({
                slidesToShow: 2,
                slidesToScroll: 2,
                dots: false,
                autoplay: false,
                infinite: false,
                speed: 500,
                arrows: true,
                focusOnSelect: false,
                autoplaySpeed: 4000,
                fade: false,
                centerMode: false,
                prevArrow: "<div class='slick-prev'><img  src='/static/assets/websites/images/btn_m_prev_on.png'></div>",
                nextArrow: "<div class='slick-next'><img  src='/static/assets/websites/images/btn_m_next_on.png'></div>"
            });
        }
        else{
             $("#play-date-slider").slick('unslick');
        }

    }
    
});

function startMonth(){
    // $(".badge:contains('1')").parent().addClass('start-month');
    $('.days-popup li span').each(function() {
        if ($(this).text() == 1) {
            $(this).parent().addClass('start-month');
        }
    });
}
