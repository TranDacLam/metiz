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