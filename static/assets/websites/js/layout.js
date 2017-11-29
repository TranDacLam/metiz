$(document).ready(function() {
    // handle double click submit 
    $("form").submit(function() {
        // submit more than once return false
        $(this).submit(function() {
            if(!$(this).valid()){
                return false;    
            }
            
        });
        // submit once return true
        return true;    
    });

    // Submit form check captcha
    $('#contactForm, #payment_form, #signup_form').on('submit', function(e) {
        if(grecaptcha.getResponse() == "") {
            e.preventDefault();
            $('.captcha-error').text("Vui lòng xác nhận captcha");
            return false;
        }
        //recaptcha passed validation 
        return true;
    });
});

// Valid only number input
function validOnlyNumber(selector, prevVal){
    selector.on("input", function (evt) {
        var self = $(this);
        // check value input only number
        if (self.val().match(/^-?\d*(\.(?=\d*)\d*)?$/) !== null) {
            prevVal = self.val()
        } else {
            // not number return value before
            self.val(prevVal);
        }
    });
}