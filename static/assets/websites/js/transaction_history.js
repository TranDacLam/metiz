$(document).ready(function() {

    // active menu profile
    $('#transaction-history').addClass('active');

    // item transaction history
    function transactionHistory(item){
        return  '<div class="col-md-12 info-th-2">'
                    + ' <div class="col-md-7 th-1-des">'
                        + '<p><label>Mã đặt vé: </label> '+ item.order_id +'</p>'
                        + '<p><label>Trạng thái: </label> Thành công</p>'
                        + '<p><label>Mô tả đặt vé: </label> '+ item.order_desc +'</p>'
                        + '<p><label>Chi phí: </label> '+ item.amount +'</p>'
                    + '</div>'
                    + '<div class="col-md-5 th-2-des">'
                     +   '<img src="'+ STATIC_URL + (item.image ? item.image : 'assets/images/default.jpg') +'" alt="'+ item.order_id +'"/>'
                    + '</div>'
                   +  '<div class="col-md-12 th-3-des"><hr/></div>'
                + '</div>';
    }

    // page current set 1
    var page_current = 1; 

    function loadTransactionHistory(){
        // load list transaction history
        $.ajax({
            url: "/profile/transaction_history/",
            type: 'POST',
            data: {
                'page': page_current
            },
            crossDomain:false,
            context: this
        })
        .done(function(response) {
            var html = '';
            // get total page
            total_page_trans = response.total_page;
            // chekc total page let remove button load more
            if(page_current >= total_page_trans){
                $('.transaction-history .btn-load-more').remove();
            }else{
                $('.transaction-history .btn-load-more').css('display', 'block');
            }
            // set total item
            $('.total_item_trans').text(response.total_item);
            page_current++;

            // for from data reponse set function transactionHistory(list)
            $.each(response.list_transaction, function(key, value) {
                html += transactionHistory(value);
            });
            
            // append list html
            $('.transaction-history .info-th').append(html);
        })
        .fail(function(error) {
            displayMsg();
            if(error.status == 400){
                $('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
            }else{
                $('.msg-result-js').html(msgResult("Error load more transaction history", "danger"));
            }
        });
    }

    // run when page load
    loadTransactionHistory();

    // run ajax when have event click load more
    $('.btn-load-more').click(function(){
        loadTransactionHistory();
    })
});