$(document).ready(function() {
    // global variable save info film
    var info_film = null;
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
            // $("body").addClass("fixIOSposition");
            $.magnificPopup.close(); 
        });

        $('#confirm').on('hide.bs.modal', function() {
            // $("body").removeClass("fixIOSposition");
        });
    }
    $('.open-popup-link').magnificPopup({
        type: 'inline',
        midClick: true,
        enableEscapeKey: false,
        fixedContentPos: true,
        callbacks: {
            beforeOpen: function() {
                // Load data before popup open load first time
                getDataPopupMovieSchedule(this.st.el);
            },
            close: function() {
            }
        }
    });


    // Validate form
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
    $("#guest_form").validate({
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
        },
        submitHandler: function(form) {
            // event.preventDefault();
            // add info_film to form before submit
            for( var item in info_film){
                $(form).append($('<input>', {
                    type: 'hidden',
                    name: item,
                    value: info_film[item]}
                ));
            };
            form.submit();
        }
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
                    window.location.href = '/booking?id_showtime=' + info_film.id_showtime + '&id_server=' + info_film.id_server +
                        '&id_movie_name=' + info_film.id_movie_name + '&id_movie_time=' + info_film.id_movie_time +
                        '&id_movie_date_active=' + info_film.id_movie_date_active + '&movie_api_id=' + info_film.movie_api_id;
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
                '<a href="javascript:void(0);" >' +
                '<input type="hidden" name="id_showtime" value="' + value.id_showtime + '">' +
                '<input type="hidden" name="id_movie_id" value="' + shedule.movie_id + '">' +
                '<input type="hidden" name="id_movie_name" value="' + shedule.movie_name + '">' +
                '<input type="hidden" name="movie_api_id" value="' + shedule.movie_id + '">' +
                '<span class="time">' + value.time +'</span>' +
                '<span class="ppnum">Phòng chiếu</span>' +
                '<span class="ppnum">' + value.room_name + '</span>' // room chiếu phim
                +
                '<span class="pp-early" title="Suất chiều đầu"></span>' +
                '</a>' +
                '</li>';
            console.log("allow_booking: ", shedule.allow_booking);

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
    // TH1: Click Lịch chiếu
    // function for modal page and schedule page
    $(document).on('click', '.popup-movie-schedule', function() {
        getDataPopupMovieSchedule(this);
    })
    // Call server get data
    // Function for modal page and schedule page
    function getDataPopupMovieSchedule(element) {
        // get element parent to determine where show data
        parent = $(element).closest(".white-popup");
        //set data for Month
        $('#modal-popup #center-month').text($(element).children('.hide-month').text());
        $('#modal-popup .days-popup li').removeClass('active-date');
        var id_server = $('.list-cinema .active').attr('data-id-server');

        // Step 2:
        // - TH2: Click Đổi xuất chiếu (page Booking)
        // get date time at page booking 
        if ($(element).attr("data-date-seat")) {
            var date_seat = $(element).attr("data-date-seat");
            $('#modal-popup .days-popup [data-date-select = ' + date_seat + ']').addClass('active-date');
            var date_query = date_seat;
            // get movie api id from booking
            var get_movie_api = $('.booking-details #movie_api_id').val();
            //set data for Month
            $('#modal-popup #center-month').text($('.days-popup li.active-date').children('.hide-month').text());
        } else {
            // - TH3: Click đặt vé a movie
            // get date time on page popup
            if ($(element).attr("data-date-select")) {
                var date_query = $(element).attr("data-date-select");
                $(element).addClass('active-date');
            } else {
                // TH1: Click Lịch chiếu (header)
                parent = $("#modal-popup");
                var date_query = new Date().toJSON().slice(0, 10).replace(/-/g, '-');
                $('#modal-popup .days-popup li:first').addClass('active-date');
                //set data for Month
                $('#modal-popup #center-month').text($('#modal-popup .days-popup li:first').children('.hide-month').text());
            }
        }

        // Call Ajax get movie show time with current date
        // cinema_id is equal id_server
        data = {
            "date": date_query,
            "cinema_id": id_server
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
                    // check movie id is movie id test
                    if (document.domain !== "metiz.vn" || movieIdTest !== value.movie_id ) {
                        html += listFilm(value);
                    }
                }
            });
            $(parent).find('.list-schedule').html(html);
            trigger_click_showtime(parent);
            if ( $(parent).find('.list-schedule').text() == '') {
                $(parent).find('.list-schedule').html('<p class="empty-schedule">Ngày Bạn Chọn Hiện Không Có Lịch Chiếu Nào. Vui Lòng Chọn Ngày Khác.<p/>');
            }
        })
        .fail(function() {
            displayMsg();
            $('.msg-result-js').html(msgResult("Error schedule film!", "danger"));
        });

    }
    // Function for modal page and schedule page
    function trigger_click_showtime(parent) {
        /* hardcode for film free for vouchers */
        function check_movie_free(element) {
            /* List Film Free */
            var lst_movie_id_free = ['3d3e64f6-a6b6-42fa-8b47-405844e37516', '160809e0-6d8c-422d-888f-7d9253fc2490', '9a95f59b-acdf-4c13-a454-8cf5df170580'];
            // Get movie id selected
            var movie_id = element.children('input[name=id_movie_id]').val();
        
            if ($.inArray(movie_id, lst_movie_id_free) > -1){
                return true;
            }
            return false;
        }

        // Validate Time Remain before 15 minutes. verify when date selected equal current date
        // function for modal page and schedule page
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
        function get_info_film(element){
            var id_showtime = element.children('input[name=id_showtime]').val();
            var id_movie_name = element.children('input[name=id_movie_name]').val();
            var movie_api_id = element.children('input[name=movie_api_id]').val();
            var id_movie_time = element.children('span[class=time]').text();
            var id_server = $('.list-cinema .active').attr('data-id-server');
            var id_movie_date_active = $("li.active-date").attr("data-date-select");
            return {'id_showtime': id_showtime,
            'id_movie_name': id_movie_name,
            'movie_api_id': movie_api_id,
            'id_movie_time': id_movie_time,
            'id_server': id_server,
            'id_movie_date_active': id_movie_date_active};
            
        }

        // Show popup warning or confirm
        function showPopup(element){
            info_film = get_info_film(element);
            console.log('popup ',info_film);
            //set content for modal #warnning or skip
            var rated = element.parents('.lot-table').attr('data-rated');
            $('#confirm').on('show.bs.modal', function() {
                $('#confirm').css("overflow-y","auto");
                // remove tabindex of magnifix popup trigger for input confirm form
                $(".mfp-ready").removeAttr("tabindex");
                $(".mfp-ready").css("overflow-y","hidden");
                if (navigator.userAgent.match(/iPhone|iPod|iPad|Android|Windows Phone|BlackBerry/i)) {

                    // add attr autocomplete for every input
                    // *** BUG *** : show suggest when focus input, suggest moving when scroll
                    $('#confirm input').attr('autocomplete', 'off');

                    // set scroll to tocuh
                    $("#confirm").css("-webkit-overflow-scrolling", "touch !important");
                }
            });

            // Set attr style when hide modal confirm
            $('#confirm').on('hide.bs.modal', function() {
                $(".mfp-ready").attr("style","overflow-x: hidden; overflow-y: auto;");
            });
            // Show popup warning or confirm
            if (rated == 'null' || rated == 'p'|| rated == 'P') {
                $('#confirm').modal('show');
            } else {
                content = JSON.parse($('#rated').text());
                $('#warning #content-warnning').text(content[rated]);
                $('#warning').modal('show');
            }
        }
        // TH2: Click đặt vé a movie
        /* change background for schedule firm on mobile */
        if (navigator.userAgent.match(/iPhone|iPod|iPad|Android|Windows Phone|BlackBerry/i)) {
            $('.sold-out a').on('click', function(event) {
                $(this).addClass('mobile-schedule');
                if(check_movie_free($(this)) == false && validate_time_remain($(this), '#modal-popup')){
                    showPopup($(this));
                }
            });
            $('.modal-schedule').on('hide.bs.modal', function() {
                $('.sold-out a').removeClass('mobile-schedule');

            });
        }else{
            // on web
            $('.sold-out a').click(function(event) {
                console.log($(parent).attr('id'));
                event.preventDefault();
                if(check_movie_free($(this)) == false && validate_time_remain($(this), '#modal-popup')){
                    showPopup($(this));
                }
                
            });
        }
        
    }
    
    //checkbox for form guest
    $('#agree_term').on('click', function() {
        if ($('#agree_term').prop("checked")) {
            $('#confirm .form-popup #submit').prop('disabled', false);
        } else {
            $('#confirm .form-popup #submit').prop('disabled', true);
        }
    });

    //dont allow key e in input phone
    $("#modal-popup input[type=number]").on("keydown", function(e) {
        return e.keyCode == 69 ? false : true;
    });
});