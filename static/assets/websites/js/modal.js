$(document).ready(function() {

    //close popup by esc key
    $("body").on("keyup", function(e) {
        var key = e.which;
        if (key == 27) {
            e.preventDefault();
            if ($('.modal-schedule').hasClass('in')) {
                $('.modal-schedule').modal('hide');
            } else {
                $.magnificPopup.close();
            }
        }
    });

    //fix background scroll in modals on mobile
    if (navigator.userAgent.match(/iPhone|iPod|iPad|Android|Windows Phone|BlackBerry/i)) {
        $('#confirm').on('show.bs.modal', function() {
            $("body").addClass("fixIOSposition");
            $.magnificPopup.close(); 
        });

        $('#confirm').on('hide.bs.modal', function() {
            $("body").removeClass("fixIOSposition");
        });
    }
    $('.open-popup-link').magnificPopup({
        type: 'inline',
        midClick: true,
        enableEscapeKey: false,
        fixedContentPos: true,
    });


    // Validate guest_form, update_form
    // Validate and handle member_form by ajax

    // message for validate form
    var lang = $('html').attr('lang');
    if (lang == 'vi') {
        message = {
            'required': 'Trường này bắt buộc',
            'phone': 'Số điện thoại không hợp lệ',
            'minlength_2': 'Nhập ít nhất 2 kí tự',
            'minlength_6': 'Nhập ít nhất 6 kí tự',
            'minlength_8': 'Mật khẩu chứa ít nhất 8 ký tự, bao gồm chữ, số và ký tự hoa hoặc ký tự đặc biệt.',
            'email': 'Email không hợp lệ',
            'rangelength_1_70': 'Họ và tên chứa ít nhất 1 kí tự và nhiều nhất 70 kí tự',
            'number': 'Vui lòng chỉ nhập các chữ số',
            'equalTo': 'Mật khẩu không khớp. Vui lòng nhập lại',
            'validatePassword': 'Mật khẩu chứa ít nhất 8 ký tự, bao gồm chữ, số và ký tự hoa hoặc ký tự đặc biệt.',
            'validateDate': 'Nhập ngày theo định dạng dd-mm-yyyy',
        }
    } else {
        message = {
            'required': 'This field is required',
            'phone': 'Invalid telephone number',
            'minlength_2': 'Please enter at least 2 characters',
            'minlength_6': 'Please enter at least 6 characters',
            'minlength_8': 'Please enter at least 8 characters',
            'email': 'Please enter a valid email address',
            'rangelength_1_70': 'Please enter a value between 1 and 70 characters long',
            'number': 'Please enter a valid number',
            'equalTo': "Password don't same. Please enter again",
            'validatePassword': 'Passwords must contain characters, numbers and at least 1 special character',
            'validateDate': 'Please enter a date in the format dd-mm-yyyy'
        }
    }

    // Can enter 0 number at the end or middle but not at the beginning.
    // Check the first characters and remove if it equal == 0
    // Then replace input with new value
    // use modal, profile, register
    
    //Prevent to enter 0(zero) number at the second character
    $('.textPhone').on('keydown',function(event){
        var caretPos = this.selectionStart;
        var keyCode = event.which || event.keyCode;
        var isZero = keyCode == 48 || keyCode == 96;
        var valPhone = $(this).val();
        if (caretPos < 2 && valPhone.startsWith("0") && isZero) {
            return false;
        } 
    });
    // Call event Paste 
     $('.textPhone').bind('paste', function(e) {
        var pasteText = e.originalEvent.clipboardData.getData('Text');
        $(this).val(removeBeforePhoneNumber(pasteText)); 
        return false;
    });
    $('.textPhone').on('blur',function(event){ 
        var valPhone = $(this).val();
        $(this).val(removeBeforePhoneNumber(valPhone));
    });

    
    // validate phone only number
    // Form Update modal schedule
    var selectorPhone_update_form = $("#update_form input[name=phone]");
    // Form Guest modal schedule
    var selectorPhone_guest_form = $("#guest_form input[name=phone]");
    // Call back validOnlyNumber layout.js 
    validOnlyNumber(selectorPhone_update_form, selectorPhone_update_form.val());
    validOnlyNumber(selectorPhone_guest_form, selectorPhone_guest_form.val());

    //validate guest form, update form
    function validateForm(form) {
        $(form).validate({
            rules: {
                name: {
                    required: true,
                    rangelength: [1, 70],
                },
                email: {
                    email:{
                        depends:function(){
                            $(this).val($.trim($(this).val()));
                            return true;
                        }
                    },
                },
                phone: {
                    required: true,
                    validatePhone: true,
                    number: true,
                    minlength: 9,
                },
            },
            messages: {
                name: {
                    required: message.required,
                    rangelength: message.rangelength_1_70,
                },
                email: {
                    email: message.email
                },
                phone: {
                    required: message.required,
                    validatePhone: message.phone,
                    number: message.number,
                    minlength: message.phone,
                }
            }
        });
    }
    $('.form-popup').each(function(index, el) {
        validateForm($(this));
    });

    // validate and handle member form
    $('#member_form').validate({
        rules: {
            email: {
                required: {
                    depends:function(){
                        $(this).val($.trim($(this).val()));
                        return true;
                    }
                },
                email: true
            },
            password: {
                required: true,
                minlength: 8,
                regex: true
            },
        },
        messages: {
            email: {
                required: message.required,
                email: message.email
            },
            password: {
                required: message.required,
                minlength: message.validatePassword,
            }
        },
        submitHandler: function(form) {
            $.ajax({
                    url: '/login/',
                    type: 'POST',
                    dataType: 'json',
                    data: $(form).serialize() + "&is_popup_schedule=1",
                })
                .done(function(data) {
                    // Get value member form
                    var id_showtime = $('#member_form input[name=id_showtime]').val();
                    var id_server = $('#member_form input[name=id_server]').val();
                    var movie_api_id = $('#member_form input[name=movie_api_id]').val();
                    var id_movie_name = $('#member_form input[name=id_movie_name]').val();
                    var id_movie_time = $('#member_form input[name=id_movie_time]').val();
                    var id_movie_date_active = $('#member_form input[name=id_movie_date_active]').val();

                    window.location.href = '/booking?id_showtime=' + id_showtime + '&id_server=' + id_server +
                        '&id_movie_name=' + id_movie_name + '&id_movie_time=' + id_movie_time +
                        '&id_movie_date_active=' + id_movie_date_active + '&movie_api_id=' + movie_api_id;
                })
                .fail(function(data) {
                    if (data.responseJSON.code == 400) {
                        $.each(data.responseJSON.errors, function(index, val) {
                            $('#error').html(val);
                        });
                    } else {
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

    // use for modal, signup, profile
    $.validator.addMethod(
        "validatePhone",
        function(value, element) {
            // put your own logic here, this is just a (crappy) example 
            return value.match(/^(01[2689]|09|[0-9]|[0-9]{2})[0-9]{8}$/);
        },
        message.phone
    );
    


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
    function listShedule(shedule) {
        var htmlShedule = '';
        $.each(shedule.lst_times, function(key, value) {

            //set end time for film schedule
            var startTime = value.time.split(':').map(Number);
            var minute = (shedule.time_running + startTime[1]) % 60;
            var hour = startTime[0] + Math.floor((shedule.time_running + startTime[1]) / 60);
            if (minute < 10) {
                minute = '0' + minute;
            }
            if (hour > 23) {
                hour -= 24;
            }
            var endTime = '~' + hour + ':' + minute;
            htmlShedule += '<li class="sold-out">' +
                '<a href="#" >' +
                '<input type="hidden" name="id_showtime" value="' + value.id_showtime + '">' +
                '<input type="hidden" name="id_movie_name" value="' + shedule.movie_name + '">' +
                '<input type="hidden" name="movie_api_id" value="' + movie_api_id + '">' +
                '<span class="time">' +
                value.time + '<span class="time-end">' + endTime + '</span>' +
                '</span>' +
                '<span class="ppnum">Phòng chiếu</span>' +
                '<span class="ppnum">' + value.room_name + '</span>' // room chiếu phim
                +
                '<span class="pp-early" title="Suất chiều đầu"></span>' +
                '</a>' +
                '</li>';


        });
        return htmlShedule;
    }

    // list movie 
    function listFilm(film) {
        return '<div class="movie-time-line-box clearfix" data-control="movie-code">' +
            '<h3 class="movie-name">' + film.movie_name + '</h3>' +
            '<div class="lot-table clearfix" data-rated="' + film.rated + '" >' +
            '<ul class="list-inline list-unstyled theater_time">' +
            listShedule(film) +
            '</ul>' +
            ' </div>' +
            ' </div>';
    }


    var movie_api_id;

    $(document).on('click', '.popup-movie-schedule', function() {

        //set data for Month
        $('#center-month').text($(this).children('.hide-month').text());
        $('.days-popup li').removeClass('active-date');

        var id_server = $('.list-cinema .active').attr('data-id-server');

        // get movie api id at booking ticket every film
        if ($(this).attr("data-movie-api-id")) {
            movie_api_id = $(this).attr("data-movie-api-id");
        }

        if ($(this).attr("data-all-movie")) {
            movie_api_id = null;
        }

        // get date time at page booking 
        if ($(this).attr("data-date-seat")) {
            var date_seat = $(this).attr("data-date-seat");
            $('.days-popup [data-date-select = ' + date_seat + ']').addClass('active-date');
            var date_query = date_seat;
            // get movie api id from booking
            var get_movie_api = $('.booking-details #movie_api_id').val();
            movie_api_id = null;
            if(get_movie_api != 'null' && get_movie_api != 'undefined'){
                movie_api_id = $('.booking-details #movie_api_id').val()
            }
            //set data for Month
            $('#center-month').text($('.days-popup li.active-date').children('.hide-month').text());
        } else {
            // get date time on page popup
            if ($(this).attr("data-date-select")) {
                var date_query = $(this).attr("data-date-select");
                $(this).addClass('active-date');
            } else {
                var date_query = new Date().toJSON().slice(0, 10).replace(/-/g, '-');
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
            "cinema_id": id_server // get cinema_id from hidden field in popup movie schedule
        }


        $.ajax({
                url: "/movie/show/times",
                type: 'get',
                data: data,
                dataType: 'json',
                crossDomain: false,
                context: this,
            })
            .done(function(response) {
                var html = '';
                $.each(response, function(key, value) {
                    if (value.lst_times.length > 0) {
                        html += listFilm(value);
                    }
                });
                $('.list-schedule').html(html);
                trigger_click_showtime();
                if ($('.list-schedule').text() == '') {
                    $('.list-schedule').html('<p class="empty-schedule">Ngày Bạn Chọn Hiện Không Có Lịch Chiếu Nào. Vui Lòng Chọn Ngày Khác.<p/>');
                }

            })
            .fail(function() {
                displayMsg();
                $('.msg-result-js').html(msgResult("Error schedule film!", "danger"));
            });
    });
    function trigger_click_showtime() {
        // Validate Time Remain before 15 minutes. verify when date selected equal current date
        function validate_time_remain(element){
            var time_remain = 15;
            var date_now = new Date();
            // get current date selected and time of movie show
            var date_selected = new Date($('.popup-movie-schedule.active-date').attr('data-date-select'));
            var start_time = element.children('.time').text().split('~')[0];
            
            // get show time sub 15 minute check show time greate than equal curren time then allow booking
            var time_show = (start_time.split(":")[0] * 60 + parseInt(start_time.split(":")[1])) - time_remain;
            var current_time = date_now.getHours() * 60 + date_now.getMinutes() ;
            
            if(new Date().setHours(0,0,0,0) < date_selected.setHours(0,0,0,0) || time_show >= current_time){
                return true;
            }
            return false;
        }

        function showPopup(element){

            var id_showtime = element.children('input[name=id_showtime]').val();
            var id_movie_name = element.children('input[name=id_movie_name]').val();
            var movie_api_id = element.children('input[name=movie_api_id]').val();
            var id_movie_time = element.children('span[class=time]').text();
            var id_server = $('.list-cinema .active').attr('data-id-server');

            $('.modal input[name=id_server]').val(id_server);
            $('.modal input[name=id_showtime]').val(id_showtime);
            $('.modal input[name=movie_api_id]').val(movie_api_id);
            $('.modal input[name=id_movie_name]').val(id_movie_name);
            $('.modal input[name=id_movie_time]').val(id_movie_time);
            $('.modal input[name=id_movie_date_active]').val($("li.active-date").attr("data-date-select"));

            //set content for modal #warnning or skip
            var rated = element.parents('.lot-table').attr('data-rated');
            $('#confirm').on('show.bs.modal', function() {
                $('#confirm').css("overflow-y","auto");
                // remove tabindex of magnifix popup trigger for input confirm form
                $(".mfp-ready").removeAttr("tabindex");
                $(".mfp-ready").css("overflow-y","hidden");
                if (navigator.userAgent.match(/iPhone|iPod|iPad|Android|Windows Phone|BlackBerry/i)) {
                // When device focus input set overflow hidden using fix focus moving
                    $('#confirm input').on("focus", function(){
                        $('#confirm').css("position", "fixed");
                        $("#confirm").css("overflow", "hidden");    
                    });

                    // when input out focus then accept user scroll popup
                    $('#confirm input').on("focusout", function(){
                        $("#confirm").css("overflow", "auto");    
                    });
                    // set scroll to tocuh
                    $("#confirm").css("-webkit-overflow-scrolling", "touch !important");
                }
            });

            // Set attr style when hide modal confirm
            $('#confirm').on('hide.bs.modal', function() {
                $(".mfp-ready").attr("style","overflow-x: hidden; overflow-y: auto;");
            });

            // ingore null or p
            if (rated == 'null' || rated == 'p') {
                $('#confirm').modal('show');
            } else {
                content = JSON.parse($('#rated').text());
                $('#warning #content-warnning').text(content[rated]);
                $('#warning').modal('show');
            }
        }

        /* change background for schedule firm on mobile */
        if (navigator.userAgent.match(/iPhone|iPod|iPad|Android|Windows Phone|BlackBerry/i)) {
            $('.sold-out a').on('click', function(event) {
                $(this).addClass('mobile-schedule');
                if(validate_time_remain($(this))){
                    showPopup($(this));
                }
            });
            $('.modal-schedule').on('hide.bs.modal', function() {
                $('.sold-out a').removeClass('mobile-schedule');

            });
            $('.modal-schedule').on('hide.bs.modal', function() {
                $('.sold-out a').removeClass('mobile-schedule');

            });
        }else{
            $('.sold-out a').click(function(event) {
                event.preventDefault();
                if(validate_time_remain($(this))){
                    showPopup($(this));    
                }
                
            });
        }
        
    }
    
    
    //checkbox for form guest
    $('#agree_term').on('click', function() {
        if ($('#agree_term').prop("checked")) {
            $('.form-popup button').prop('disabled', false);
        } else {
            $('.form-popup button').prop('disabled', true);
        }
    });

    //dont allow key e in input phone
    $("#modal-popup input[type=number]").on("keydown", function(e) {
        return e.keyCode == 69 ? false : true;
    });


});