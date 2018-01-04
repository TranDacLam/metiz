$(document).ready(function() {
    $('.msg-result, .msg-result-js').fadeIn().delay(4000).fadeOut('slow');
});

// message result on js
function msgResult(message, type){
    return '<ul class="messages msg-result">'
                +'<li>'
                   +' <button type="button" class="btn btn-'+ type +'">'
                        +'<span class="badge"><i class="fa fa-exclamation-triangle"></i></span> '
                        + message
                   +'</button>'
                +'</li>'
                +'button'
            +'</ul>';
}

function displayMsg(){
    $('.msg-result-js').css({'display': 'block'});
    setTimeout(function() {
        $('.msg-result-js').fadeOut('slow');
    }, 4000);
}