$(document).ready(function() {
    // active menu profile
    $('#info-member-card').addClass('active');

    setBarcode();

    function setBarcode(){
        var settings = {
            output: 'css',
            bgColor: '#FFFFFF',
            color: '#000000',
            barWidth: '1',
            barHeight: '50'
        };
        var type = 'code128';
        var barcode = $('input[name=barcode_member_card]').val();

        $('#barcode-member-card').barcode(
            barcode, // Value barcode (dependent on the type of barcode)
            type, // type (string)
            settings
        );
    }

});