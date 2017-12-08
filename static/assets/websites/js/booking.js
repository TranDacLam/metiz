function guid() {
      function s4() {
        return Math.floor((1 + Math.random()) * 0x10000)
          .toString(16)
          .substring(1);
      }
      return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
        s4() + '-' + s4() + s4() + s4();
    }

$(document).ready(function() {
    var id_server = $('#id_server').val();
    var id_showtime = $('#id_showtime').val();
    var movie_api_id = $('#movie_api_id').val();

    // Validate member_card only input alpha
    $("#member_card").on("input", function(){
        var regexp = /[^a-zA-Z]/g;
        if($(this).val().match(regexp)){
            $(this).val( $(this).val().replace(regexp,'') );
        }
    });

    // show icon load when ajax start 
    $(document).ajaxStart(function(){
        $(".ajax-loader").css("display", "block");
    });
    // hidden icon load when ajax complete
    $(document).ajaxComplete(function(){
        $(".ajax-loader").css("display", "none");
    });

    // variable setTimeout
    var timer;

    // Get list seats
    $.ajax({
        url: "/movie/seats",
        type: 'GET',
        data: {
            "id_showtime": id_showtime,
            "id_server": id_server
        },
        dataType: 'json',
        crossDomain:false,
        context: this,
    })
    .done(function(response) {
        // Check List seat 
        if(response.List && response.List.length > 0){
            bookingSeat(response.List);

            // disable select seat when keydown key space
            // Step 1: Turn off keydown (key space), override event keydown (key space) in library seat-charts.
            // Step 2: Turn on keydown and handle event prevenDefault
            $("#seat-map .seatCharts-row div.seatCharts-seat.seatCharts-cell.available").off("keydown");
            $("#seat-map .seatCharts-row div.seatCharts-seat.seatCharts-cell.available").on("keydown", function(e){
                if (e.which == 32) {
                    e.preventDefault();
                }        
            });
            // Disable forcus outside  area choice seat 
            $('#seat-map').unbind("focus");
        }else{
            // show message when List seat empty, setTimeout 10s back home
            displayMsg();
            $('.msg-result-js').html(msgResult("Lỗi hệ thống! Vui lòng liên hệ "
                +"với admin để được hỗ trợ, hệ thống sẽ quay lại trang chủ sau 10 giây. Cảm ơn!", "danger"));
            timer = setTimeout(function(){ 
                window.location ='/';
            }, 10000);
        }
        
    })
    .fail(function(error) {
        displayMsg();
        if(error.status == 400){
            $('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
        }else{
            $('.msg-result-js').html(msgResult("Error get seats", "danger"));
        }
    });

    // Clear setTimeout when click show popup schedule in 10s back home
    $('.popup-movie-schedule').on('click', function(){
        window.clearTimeout(timer);
    });


    function bookingSeat(objBooking){
        var $cart = $('#selected-seats'), //Sitting Area
        $counter = $('#counter'), //Votes
        $total = $('#total'); //Total money
        var maximumSeat = 8; // choice seat maximum is 8 seat

        var sameStr = '';
        var iArr = -1;
        var rowNaming = [];
        var arrStatus = [];
        var seatMax = parseInt(objBooking[objBooking.length-1].NAME.substring(1,3));
        var objSeat = [];
        var mapArr = [];
        var mapRow = [];
        var number;

        // varirable price 
        var price_a;
        var price_c;
        var price_v;
        var price_l;

        // get Type seat and set Price for every type seat
        function typeSeatBooking(seat){
            var type_seat;
            switch(seat.TYPE_SEAT_ID) {
                case "30": 
                    type_seat = "c";
                    price_c = parseInt(seat.PRICE);
                    break;
                case "31": 
                    type_seat = "v";
                    price_v = parseInt(seat.PRICE);
                    break;
                case "32": 
                    type_seat = "l";
                    price_l = parseInt(seat.PRICE);
                    break;
                default: 
                    type_seat = "a";
                    price_a = parseInt(seat.PRICE);
            }
            return type_seat;
        }

        // array object with name, value form list_booking NAME
        for(i=0; i < objBooking.length; i++){
            if(objBooking[i].NAME.substring(0,1) == sameStr){
                objSeat[iArr].value.push(parseInt(objBooking[i].NAME.substring(1,3)));
                objSeat[iArr].type_seat.push(typeSeatBooking(objBooking[i]));
                objSeat[iArr].id_seat.push({
                                'id': objBooking[i].ID,
                            });
            }else{
                iArr++;
                //seat max of row, get value trước row seat kế tiếp
                // vd: A1=1, A2=2, B1=1. get value A2=2  
                if(iArr > 0 && parseInt(objBooking[i-1].NAME.substring(1,3)) > seatMax){
                    seatMax = parseInt(objBooking[i-1].NAME.substring(1,3));
                }
                sameStr = rowNaming[iArr] = objBooking[i].NAME.substring(0,1);
                objSeat[iArr] = {
                    'name':objBooking[i].NAME.substring(0,1),
                    'value':[parseInt(objBooking[i].NAME.substring(1,3))],
                    'type_seat':[typeSeatBooking(objBooking[i])],
                    'id_seat':[{
                                'id': objBooking[i].ID,
                            }]
                };
            }

            // array with status
            if(!(objBooking[i].STATUS == "False")){
                arrStatus.push(objBooking[i].ID);
            }
        }

        // Range 
        var numberRange = function(start, stop, step) {
            var arrRange = [start];
            while (start < stop) {
                start += step || 1;
                arrRange.push(start);
            }
            return arrRange;
        };

        // numberRange get value (1,3) -> [1,2,3] 
        var arrColumns = numberRange(1, seatMax);

        // get array map seat Charts
        for(i=0; i< objSeat.length; i++){
            number = 0;
            $.grep(arrColumns, function(el) {
                if ($.inArray(el, objSeat[i].value) == -1){
                    mapRow[el-1] = "_";
                    number--;
                }else{
                    mapRow[el-1] = objSeat[i].type_seat[number] + '['+ objSeat[i].id_seat[number].id +']';
                }
                number++;
            });
            mapArr[i] = mapRow.join('');
        }

        var sc = $('#seat-map').seatCharts({
            map: mapArr, // List seats
            naming : { // Name seat columns, rows
                top : false,
                rows: rowNaming,
                columns: arrColumns,
                getLabel : function (character, row, column) {
                    return row+column;
                }
            },
            seats: { //Definition seat property
                a: {
                    price   : price_a
                },
                v: {
                    price   : price_v,
                    classes : 'seat-vip', 
                    category: 'vip'
                },
                c: {
                    price   : price_c,
                    classes : 'seat-couple', 
                    category: 'couple'
                },
                l: {
                    price   : price_l,
                    classes : 'seat-ld', 
                    category: 'LD'
                }                  
            },
            legend : { //Definition legend
                node : $('#legend'),
                items : [
                    [ 'a', 'unavailable', 'Ghế đã đặt'],
                    [ 'a', 'selected', 'Ghế đang chọn'],
                    [ 'a', 'available',   'Ghế thường' ],
                    [ 'v', 'available',   'Ghế VIP' ],
                    [ 'c', 'available',   'Ghế couple' ],
                    [ 'l', 'available',   'Ghế cao cấp' ]
                ]
            },
            click: function () { //Click event
                // Check status and maximum seat choice
                if (this.status() == 'available' && sc.find('selected').length < maximumSeat) { //optional seat
                    $('<li>'+this.settings.label+'</li>')
                    // $('<li>'+(this.settings.character)+''+this.settings.label+'</li>')
                        .attr('id', 'cart-item-'+this.settings.id)
                        .data('seatId', this.settings.id)
                        .appendTo($cart);

                    // set number seat html
                    $counter.text(sc.find('selected').length+1);
                    // get total price seat selected
                    var moneyTotal = recalculateTotal(sc)+this.data().price;
                    // set total html and format money VND
                    $total.text(moneyTotal.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1."));

                    return 'selected';
                } else if (this.status() == 'selected') { //Checked
                        //Update Number
                        $counter.text(sc.find('selected').length-1);
                        //update totalnum
                        var updateMoneyTotal = recalculateTotal(sc)-this.data().price;
                        // set total html and format money VND
                        $total.text(updateMoneyTotal.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1."));

                        //Delete reservation
                        $('#cart-item-'+this.settings.id).remove();
                        //optional
                        return 'available';
                } else if (this.status() == 'unavailable') { //sold
                    return 'unavailable';
                } else {
                    // check maximum seat result message
                    if(sc.find('selected').length >= maximumSeat ){
                        displayMsg();
                        $('.msg-result-js').html(msgResult("Vui lòng chỉ chọn tối đa 8 ghế.", "warning"));
                    }
                    return this.style();
                }
            }
        });

        //sold seat
        sc.get(arrStatus).status('unavailable');

        // Trim name seat
        function strimNameSeat(str){
            if(str.length == 2 && parseInt(str.substring(1,3)) < 10){
                my_string = str.split('');
                strimStr = my_string.join('0');
                return strimStr;
            }
            return str;
        }

        // Get ID, NAME seat selected. [{"ID": "1", "NAME": "A03"}]
        function getSeatSelected(){
            var seatSelected = new Array();
            var seats =  sc.find('selected').seats;
            for(i=0;i<seats.length; i++){
                seatSelected.push(JSON.stringify({
                    'ID': seats[i].settings.id,
                    'NAME': strimNameSeat(seats[i].settings.label)
                }));
            }
            return seatSelected;
        }
        // click booking next button.
        $('#btnNextBooking').on('click',function(){
            // get length Seat selected
            var totalSeat = getSeatSelected().length;
            // check user selected seat?
            if(totalSeat < 1){
                displayMsg();
                $('.msg-result-js').html(msgResult("Bạn chưa chọn ghế!", "warning"));
                return false;
            } else {
                $('#member_card_modal').modal('show');
            }
            
        });
        // Click add Card button
        $('#btn_add_card').on('click',function(){
            var totalPayment = recalculateTotal(sc);
            var id_movie_time = $('.time-movie-booking').text().replace('~', '-');
            var id_movie_date_active = $('.date-movie-booking').text();
            // Translate string, toUpperCase first letter of string, substring if string > 20 character
            var id_movie_name = firstLeterCase(translateVI($('.name-movie-booking').text())).substring(0, 25);

            // get id, name seat selected
            var seatSelected = getSeatSelected();

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
                // get array id seat selected
                var seats_choice = seatSelected.map(item => JSON.parse(item).ID);
                // get array name seat selected va sort by name
                var seatPayment = seatSelected.map(item => JSON.parse(item).NAME).sort();

                window.location.href = '/payment?totalPayment='+ totalPayment
                +'&seats='+ seatPayment + '&id_movie_name='+id_movie_name
                + '&id_movie_time='+id_movie_time + '&id_movie_date_active='+id_movie_date_active
                + '&working_id='+working_id + '&barcode='+ barcode 
                + '&seats_choice='+seats_choice + '&id_server=' +id_server + '&id_showtime=' +id_showtime
                + '&movie_api_id=' +movie_api_id;
            })
            .fail(function(error) {
                displayMsg();
                $('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
            });
        });

        // Refresh seat selected
        $('.booking-refresh a').on('click', function(){
            sc.find('selected').status('available');
            $counter.text(0);
            $total.text(0);
            $('#selected-seats').html('');
        });
    }

    // format date movie
    $('.date-movie-booking').text(getDate());
    function getDate(){
        var date_shedule = $('.date-movie-booking').text();
        return date_shedule.replace(/([0-9]{4})\-([0-9]{2})\-([0-9]{2})/g, '$3-$2-$1');
    }
});
//sum total money
function recalculateTotal(sc) {
    var total = 0;
    sc.find('selected').each(function () {
        total += this.data().price;
    });
    return total;
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