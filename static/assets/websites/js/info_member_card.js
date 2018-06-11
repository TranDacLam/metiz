$(document).ready(function() {
    // active menu profile
    $('#info-member-card').addClass('active');

    // barde code use barcode jquery
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

    setBarcode();

    // Get gift
    $.ajax({
        url: '/api/gift/claiming_points/',
        type: 'GET',
        dataType: 'json',
        crossDomain:false,
        context: this,
    })
    .done(function(response) {
        var html = '';
        // set list gift into html
        if(response.length > 0){
            $.each(response, function(key, value) {
                html += '<tr>'
                            + '<td>'+ value.name +'</td>'
                            + '<td>'+ value.point +'</td>'
                        + '</tr>';
            });
        }else{
            html += '<tr class="text-center">'
                        + '<td colspan="2">Chưa có mục đổi quà nào</td>'
                    + '</tr> ';
        }
        
        // append list html
        $('.info-member-card .info-mc-2 table tbody').append(html);
    })
    .fail(function(error) {
        displayMsg();
        if(error.status == 400){
            $('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
        }else{
            $('.msg-result-js').html(msgResult("Lỗi danh mục đổi quà.", "danger"));
        }
    })

    $('#form-member-card').validate({
        rules: {
            card_member: { 
                required: true
            }
        },
        messages:{
            card_member: {
                required: 'Mã số thẻ không được để trống.'
            }
        },
        submitHandler: function(form) {
            // disable button 
            $(this).prop('disabled', true);
            // get card member
            var card_member = $("#form-member-card input[name=card_member]").val();
            var index_card = card_member.indexOf("*");
            var card_member_sub = card_member;
            if(index_card != -1){
                var card_member_sub = card_member.substring(0, index_card);
            }

            $.ajax({
                url: '/api/card_member/link/',
                type: 'POST',
                data: JSON.stringify({
                    "card_member": card_member_sub
                }),
                headers: { 
                    'Content-Type': 'application/json'
                },
                dataType: 'json',
                crossDomain:false,
                context: this
            })
            .done(function(response) {
                // show message success
                displayMsg();
                $('.msg-result-js').html(msgResult('Liên kết thẻ thành công.', "success"));
                // reload page after 2s
                setTimeout(function(){ 
                    location.reload();
                }, 2000);
            })
            .fail(function(error) {
                $(this).prop('disabled', false);
                displayMsg();
                if(error.status == 400){
                    $('#card_member-error').text(error.responseJSON.message);
                    $('#card_member-error').css('display', 'block');
                }else{
                    $('.msg-result-js').html(msgResult("Lỗi liên kết thẻ thành viên.", "danger"));
                }
            })
        }
    });

});