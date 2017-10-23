var price = 10; //price
// data example
var list_booking = {"List":[{"ID":"11984242","NAME":"A01","STATUS":"True","X":"198","Y":"63","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984249","NAME":"A02","STATUS":"True","X":"264","Y":"63","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984256","NAME":"A03","STATUS":"False","X":"330","Y":"63","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984266","NAME":"A04","STATUS":"False","X":"396","Y":"63","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984274","NAME":"A05","STATUS":"False","X":"462","Y":"63","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984282","NAME":"A06","STATUS":"False","X":"528","Y":"63","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984289","NAME":"A07","STATUS":"False","X":"594","Y":"63","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984296","NAME":"A08","STATUS":"False","X":"660","Y":"63","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984304","NAME":"A10","STATUS":"False","X":"726","Y":"63","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984237","NAME":"B01","STATUS":"False","X":"132","Y":"126","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984243","NAME":"B02","STATUS":"False","X":"198","Y":"126","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984250","NAME":"B03","STATUS":"False","X":"264","Y":"126","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984257","NAME":"B04","STATUS":"False","X":"330","Y":"126","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984267","NAME":"B05","STATUS":"False","X":"396","Y":"126","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984275","NAME":"B06","STATUS":"False","X":"462","Y":"126","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984283","NAME":"B07","STATUS":"False","X":"528","Y":"126","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984290","NAME":"B08","STATUS":"False","X":"594","Y":"126","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984297","NAME":"B09","STATUS":"False","X":"660","Y":"126","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984305","NAME":"B10","STATUS":"True","X":"726","Y":"126","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984238","NAME":"C01","STATUS":"False","X":"132","Y":"189","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984244","NAME":"C02","STATUS":"False","X":"198","Y":"189","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984251","NAME":"C03","STATUS":"False","X":"264","Y":"189","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984258","NAME":"C04","STATUS":"False","X":"330","Y":"189","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984268","NAME":"C05","STATUS":"False","X":"396","Y":"189","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984276","NAME":"C06","STATUS":"False","X":"462","Y":"189","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984284","NAME":"C07","STATUS":"False","X":"528","Y":"189","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984291","NAME":"C08","STATUS":"False","X":"594","Y":"189","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984298","NAME":"C09","STATUS":"False","X":"660","Y":"189","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984306","NAME":"C10","STATUS":"False","X":"726","Y":"189","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984239","NAME":"D01","STATUS":"False","X":"132","Y":"252","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984245","NAME":"D02","STATUS":"False","X":"198","Y":"252","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984252","NAME":"D03","STATUS":"True","X":"264","Y":"252","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984259","NAME":"D04","STATUS":"False","X":"330","Y":"252","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984269","NAME":"D05","STATUS":"False","X":"396","Y":"252","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984277","NAME":"D06","STATUS":"False","X":"462","Y":"252","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984285","NAME":"D07","STATUS":"False","X":"528","Y":"252","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984292","NAME":"D08","STATUS":"False","X":"594","Y":"252","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984299","NAME":"D09","STATUS":"False","X":"660","Y":"252","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984307","NAME":"D10","STATUS":"False","X":"726","Y":"252","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984240","NAME":"E01","STATUS":"False","X":"132","Y":"315","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984246","NAME":"E02","STATUS":"False","X":"198","Y":"315","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984253","NAME":"E03","STATUS":"False","X":"264","Y":"315","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984260","NAME":"E04","STATUS":"False","X":"330","Y":"315","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984270","NAME":"E05","STATUS":"False","X":"396","Y":"315","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984278","NAME":"E06","STATUS":"False","X":"462","Y":"315","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984286","NAME":"E07","STATUS":"False","X":"528","Y":"315","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984293","NAME":"E08","STATUS":"False","X":"594","Y":"315","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984300","NAME":"E09","STATUS":"False","X":"660","Y":"315","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984308","NAME":"E10","STATUS":"False","X":"726","Y":"315","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984241","NAME":"F01","STATUS":"False","X":"132","Y":"378","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984247","NAME":"F02","STATUS":"False","X":"198","Y":"378","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984254","NAME":"F03","STATUS":"False","X":"264","Y":"378","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984261","NAME":"F04","STATUS":"False","X":"330","Y":"378","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984271","NAME":"F05","STATUS":"False","X":"396","Y":"378","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984279","NAME":"F06","STATUS":"False","X":"462","Y":"378","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984287","NAME":"F07","STATUS":"False","X":"528","Y":"378","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984294","NAME":"F08","STATUS":"False","X":"594","Y":"378","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984301","NAME":"F09","STATUS":"False","X":"660","Y":"378","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984309","NAME":"F10","STATUS":"False","X":"726","Y":"378","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984262","NAME":"G01","STATUS":"False","X":"330","Y":"441","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984272","NAME":"G02","STATUS":"False","X":"396","Y":"441","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984280","NAME":"G03","STATUS":"False","X":"462","Y":"441","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984288","NAME":"G04","STATUS":"False","X":"528","Y":"441","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984295","NAME":"G05","STATUS":"False","X":"594","Y":"441","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984302","NAME":"G06","STATUS":"False","X":"660","Y":"441","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984263","NAME":"H01","STATUS":"False","X":"330","Y":"504","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984273","NAME":"H02","STATUS":"False","X":"396","Y":"504","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984281","NAME":"H03","STATUS":"False","X":"462","Y":"504","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984303","NAME":"H04","STATUS":"False","X":"660","Y":"504","W":"129","H":"60","COLOR":"Fuchsia","TYPE_SEAT_ID":"30","TYPE_SEAT_NAME":"ĐÔI","PRICE":""},{"ID":"11984264","NAME":"I03","STATUS":"False","X":"330","Y":"567","W":"129","H":"60","COLOR":"Fuchsia","TYPE_SEAT_ID":"30","TYPE_SEAT_NAME":"ĐÔI","PRICE":""},{"ID":"11984310","NAME":"I08","STATUS":"False","X":"660","Y":"567","W":"63","H":"60","COLOR":"ffff8000","TYPE_SEAT_ID":"29","TYPE_SEAT_NAME":"ĐƠN","PRICE":""},{"ID":"11984248","NAME":"J04","STATUS":"False","X":"198","Y":"630","W":"129","H":"60","COLOR":"Fuchsia","TYPE_SEAT_ID":"30","TYPE_SEAT_NAME":"ĐÔI","PRICE":""},{"ID":"11984265","NAME":"J12","STATUS":"False","X":"330","Y":"630","W":"129","H":"60","COLOR":"Fuchsia","TYPE_SEAT_ID":"30","TYPE_SEAT_NAME":"ĐÔI","PRICE":""}]}
$(document).ready(function() {
    var $cart = $('#selected-seats'), //Sitting Area
    $counter = $('#counter'), //Votes
    $total = $('#total'); //Total money

    var objBooking = list_booking.List;
    var sameStr = '';
    var iArr = -1;
    var rowNaming = [];
    var arrStatus = [];
    var numberMax = 0;
    var objSeat = [];
    var mapArr = [];
    var number;
    // array object with name, value form list_booking NAME
    for(i=0; i < objBooking.length; i++){
        if(objBooking[i].NAME.substring(0,1) == sameStr){
            //number max of row
            if(parseInt(objBooking[i].NAME.substring(1,3)) > numberMax){
                numberMax = parseInt(objBooking[i].NAME.substring(1,3));
            }
            objSeat[iArr].value.push(parseInt(objBooking[i].NAME.substring(1,3)));
        }else{
            iArr++;
            sameStr = rowNaming[iArr] = objBooking[i].NAME.substring(0,1);
            objSeat[iArr] = {
                'name':objBooking[i].NAME.substring(0,1),
                'value':[parseInt(objBooking[i].NAME.substring(1,3))]
            };
        }

        // array with status
        if(!(objBooking[i].STATUS == "False")){
            if(parseInt(objBooking[i].NAME.substring(1,3)) < 10){
                arrStatus[i] = objBooking[i].NAME.replace('0','_');
            }else{
                my_string = objBooking[i].NAME.split('');
                my_string.splice( 1 , 0, '_' );
                arrStatus[i] = my_string.join('');
            }
        }
    }

    // Get array map seatCharts
    for(i=0; i< objSeat.length; i++){
        mapArr[i] = [];
        number=1;
        for(j=0; j<numberMax; j++){
            if(objSeat[i].value[j] == number){
                mapArr[i] += objSeat[i].name;
            }else{
                mapArr[i] += '_';
                j--;
            }
            if(number == numberMax){
                break;
            }
            number++;
        }
    }

    var sc = $('#seat-map').seatCharts({
        map: mapArr,
        naming : {
            top : false,
            rows: rowNaming,
            // can 1 for 0...numberMax get array columns
            columns: ['1','2','3','4','5','6','7','8','9','10',
                '11','12','13','14','15','16','17','18','19','20'],
            getLabel : function (character, row, column) {
                return row+column;
            }
        },
        legend : { //Definition legend
            node : $('#legend'),
            items : [
                [ 'a', 'available',   'Ghế trống' ],
                [ 'a', 'unavailable', 'Ghế đã có người đặt'],
                [ 'a', 'selected', 'Ghế đang chọn']
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
                $total.text(recalculateTotal(sc)+price);

                return 'selected';
            } else if (this.status() == 'selected') { //Checked
                    //Update Number
                    $counter.text(sc.find('selected').length-1);
                    //update totalnum
                    $total.text(recalculateTotal(sc)-price);

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

});
//sum total money
function recalculateTotal(sc) {
    var total = 0;
    sc.find('selected').each(function () {
        total += price;
    });

    return total;
}
