$(document).ready(function() {
    // validate phone only number
    var selectorPhone = $("#contactForm input[name=phone]");
    // Call back validOnlyNumber layout.js 
    validOnlyNumber(selectorPhone, '');

    // Submit form check validate captcha
    $('#contactForm').on('submit', function(e) {
        var res = grecaptcha.getResponse(widId);

        if (res == "" || res == undefined || res.length == 0){
            e.preventDefault();
            $('.captcha-error').text("Vui lòng xác nhận captcha");
            return false;
        }
        //recaptcha passed validation 
        return true;
    });

    $("#contactForm").validate({
        rules: {
            name: { 
                required: true,
            },
            email:{
                required: true,
                email: true
            },
            phone:{
                required: true,
                rangelength:[10, 11],
                number: true
            },
            message:{
                required: true,
            }
        },
        messages:{
            name: {
                required: "Vui lòng nhập tên",
            },
            email: {
                required: "Vui lòng nhập email",
                email: "Email không hợp lệ"
            },
            phone: {
                required: "Vui lòng nhập số điện thoại",
                rangelength: "Số điện thoại không hợp lệ",
                number: "Vui lòng chỉ nhập chữ số"
            },
            message: {
                required: "Vui lòng nhập nội dung",
            }
        }
    });
});

// load recaptcha 
var widId = "";
// device IOS
var isIOS = navigator.userAgent.match(/(\(iPod|\(iPhone|\(iPad)/);
// scroll to form conactForm
var focusWhatever = function (response) {
    // check device
    if(isIOS){
        $("html, body").animate({ scrollTop: $("#contactForm").offset().top }, "slow");
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