$(document).ready(function() {
    // active popup
    $('.open-popup-link').magnificPopup({
          type: 'inline',
          midClick: true,
    });

    startMonth();

    // list show time of a movie, callback from function listFilm
    function listShedule(shedule){
        var htmlShedule = '';
        $.each(shedule.lst_times, function(key, value) {
            htmlShedule +=  '<li class="sold-out">'
                                +'<a href="#" data-toggle="modal" data-target="#warning">'
                                    +'<input type="hidden" name="id_showtime" value="'+ value.id_showtime +'">'
                                    +'<input type="hidden" name="id_movie_name" value="'+ shedule.movie_name +'">'
                                    +'<span class="time">'+ value.time +'</span>'
                                    +'<span class="clock">'+ value.time +'</span>'
                                    +'<span class="ppnum">43</span>' // Số ghế trống
                                    +'<span class="ppnum"></span>' // room chiếu phim
                                    +'<span class="pp-early" title="Suất chiều đầu"></span>'
                                +'</a>'
                            +'</li>';
        });
        return htmlShedule;
    }

    // list movie 
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


    var movie_api_id;

    $(document).on('click', '.popup-movie-schedule', function () { 
        $('.days-popup li').removeClass('active-date');

        var id_sever = $('.list-cinema .active').attr('data-id-server');
        
        // get movie api id at booking ticket every film
        if($(this).attr("data-movie-api-id")){
            movie_api_id = $(this).attr("data-movie-api-id");
        }
        
        if($(this).attr("data-all-movie") || $(this).attr("data-date-seat")){
            movie_api_id = null;
        }

        // get date time at page booking 
        if($(this).attr("data-date-seat")){
            var date_seat = $(this).attr("data-date-seat");
            $('.days-popup [data-date-select = '+ date_seat +']').addClass('active-date');
            var date_query = date_seat;
        }else{
            // get date time on page popup
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
            "movie_api_id": movie_api_id,
            "cinema_id": id_sever // get cinema_id from hidden field in popup movie schedule
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
            if ($('.list-schedule').text() == '') {
                $('.list-schedule').html('<p class="empty-schedule">Ngày Bạn Chọn Hiện Không Có Lich Chiếu Nào. Vui Lòng Chọn Ngày Khác<p/>');
            }
        })
        .fail(function() {
            displayMsg();
            $('.msg-result-js').html(msgResult("Error schedule film!", "danger"));
        });
    });

    function getValue(){
         $('.sold-out a').click(function(event) {
            event.preventDefault();
            var id_showtime = $(this).children('input[name=id_showtime]').val();
            var id_movie_name = $(this).children('input[name=id_movie_name]').val();
            var id_movie_time = $(this).children('span[class=time]').text();
            
            $('.modal input[name=id_sever]').val(1);
            $('.modal input[name=id_showtime]').val(id_showtime);
            $('.modal input[name=id_movie_name]').val(id_movie_name);
            $('.modal input[name=id_movie_time]').val(id_movie_time);
            $('.modal input[name=id_movie_date_active]').val($("li.active-date").attr("data-date-select"));
            
            $('#member_form #id_showtime_memeber').text(id_showtime);
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

    //validate guest form, update form
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
            }
        });
    }
    $('.form-popup').each(function(index, el) { 
        validateForm($(this)); 
    });

    // handle member form
    $('#member_form').validate({
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
            var id_sever = $('.list-cinema .active').attr('data-id-server');

            $.ajax({
                url: '/login/',
                type: 'POST',
                dataType: 'json',
                data: $(form).serialize() + "&schedule_key=1",
            })
            .done(function(data) {
                id_showtime = $('#member_form #id_showtime_memeber').text();
                window.location.href = '/booking?id_showtime='+ id_showtime + '&id_sever='+ id_sever;
            })
            .fail(function(data) {
                if (data.status == 400) {
                    $.each(data.responseJSON.errors, function(index, val) {
                        $('#error').html(val);
                    });
                }
                else{
                    $('#error').html(data.responseJSON.message);
                }
            });
        }
    });

    $.validator.addMethod(
      "validatePassword",
      function (value, element) {
        return value.match(/[^a-z0-9 ]/);
      },
      message.validatePassword
    );

    
    
    //checkbox for form guest
    $('#agree_term').on('click', function(){
        if($('#agree_term').prop("checked")){
            $('.form-popup button').prop('disabled', false);
        }else{
            $('.form-popup button').prop('disabled', true);
        }
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
