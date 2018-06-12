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