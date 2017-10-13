$(document).ready(function() {
    $('#change_password').on('change', function(){
        if ($(this).is(':checked')) {
            $('.metiz-changepass').css({ "display": "block" });
        }else{
            $('.metiz-changepass').css({ "display": "none" });
        }
    });
});