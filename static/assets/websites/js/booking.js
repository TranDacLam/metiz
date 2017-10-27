$(document).ready(function() {
    var id_server = $('#id_sever').val();
    var id_showtime = $('#id_showtime').val();

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
        bookingSeat(response.List);
    })
    .fail(function(error) {
        displayMsg();
        if(error.status == 400){
            $('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
        }else{
            $('.msg-result-js').html(msgResult("Error get seats", "danger"));
        }
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

        // get Type seat
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
        function numberRange (start, end) {
            return new Array(end - start).fill().map((d, i) => i + start);
        }

        // numberRange get value (1,3) -> [1,2] 
        var arrColumns = numberRange(1, seatMax+1);

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
            map: mapArr,
            naming : {
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

                    $counter.text(sc.find('selected').length+1);
                    $total.text(recalculateTotal(sc)+this.data().price);

                    return 'selected';
                } else if (this.status() == 'selected') { //Checked
                        //Update Number
                        $counter.text(sc.find('selected').length-1);
                        //update totalnum
                        $total.text(recalculateTotal(sc)-this.data().price);

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
        // Get ID, NAME seat selected. [{"ID": "1", "NAME": "A03"}]
        function getSeatSelected(){
            seatSelected = new Array();
            var seats =  sc.find('selected').seats;
            for(i=0;i<seats.length; i++){
                seatSelected.push(JSON.stringify({
                    'ID': seats[i].settings.id,
                    'NAME': strimNameSeat(seats[i].settings.label)
                }));

                seatPayment.push(strimNameSeat(seats[i].settings.label));
            }
            return seatSelected;
        }



        // redirect payment with total and seat
        $('#btnNextBooking').on('click',function(){
            var totalPayment = parseInt($('#total').text());
            var lst_seats = getSeatSelected();
            var totalSeat = seatPayment.length;

            // check user selected seat?
            if(totalSeat < 1){
                displayMsg();
                $('.msg-result-js').html(msgResult("Bạn chưa đặt vé!", "warning"));
                return false;
            }
            data = {
                "id_showtime": id_showtime,
                "id_server": id_server,
                "lst_seats": "["+ lst_seats.toString() +"]"
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
                window.location.href = '/payment?totalPayment='+ totalPayment +'&totalSeat='+ totalSeat +'&seats='+ seatPayment;
            })
            .fail(function(error) {
                displayMsg();
                $('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
            });
        });


        function strimNameSeat(str){
            if(str.length == 2 && parseInt(str.substring(1,3)) < 10){
                my_string = str.split('');
                strimStr = my_string.join('0');
                return strimStr;
            }
            return str;
        }

        // Refresh seat selected
        $('.booking-refresh a').on('click', function(){
            sc.find('selected').status('available');
            $counter.text(0);
            $total.text(0);
            $('#selected-seats').html('');
        });
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