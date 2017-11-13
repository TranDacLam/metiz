$(document).ready(function() {
    // format money page payment_return
    var money_total_return = $('.amout-pay-return').text();
    $('.amout-pay-return').text(money_total_return.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1."));
});