$(document).ready(function() {
    
    //close popup by esc key
    $("body").on("keyup", function(e){
        var key = e.which;
        if (key == 27){
            e.preventDefault();
            if($('#modal-popup .modal').hasClass('in')){
                $('#modal-popup .modal').modal('hide');
            }
            else{
                $.magnificPopup.close();
            }
        } 
    });

    //fix bug input element in modals 
    if( navigator.userAgent.match(/iPhone|iPad|iPod/i) || navigator.userAgent.match(/Android/i)){
        $('#myModal').on('shown.bs.modal', function () {
            $('body').css('overflow','hidden');
        })
    }

    // Validate guest_form, update_form
    // Validate and handle member_form by ajax
    
    // message for validate form
    var lang = $('html').attr('lang');
    if ( lang == 'vi') {
        message = {'required': 'Trường này bắt buộc', 
        'phone': 'Số điện thoại không hợp lệ',
        'minlength_2' :'Nhập ít nhất 2 kí tự', 
        'minlength_6' :'Nhập ít nhất 6 kí tự',
        'minlength_8' :'Nhập ít nhất 8 kí tự',
        'email': 'Email không hợp lệ',
        'number': 'Nhập các chữ số',
        'equalTo': 'Mật khẩu không khớp. Vui lòng nhập lại',
        'validatePassword': 'Mật khẩu chứa ít nhất 8 ký tự, bao gồm chữ, số và ký tự hoa hoặc ký tự đặc biệt.',
        'validateDate': 'Nhập ngày theo định dạng dd-mm-yyyy',}
    } else {
        message = {'required': 'This field is required', 
        'phone': 'Invalid telephone number',
        'minlength_2' :'Please enter at least 2 characters', 
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
                    minlength: 2
                },
                email:{
                    email: true
                },
                phone:{
                    required: true,
                    validatePhone: true,
                },
            },
            messages:{
                name:{
                    required: message.required,
                    minlength: message.minlength_2
                },
                email:{
                    email: message.email
                },
                phone:{
                    required: message.required,
                    validatePhone: message.phone,
                }
            }
        });
    }
    $('.form-popup').each(function(index, el) { 
        validateForm($(this)); 
    });

    // validate and handle member form
    $('#member_form').validate({
        rules:{
            email:{
                required: true,
                email: true
            },
            password:{
                required: true,
                minlength: 8,
                regex: true
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
            $.ajax({
                url: '/login/',
                type: 'POST',
                dataType: 'json',
                data: $(form).serialize() + "&is_popup_schedule=1",
            })
            .done(function(data) {
                // Get value member form
                var id_showtime = $('#member_form input[name=id_showtime]').val();
                var id_sever = $('#member_form input[name=id_sever]').val();
                var id_movie_name = $('#member_form input[name=id_movie_name]').val();
                var id_movie_time = $('#member_form input[name=id_movie_time]').val();
                var id_movie_date_active = $('#member_form input[name=id_movie_date_active]').val();

                window.location.href = '/booking?id_showtime='+ id_showtime + '&id_sever='+ id_sever
                            + '&id_movie_name='+ id_movie_name + '&id_movie_time='+ id_movie_time
                            + '&id_movie_date_active='+ id_movie_date_active;
            })
            .fail(function(data) {
                if (data.responseJSON.code == 400) {
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

     // validate password
    $.validator.addMethod(
        "regex",
         function(value, element) {
            return this.optional(element) || (value.match(/[a-z]/) && value.match(/[!@#$%^&*()_+A-Z]/) && value.match(/[0-9]/));
        },
        message.validatePassword
    );

     $.validator.addMethod(
      "validatePhone",
      function (value, element) {
        // put your own logic here, this is just a (crappy) example 
        return value.match(/^(01[2689]|09|[0-9]|[0-9]{2})[0-9]{8}$/);
      },
      message.phone
    );
    // active popup
    $('.open-popup-link').magnificPopup({
        type: 'inline',
        midClick: true,
        enableEscapeKey: false,
       
    });
    
   
    // *** POPUP MOVIE SCHEDULE ***
    // Get list movie, show time
    // * Step 1:
    // - TH1: Click Lịch chiếu (header) or Đổi xuất chiếu (page Booking)
    // --- Set movie_api_id = null -> let get list movie
    // - TH2: Click đặt vé a movie
    // --- get movie_api_id movie selected -> let get a movie selected
    // * Step 2:
    // - TH1: Click Lịch chiếu (header)
    // --- get date_query = date current
    // - TH2: Click Đổi xuất chiếu (page Booking)
    // --- get data-date-seat, get date schedule user selected
    // --- Show popup movie schedule date selected
    // - TH3: Click đặt vé a movie
    // --- get movie-api-id movie selected
    // * Step 3:
    // - function listShedule: list show time of 1 movie
    // - function listFilm: list movie of date selected
    
    
    // list show time of a movie, callback from function listFilm
    function listShedule(shedule){
        var htmlShedule = '';
        $.each(shedule.lst_times, function(key, value) {
            
            //set end time for film schedule
            var startTime = value.time.split(':').map( Number );
            var munite = (shedule.time_running + startTime[1])%60;
            var hour = startTime[0] + ((shedule.time_running + startTime[1] - munite)/60);
            if (munite < 10 ){
                munite = '0' + munite;
            }
            if (hour > 23){
                hour -= 24;
            }
            var endTime = '~' + hour + ':' + munite;

            htmlShedule +=  '<li class="sold-out">'
                                +'<a href="#" >'
                                    +'<input type="hidden" name="id_showtime" value="'+ value.id_showtime +'">'
                                    +'<input type="hidden" name="id_movie_name" value="'+ shedule.movie_name +'">'
                                    +'<span class="time">'
                                        + value.time +'<span class="time-end">'+endTime+'</span>'
                                    +'</span>'
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
                    +'<div class="lot-table clearfix" data-rated="'+ film.rated +'" >'
                        +'<ul class="list-inline list-unstyled theater_time">'
                            + listShedule(film)
                        +'</ul>'
                   +' </div>'
               +' </div>';
    } 


    var movie_api_id;

    $(document).on('click', '.popup-movie-schedule', function () {
        
                
        //set data for Month
        $('#center-month').text($(this).children('.hide-month').text());
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
                //set data for Month
                $('#center-month').text($('.days-popup li:first').children('.hide-month').text());
            }
        }
        
        // Call Ajax get movie show time with current date
        // cinema_id is equal id_server
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
                $('.list-schedule').html('<p class="empty-schedule">Ngày Bạn Chọn Hiện Không Có Lịch Chiếu Nào. Vui Lòng Chọn Ngày Khác.<p/>');
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
            var id_sever = $('.list-cinema .active').attr('data-id-server');
            
            $('.modal input[name=id_sever]').val(id_sever);
            $('.modal input[name=id_showtime]').val(id_showtime);
            $('.modal input[name=id_movie_name]').val(id_movie_name);
            $('.modal input[name=id_movie_time]').val(id_movie_time);
            $('.modal input[name=id_movie_date_active]').val($("li.active-date").attr("data-date-select"));
            
            //set content for modal #warnning or skip
            var rated = $(this).parents('.lot-table').attr('data-rated');
            if(rated != 'null'){
                $('#warning #content-warnning').text(rated);
                $('#warning').modal('show');
            }else{
                $('#btn-skip').click();
            }
        });
    }
    
    //checkbox for form guest
    $('#agree_term').on('click', function(){
        if($('#agree_term').prop("checked")){
            $('.form-popup button').prop('disabled', false);
        }else{
            $('.form-popup button').prop('disabled', true);
        }
    });
    
    //dont allow key e in input phone
    $("#modal-popup input[type=number]").on("keydown", function(e){
        return e.keyCode == 69 ? false : true;
    });
});

