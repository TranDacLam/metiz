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

    // show icon load when ajax start 
    $(document).ajaxStart(function(){
        $(".ajax-loader").css("display", "block");
    });
    // hidden icon load when ajax complete
    $(document).ajaxComplete(function(){
        $(".ajax-loader").css("display", "none");
    });

    // disable key space when select seat
    $('.seatCharts-cell').keydown(function(e) {
        if(e.which === 32){
            return false;
        }
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
                    [ 'a', 'unavailable', 'Ghế đã có người đặt'],
                    [ 'a', 'selected', 'Ghế đang chọn'],
                    [ 'a', 'available',   'Ghế trống' ],
                    [ 'v', 'available',   'Ghế VIP' ],
                    [ 'c', 'available',   'Ghế couple' ],
                    [ 'l', 'available',   'Ghế cao cấp' ]
                ]
            },
            click: function () { //Click event
                if (this.status() == 'available') { //optional seat
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
                    return this.style();
                }
            }
        });

        //sold seat
        sc.get(arrStatus).status('unavailable');

        var seatPayment = [];
        var seats_choice = [];

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
            seatSelected = new Array();
            var seats =  sc.find('selected').seats;
            for(i=0;i<seats.length; i++){
                seats_choice.push(seats[i].settings.id);
                seatSelected.push(JSON.stringify({
                    'ID': seats[i].settings.id,
                    'NAME': strimNameSeat(seats[i].settings.label)
                }));

                seatPayment.push(strimNameSeat(seats[i].settings.label));
            }
            // Sort by name seat
            seatPayment.sort();
            
            return seatSelected;
        }



        // redirect payment with total and seat
        $('#btnNextBooking').on('click',function(){
            var totalPayment = recalculateTotal(sc);
            var lst_seats = getSeatSelected();
            var totalSeat = seatPayment.length;
            var id_movie_name = $('.name-movie-booking').text();
            var movie_time_replace = $('.time-movie-booking').text();
            var id_movie_date_active = $('.date-movie-booking').text();
            var id_movie_time = movie_time_replace.replace('~', '-');

            // check user selected seat?
            if(totalSeat < 1){
                displayMsg();
                $('.msg-result-js').html(msgResult("Bạn chưa chọn ghế!", "warning"));
                return false;
            }
            var working_id = guid();
            data = {
                "id_showtime": id_showtime,
                "id_server": id_server,
                "lst_seats": "["+ lst_seats.toString() +"]",
                "working_id": working_id
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
                window.location.href = '/payment?totalPayment='+ totalPayment +'&totalSeat='+ totalSeat 
                +'&seats='+ seatPayment + '&id_movie_name='+id_movie_name
                + '&id_movie_time='+id_movie_time + '&id_movie_date_active='+id_movie_date_active
                + '&working_id='+working_id + '&barcode='+ barcode 
                + '&seats_choice='+seats_choice + '&id_server=' +id_server + '&id_showtime=' +id_showtime;
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
        return date_shedule.replace(/([0-9]{4})\-([0-9]{2})\-([0-9]{2})/g, '$3 - $2 - $1');
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