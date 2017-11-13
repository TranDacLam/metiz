var validNavigation = false;

function endSession() {
    // Call server clear session
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


$(document).ready(function() {
    // detect redirect page only ecept button submit form and change showtime
    $('body a').click(function(evt){    
       if(evt.target.id == "btn-payment-seats" || $(evt.target).hasClass("popup-movie-schedule") || evt.target.id == "id-menu-member" || evt.target.id == "id-menu-movie"){
          return;
       }else{
            endSession();
       }
        
    });

    window.onload = function () {
        if (typeof history.pushState === "function") {
            history.pushState("loadpage", null, null);
            window.onpopstate = function () {
                history.pushState('new_loadpage', null, null);
                // Handle the back (or forward) buttons here
                // Will NOT handle refresh, use onbeforeunload for this.
                endSession();
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
    }

    $("#btnPopup").click(function (event) {
        // event.preventDefault();
        // var postData = JSON.stringify($("#create_form").serializeArray());
        var postData = $("#create_form").serialize();
        var submitUrl = $("#create_form").attr("action");
        // Call server verify session
        $.ajax({
            type: "POST",
            url: submitUrl,
            data: postData,
            dataType: "JSON",
            success: function (x) {
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

    // setTimeOut 5 minutes will redirect page timeout/booking
    setTimeout(function(){
        endSession();
        window.location.href = '/timeout/booking'
    }, 300000);

    // format money
    var money_total = $('#create_form input[name=amount-text]').val();
    $('#create_form input[name=amount-text]').val(money_total.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1."));
});