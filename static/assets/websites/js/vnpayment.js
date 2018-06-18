var validNavigation = false;

// function endSession() {
//     // Call server clear session
//     var working_id = $("#working_id").val();
//     var id_server = $('.vnpayment #payment_form input[name=id_server]').val();
//     $.ajax({
//         url: "clear/seats",
//         type: 'POST',
//         data: {
//             "working_id": working_id,
//             "id_server": id_server
//         },
//         dataType: 'json',
//         crossDomain:false,
//         context: this,
//         async: false
//     });
// }


$(document).ready(function() {
    // detect redirect page only ecept button submit form and change showtime
    // $('body a').click(function(evt){    
    //    if(evt.target.id == "btn-payment-seats" || $(evt.target).hasClass("open-popup-link") || $(evt.target).hasClass("popup-movie-schedule") || evt.target.id == "id-menu-member" || evt.target.id == "id-menu-movie"){
    //       return;
    //    }else{
    //         endSession();
    //    }
        
    // });

    // window.onload = function () {
    //     if (typeof history.pushState === "function") {
    //         history.pushState("loadpage", null, null);
    //         window.onpopstate = function () {
    //             history.pushState('new_loadpage', null, null);
    //             // Handle the back (or forward) buttons here
    //             // Will NOT handle refresh, use onbeforeunload for this.
    //             endSession();
    //             var id_showtime = $('#payment_form input[name=id_showtime]').val();
    //             var id_server = $('#payment_form input[name=id_server]').val();
    //             var movie_api_id = $('#payment_form input[name=movie_api_id]').val();
    //             var id_movie_name = $('#payment_form input[name=id_movie_name]').val();
    //             var id_movie_time = $('#payment_form input[name=id_movie_time]').val();
    //             var id_movie_date_active = getDate($('#payment_form input[name=id_movie_date_active]').val());

    //             window.location.href = '/booking?id_showtime='+ id_showtime + '&id_server='+ id_server
    //                         + '&id_movie_name='+ id_movie_name + '&id_movie_time='+ id_movie_time
    //                         + '&id_movie_date_active='+ id_movie_date_active + '&movie_api_id='+ movie_api_id;
    //         };
    //     }
    // }

    // Submit form check validate captcha
    $('#payment_form').on('submit', function(e) {
        var res = grecaptcha.getResponse(widId);

        if (res == "" || res == undefined || res.length == 0){
            e.preventDefault();
            $('.captcha-error').text("Vui lòng xác nhận captcha");
            return false;
        }
        //recaptcha passed validation 
        return true;
    });

    // validate form
    var val_required = 'Trường này là bắt buộc';
    $("#payment_form").validate({
        rules: {
            amount: { 
                required: true,
            },
            bank_code: { 
                required: true,
            },
            order_id: {
                required: true,
            }
        },
        messages:{
            amount: {
                required: val_required,
            },
            bank_code: {
                required: val_required,
            },
            order_id: {
                required: val_required,
            }
        }
    });

    // setTimeOut 5 minutes will redirect page timeout/booking
    setTimeout(function(){
        // endSession();
        window.location.href = '/timeout/?key_query=payment';
    }, 600000);

    // format money
    var money_total = $('#payment_form input[name=amount-text]').val();
    $('#payment_form input[name=amount-text]').val(money_total.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1."));

    // Format date
    function getDate(date_shedule){
        return date_shedule.replace(/([0-9]{2})\-([0-9]{2})\-([0-9]{4})/g, '$3-$2-$1');
    }
});

// load recaptcha 
var widId = "";
// device IOS
var isIOS = navigator.userAgent.match(/(\(iPod|\(iPhone|\(iPad)/);
// scroll to form conactForm
var focusWhatever = function (response) {
    // check device
    if(isIOS){
        $("html, body").animate({ scrollTop: $("#payment_form").offset().top }, "slow");
    }
};

// on load captcha
var onloadCallback = function ()
{
    widId = grecaptcha.render('re-captcha', {
        'sitekey': recaptchaKey,
        'theme': "light",
        'callback' : focusWhatever
    });
};