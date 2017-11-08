var validNavigation = false;

function endSession() {
// Browser or broswer tab is closed
// Do sth here ...
    var working_id = $("#working_id").val();
    var id_server = $('.vnpayment #create_form input[name=id_server]').val();
    $.ajax({
        url: "clear/seats",
        type: 'POST',
        data: {
            "working_id": working_id,
            "id_server": id_server
        },
        dataType: 'json',
        crossDomain:false,
        context: this,
        async: false
    });
}

function wireUpEvents() {
/*
* For a list of events that triggers onbeforeunload on IE
* check http://msdn.microsoft.com/en-us/library/ms536907(VS.85).aspx
*/
    
    window.onbeforeunload = function() {
        if (!validNavigation) { 
            endSession();
            window.setTimeout(function () { 
                window.location.href = "/timeout/booking";
            }, 0); 
            window.onbeforeunload = null; // necessary to prevent infinite loop, that kills your browser 
        }
    }

 // Attach the event submit for all forms in the page
     $("form").bind("submit", function() {
        validNavigation = true;
     });

 // Attach the event click for all inputs in the page
     $("input[type=submit]").bind("click", function() {
        validNavigation = true;
     });
}


$(document).ready(function() {
    window.onload = function () {
        if (typeof history.pushState === "function") {
            history.pushState("loadpage", null, null);
            window.onpopstate = function () {
                history.pushState('new_loadpage', null, null);
                // Handle the back (or forward) buttons here
                // Will NOT handle refresh, use onbeforeunload for this.
                var id_showtime = $('#member_form input[name=id_showtime]').val();
                var id_sever = $('#member_form input[name=id_sever]').val();
                var id_movie_name = $('#member_form input[name=id_movie_name]').val();
                var id_movie_time = $('#member_form input[name=id_movie_time]').val();
                var id_movie_date_active = $('#member_form input[name=id_movie_date_active]').val();

                window.location.href = '/booking?id_showtime='+ id_showtime + '&id_sever='+ id_sever
                            + '&id_movie_name='+ id_movie_name + '&id_movie_time='+ id_movie_time
                            + '&id_movie_date_active='+ id_movie_date_active;
            };
        }
        // else {
        //     var ignoreHashChange = true;
        //     window.onhashchange = function () {
        //         if (!ignoreHashChange) {
        //             ignoreHashChange = true;
        //             window.location.hash = Math.random();
        //             alert("refres");
        //             // Detect and redirect change here
        //             // Works in older FF and IE9
        //             // * it does mess with your hash symbol (anchor?) pound sign
        //             // delimiter on the end of the URL
        //         }
        //         else {
        //             ignoreHashChange = false;   
        //         }
        //     };
        // }
    }
    wireUpEvents();  

    $("#btnPopup").click(function (event) {
        // event.preventDefault();
        // var postData = JSON.stringify($("#create_form").serializeArray());
        var postData = $("#create_form").serialize();
        console.log("postData ",postData);
        var submitUrl = $("#create_form").attr("action");
        $.ajax({
            type: "POST",
            url: submitUrl,
            data: postData,
            dataType: "JSON",
            success: function (x) {
                console.log("success ",x);
                if (x.code === '00') {
                    if (window.vnpay) {
                        vnpay.open({width: 768, height: 600, url: x.data});
                    }
                    else {
                        location.href = x.data;
                    }
                    return false;
                } else {
                    alert(x.Message);
                }
            },
            crossDomain: false
        });
        return false;
    });

    // validate form
    var val_required = 'Trường này là bắt buộc';
    $("#create_form").validate({
        rules: {
            amount: { 
                number: true,
                required: true,
                min: 1,
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
                number: 'Vui lòng chỉ nhập số',
                required: val_required,
                min: "Vui lòng nhập lớn hơn 0."
            },
            bank_code: {
                required: val_required,
            },
            order_id: {
                required: val_required,
            }
        }
    });

    // format money
    var money_total = $('#create_form input[name=amount-text]').val();
    $('#create_form input[name=amount-text]').val(money_total.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1."));
});

// back page booking seat
function goBack() {
    window.history.back();
}

function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10)
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.text(minutes + ":" + seconds);

        if (--timer < 0) {
            endSession();
            window.location.href = '/timeout/booking'
        }
    }, 1000);
}

jQuery(function ($) {
    var fiveMinutes = 60 * 5,
        display = $('#time-cout-down');
    startTimer(fiveMinutes, display);
});