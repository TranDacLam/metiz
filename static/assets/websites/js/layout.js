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
    // If Browser is IE then remove placeholder
    if (GetIEVersion() > 0){
        $(':input').removeAttr('placeholder');
        $(':textarea').removeAttr('placeholder');
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

// Convert date and startTime to Jquery DateTime
function convertStringToDate(date, start_time){
    var date_arr = date.split("/");
    var month = date_arr[1];
    if (month > 1){
        month = month - 1 ;
    }
    var date_time_movie_start = new Date(date_arr[2], month, date_arr[0], start_time[0], start_time[1]);
    return date_time_movie_start;
}