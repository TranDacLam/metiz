function bookingAddCard(sc, id_showtime, id_server, movie_api_id){
    // Click add Card button
    $('#btn_add_card').on('click',function(){
        var totalPayment = recalculateTotal(sc);
        var id_movie_time = $('.time-movie-booking').text().replace('~', '-');
        var id_movie_date_active = $('.date-movie-booking').text();
        // Translate string, toUpperCase first letter of string, substring if string > 20 character
        var id_movie_name = firstLeterCase(translateVI($('.name-movie-booking').text())).substring(0, 25);

        var movie_poster = $('.movie-poster-class').val();

        // get id, name seat selected
        // function from booking_function_common.js
        var seatSelected = getSeatSelected(sc);

        var working_id = guid();
        data = {
            "id_showtime": id_showtime,
            "id_server": id_server,
            "lst_seats": "["+ seatSelected.toString() +"]",
            "working_id": working_id,
            "member_card": $("#member_card").val()
        }
        $.ajax({
            url: "/verify/seats",
            type: 'POST',
            data: data,
            dataType: 'json',
            crossDomain:false,
            context: this,
        })
        .done(function(response) {
            var barcode = response.BARCODE

            // get array ID and NAME seat selected
            // get array name seat selected va sort by name
            var seats_choice =[];
            var seatPayment = [];
            for(i=0; i<seatSelected.length; i++){
                seats_choice.push(JSON.parse(seatSelected[i]).ID);
                seatPayment.push(JSON.parse(seatSelected[i]).NAME);
            }
            // Sort array seatPayment
            seatPayment.sort();

            data_form = {
                    "totalPayment": response.total_payment,
                    "seats": seatPayment,
                    "id_movie_name": id_movie_name,
                    "id_movie_time": id_movie_time,
                    "id_movie_date_active": id_movie_date_active,
                    "working_id":working_id,
                    "barcode":barcode,
                    "seats_choice":seats_choice,
                    "id_server":id_server,
                    "id_showtime":id_showtime,
                    "movie_api_id":movie_api_id,
                    "movie_poster": movie_poster
                }

             $.ajax({
                url: "/payment/encrypt/",
                type: 'POST',
                data: {"data_form": JSON.stringify(data_form)},
                dataType: 'json',
                crossDomain:false,
                context: this,
            })
            .done(function(response) {
                window.location.href = '/payment/method?data='+encodeURIComponent(response.data_encode);
            }).fail(function(error) {
                displayMsg();
                $('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
            });
            
        })
        .fail(function(error) {
            displayMsg();
            $('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
        });
    });
}

function guid() {
    function s4() {
        return Math.floor((1 + Math.random()) * 0x10000)
            .toString(16)
            .substring(1);
    }
    return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
        s4() + '-' + s4() + s4() + s4();
}

// translate unikey
function translateVI(str) {  
    str= str.toLowerCase();  
    str= str.replace(/à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ/g,"a");  
    str= str.replace(/è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ/g,"e");  
    str= str.replace(/ì|í|ị|ỉ|ĩ/g,"i");  
    str= str.replace(/ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ/g,"o");  
    str= str.replace(/ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ/g,"u");  
    str= str.replace(/ỳ|ý|ỵ|ỷ|ỹ/g,"y");  
    str= str.replace(/đ/g,"d");  
    return str;  
}

// toUpperCase first leter of string
function firstLeterCase(str){
    str = str.toLowerCase();
    var array = str.split(' ');
    for(var c = 0; c < array.length; c++){
        if(array[c][0] != null){
            array[c] = array[c][0].toUpperCase() + array[c].substring(1);
        }
    }
    return array.join('');
}