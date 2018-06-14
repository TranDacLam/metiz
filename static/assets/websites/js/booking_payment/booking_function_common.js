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
function getSeatSelected(sc){
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

// file: booking_add_to_card.js
function guid() {
    function s4() {
        return Math.floor((1 + Math.random()) * 0x10000)
            .toString(16)
            .substring(1);
    }
    return s4() + s4() + '-' + s4() + '-' + s4() + '-' +
        s4() + '-' + s4() + s4() + s4();
}

// translate unikey, file: booking_add_to_card.js
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

// toUpperCase first leter of string, file: booking_add_to_card.js
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

//sum total money, file: booking_create_seat.js
function recalculateTotal(sc) {
    var total = 0;
    sc.find('selected').each(function () {
        total += this.data().price;
    });
    return total;
}

// show msg, file booking_validate_seat.js
function messages_valied_seat(){
    displayMsg();
    $('.msg-result-js').html(msgResult("Việc chọn vị trí ghế của bạn không được để trống "
        + "1 ghế ở bên trái, giữa hoặc bên phải trên cùng hàng ghế mà bạn vừa chọn.", "warning"));
}