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

    // Message updating Blog phim on Menu
    $('.blog-updating').on('click', function(){
        displayMsg();
        $('.msg-result-js').html(msgResult("Chức năng đang được cập nhật. Mời bạn quay lại vào lúc khác", "info"));
    });

    // If Browser is IE then remove placeholder
    if (GetIEVersion() > 0){
        $(':input').removeAttr('placeholder');
    }

    
});

// if browser is not IE then return 0 else return version number
function GetIEVersion() {
    var sAgent = window.navigator.userAgent;
    var Idx = sAgent.indexOf("MSIE");

    // If IE, return version number.
    if (Idx > 0) 
        return parseInt(sAgent.substring(Idx+ 5, sAgent.indexOf(".", Idx)));

    // If IE 11 then look for Updated user agent string.
    else if (!!navigator.userAgent.match(/Trident\/7\./)) 
        return 11;

    else
        return 0; //It is not IE
}

// Valid only number input
function validOnlyNumber(selector, prevVal){
    selector.on("input", function (evt) {
        var self = $(this);
        // check value input only number
        if (self.val().match(/^[0-9]*$/) !== null) {
            prevVal = self.val()
        } else {
            // not number return value before
            self.val(prevVal);
        }
    });
}

// Function validate phone number
// Remove 0 number before phone number 
    function removeBeforePhoneNumber(str) {
        if(typeof str !== 'undefined'){
            var trimmed = str.replace(/\b0+/g, "");
            return trimmed;
        }
    } 