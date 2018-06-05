$(document).ready(function() {

    // global variable save info film
    var info_film_schedule = null;

    
    // validate phone only number
    // Form Guest modal schedule
    var selectorPhone_guest_form = $("#guest_form_schedule input[name=phone]");
    // Call back validOnlyNumber layout.js 
    validOnlyNumber(selectorPhone_guest_form, selectorPhone_guest_form.val());

    //validate guest form, update form
    $("#guest_form_schedule").validate({
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
        submitHandler: function(form, event) {
            event.preventDefault();
            // add info_film_schedule to form before submit
            for( var item in info_film_schedule){
                $(form).append($('<input>', {
                    type: 'hidden',
                    name: item,
                    value: info_film_schedule[item]}
                ));
            }
            form.submit();
        }
    });
    // validate and handle member form
    $('#member_form_schedule').validate({
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
                    window.location.href = '/booking?id_showtime=' + info_film_schedule.id_showtime + '&id_server=' + info_film_schedule.id_server +
                        '&id_movie_name=' + info_film_schedule.id_movie_name + '&id_movie_time=' + info_film_schedule.id_movie_time +
                        '&id_movie_date_active=' + info_film_schedule.id_movie_date_active + '&movie_api_id=' + info_film_schedule.movie_api_id;
                })
                .fail(function(data) {
                    if (data.responseJSON.code == 400) {
                        $.each(data.responseJSON.errors, function(index, val) {
                            $('#member_form_schedule #error').html(val);
                        });
                    } else {
                        $('#member_form_schedule #error').html(data.responseJSON.message);
                    }
                });
        }
    });



    // *** MOVIE SCHEDULE ***
    // inherit getDataPopupMovieSchedule function in model.js
    // Get list movie, show time
    // - TH1: Click show schedule (on header)
    // --- auto click first day
    // - TH2: Click day ( on date show )
    // --- chang month, addClass active-date


    // - TH2: Click day ( on date show )
    $(document).on('click', '#schedule-film .popup-movie-schedule', function() {
        getDataMovieSchedule(this);
    })

    // Call server get data
    function getDataMovieSchedule(element) {

        //set data for Month
        $('#schedule-film #center-month').text($(element).children('.hide-month').text());
        $('#schedule-film .days-popup li').removeClass('active-date');

        var id_server = $('#schedule-film .list-cinema .active').attr('data-id-server');
        $(element).addClass('active-date');
    }
    // TH1: Click show time (on header)
    $('#schedule-film .days-popup li:first').click();
        

    //dont allow key e in input phone
    $("#schedule-film input[type=number]").on("keydown", function(e) {
        return e.keyCode == 69 ? false : true;
    });
});