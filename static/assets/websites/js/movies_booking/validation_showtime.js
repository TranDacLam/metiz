// Validate Time Remain before 15 minutes. verify when date selected equal current date
 // function for modal page and schedule page
function validate_time_remain(element){
    var time_remain = 15;
    var date_now = new Date();
    // get current date selected and time of movie show
    var date_selected = new Date($('.day-showing-item.active-date').attr('movie-day-selected'));
    var start_time = element.children('.time').text().split('~')[0];
    
    // get show time sub 15 minute check show time greate than equal curren time then allow booking
    var time_show = (start_time.split(":")[0] * 60 + parseInt(start_time.split(":")[1])) - time_remain;
    var current_time = date_now.getHours() * 60 + date_now.getMinutes() ;
    
    if(new Date().setHours(0,0,0,0) < date_selected.setHours(0,0,0,0) || time_show >= current_time){
        return true;
    }
    return false;
}
