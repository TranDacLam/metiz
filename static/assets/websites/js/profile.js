$(document).ready(function() {
    $('.my-account .buttons-set button').on('click',function(){
        $(this).prop('disabled', true);
    });
});