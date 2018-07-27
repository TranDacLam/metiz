$(document).ready(function() {
    // if input is_public checked, hidden user
    if($("#id_is_public").is(':checked')){
        $(".grp-cells-1.users ").css('display', 'none');
    };
    // hidden user when check
    $("#id_is_public").on('click', function(){
        if($("#id_is_public").is(':checked')){
            $(".grp-cells-1.users").css('display', 'none');
        }else{
            $(".grp-cells-1.users").css('display', 'block');
        }
    });
});