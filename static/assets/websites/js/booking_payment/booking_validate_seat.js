function bookingValidateSeat(sc){
    // click booking next button.
    $('#btnNextBooking').on('click',function(){
        var movie_id = $("#movie_api_id").val();

        // On LOCAL, DEV, UAT envs then only accept film test movie api setting on server
        if (document.domain != "metiz.vn" && movieIdTest != movie_id ) {
            alert("Phim này chỉ được xuất vé trên PRODUCTION. Vui chọn phim TEST khác.");
            return;
        }

        var number_column_valid; // get number seat selected
        var status_valid = false; // status show message error
        var seats_row_valid; // array object of a row
        var number_max_valid; // index max in a row
        var number_min_valid; // index min in a row
        var total_available_valid; // Total seats on 1 row, check condition > 3

        // redirect to page timeout when time out movie
        // file booking_validate_timeout_movie.js
        if(bookingValidateTimeOutMovie()){
            window.location.href = "/timeout/?page=movie";
            return;
        }

        // get length Seat selected
        // function from booking_function_common.js
        var totalSeat = getSeatSelected(sc).length;

        // check user selected seat?
        if(totalSeat < 1){
            displayMsg();
            $('.msg-result-js').html(msgResult("Bạn chưa chọn ghế!", "warning"));
            return false;
        }

        sc.find('selected').each(function(key){
            seats_row_valid = [];
            number_max_valid = 0;
            number_min_valid = 0;

            // add class -> foreach seat in a row seat selected
            $('#seat-map').find('#'+this.settings.id).parent().addClass('parent_seat_'+key);
            $(".parent_seat_" + key +">div").each(function(index) {
                seats_row_valid[index] = {id: $(this).attr("id"), name: $(this).text()};
                // get index max in a row which seat must exist
                if($(this).text()){
                    number_max_valid = index;
                }
                // get index min in a row which seat could select
                if($(this).text() && number_min_valid == 0 && ($(this).hasClass('available') || 
                    $(this).hasClass('selected') || $(this).hasClass('unavailable'))){
                    number_min_valid = index;
                }
            });

            // Total seats on 1 row, check condition > 3
            total_available_valid = $(".parent_seat_" + key +">.available, .parent_seat_" + key +">.selected").length;

            // get numer of seat selected
            number_column_valid = parseInt(this.settings.label.substring(1,3));

            // check total seat could select must > 3 and type seat != couple then select free
            if(total_available_valid > 3 && this.settings.character != "c"){
                // Seat => []: trong, [x]: da chon, [v]: dang chon
                // [][v][v] -> fail
                if(number_column_valid == (number_min_valid + 1) && 
                    sc.get(seats_row_valid[number_min_valid].id).settings.status == "available"){
                        status_valid = true;
                        return false;
                } // [v][v][x] -> fail
                else if((number_column_valid == (number_max_valid - 1)) && 
                    sc.get(seats_row_valid[number_max_valid].id).settings.status == "available"){
                        status_valid = true;
                        return false;
                } // [][][v][][x] -> failm [][][v][][v] -> fail
                else if(number_column_valid > (number_min_valid + 1) && 
                    (sc.get(seats_row_valid[number_column_valid-1].id).settings.status == "available") &&
                    ((sc.get(seats_row_valid[number_column_valid-2].id).settings.status == "unavailable") ||
                    (sc.get(seats_row_valid[number_column_valid-2].id).settings.status == "selected")) ){
                        status_valid = true;
                        return false;
                } // [x][][v][][] -> failm [v][][v][][] -> fail
                else if((number_column_valid < (number_max_valid - 1)) && 
                    (sc.get(seats_row_valid[number_column_valid+1].id).settings.status == "available") &&
                    ((sc.get(seats_row_valid[number_column_valid+2].id).settings.status == "unavailable") ||
                    (sc.get(seats_row_valid[number_column_valid+2].id).settings.status == "selected"))){
                        status_valid = true;
                        return false;
                }
            }

            // Remove class, button next time not to override
            $('#seat-map .seatCharts-row').removeClass('parent_seat_'+key);
        });

        if(status_valid){
            messages_valied_seat();
            return false;
        }else {
            $('#member_card_modal').modal('show');
        }
        
    });
}