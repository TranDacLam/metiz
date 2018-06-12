// create seat
function bookingSeat(objBooking, id_showtime, id_server, movie_api_id){
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

            // Check first seat and set coordinates X first for every name seat
            if(parseInt(objBooking[i].NAME.substring(1,3)) == 1){
                objSeat[iArr].coordinates_x = objBooking[i].X;
            }

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
        // Check seat is couple
        if(objSeat[i].type_seat[0] == "c"){
            var seatMaxCouple;
            // max seat - number seat couple in 1 row. 1 seat couple = 2 seat empty  
            seatMaxCouple = seatMax - objSeat[i].type_seat.length;
            
            // Get arr seat form 0 - max seat couple
            var mapRowCouple = mapRow.splice(0,seatMaxCouple);
            mapArr[i] = mapRowCouple.join('');
        }else{
            mapArr[i] = mapRow.join('');
        }
        
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
                [ 'l', 'available',   'Ghế cao cấp' ],
                [ 'c', 'available',   'Ghế couple' ]
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

    // Check coordinates X seat, If seat couple exist then compare coordinates X seat other
    // If different, insert Before seat couple first 1 div at row last
    for(k=0; k < (objSeat.length - 1); k++){
        if(objSeat[k].coordinates_x && objSeat[objSeat.length - 1].coordinates_x){
            if((objSeat[k].coordinates_x != objSeat[objSeat.length - 1].coordinates_x) && 
                (objSeat[objSeat.length - 1].type_seat[0] == "c")){
                $("<div class='seatCharts-cell seatCharts-space'></div>").insertBefore(".seatCharts-row:last .seat-couple:first");
                $('.seatCharts-row:last .seatCharts-space:last').remove();
                break;
            }
        }
    }

    //sold seat
    sc.get(arrStatus).status('unavailable');

    // click booking next button.
    // function from booking_check_seat.js
    bookingCheckSeat(sc);

    // Click add Card button
    // function from booking_add_card.js
    bookingAddCard(sc, id_showtime, id_server, movie_api_id);

    // Refresh seat selected
    $('.booking-refresh a').on('click', function(){
        sc.find('selected').status('available');
        $counter.text(0);
        $total.text(0);
        $('#selected-seats').html('');
    });
}

//sum total money
function recalculateTotal(sc) {
    var total = 0;
    sc.find('selected').each(function () {
        total += this.data().price;
    });
    return total;
}