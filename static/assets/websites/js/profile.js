$(document).ready(function() {

    // active menu profile
    $('#profile').addClass('active');

    var val_required = 'Trường này là bắt buộc';
    var val_date = 'Nhập ngày theo định dạng dd-mm-yyyy';

    // validate phone, persional only number
    var selectorPhone = $("#profile-validate input[name=phone]");
    var selectorPersonal = $("#profile-validate input[name=personal_id]");
    // Call back validOnlyNumber layout.js 
    validOnlyNumber(selectorPhone, selectorPhone.val());
    validOnlyNumber(selectorPersonal, selectorPersonal.val());

    // page profile
    $("#profile-validate").validate({
        rules: {
            full_name: { 
                required: true,
                rangelength: [1, 70],
            },
            birth_date: { 
                required: true,
                validateDate: true,
            },
            phone: {
                required: true,
                number: true,
                minlength: 9,
                validatePhone: true,
            },
            email:{
                required: true,
            },
            personal_id: {
                number: true,
                rangelength:[9, 9],
            }
        },
        messages:{
            full_name: {
                required: val_required,
                rangelength: "Họ và tên chứa ít nhất 1 kí tự và nhiều nhất 70 kí tự",
            },
            birth_date: {
                required: val_required,
                validateDate: val_date,
            },
            phone: {
                required: val_required,
                number: 'Vui lòng chỉ nhập số',
                minlength: "Số điện thoại không hợp lệ",
                validatePhone: "Số điện thoại không hợp lệ",
            },
            email: {
                required: val_required,
            },
            personal_id: {
                number: 'Vui lòng chỉ nhập số',
                rangelength: 'Vui lòng nhập CMND gồm 9 chữ số'
            }  
        }
    });
    // format birthday
    $.validator.addMethod(
      "validateDate",
      function (value, element) {
        // put your own logic here, this is just a (crappy) example 
        return value.match(/^\d\d?\-\d\d?\-\d\d\d\d$/);
      },
      message_translate.validateDate
    );

    // Validate phone number
    // Can enter 0 number at the end or middle but not at the beginning.
    // Check the first characters and remove if it equal == 0
    // Then replace input with new value
    // Use profile
    
    //Prevent to enter 0(zero) number at the second character
    $('.textPhone').on('keydown',function(event){
        var caretPos = this.selectionStart;
        var keyCode = event.which || event.keyCode;
        var isZero = keyCode == 48 || keyCode == 96;
        var valPhone = $(this).val();
        if (caretPos < 2 && valPhone.startsWith("0") && isZero) {
            return false;
        } 
    });
    // Call event Paste 
     $('.textPhone').bind('paste', function(e) {
        var pasteText = e.originalEvent.clipboardData.getData('Text');
        $(this).val(removeBeforePhoneNumber(pasteText)); 
        return false;
    });
    $('.textPhone').on('blur',function(event){ 
        var valPhone = $(this).val();
        $(this).val(removeBeforePhoneNumber(valPhone));
    });
        // set datetimepicker for signup and profile

    // Get current date 5 year ago
    var date_now = new Date();
    var date_day = ("0" + date_now.getDate()).slice(-2);
    var date_month = ("0" + (date_now.getMonth() + 1)).slice(-2);
    var date_today = (date_now.getFullYear() - 5) + "-" + (date_month) + "-" + (date_day);

    $('#birth_date:not(.readonly)').datebox({
            mode: "calbox",
            beforeToday: true,
            useFocus: true,
            useButton: false,
            useHeader: false,
            calShowDays: false,
            calUsePickers: true,
            calHighToday:true,
            themeDatePick: 'warning',
            defaultValue: date_today,
            calYearPickMax: 'NOW',
            calYearPickMin: 100,
            beforeOpenCallback: function(){
                //if having error hide errortext 
                if($('#birth_date-error').length){
                    $('.input-group #birth_date-error').css('display', 'none');// of jquery validate
                    $('#birth_date').css('color','#555');
                }
            },
            closeCallback: function(){
                //if date valid show tick image
                if($('#birth_date').val() != ''){
                    $('.birthday-inline #birth_date_valid').css('display', 'inline-block');
                }else{
                    $('.input-group #birth_date-error').css('display', 'inline-block');
                }
            },
        });

    if( navigator.userAgent.match(/iPhone|iPad|iPod|Android/i)){
        $('#birth_date:not(.readonly)').datebox({
            mode: "flipbox",
            beforeToday: true,
            useFocus: true,
            useButton: false,
            useHeader: true,
            defaultValue: date_today,
            beforeOpenCallback: function(){
                $('body').css('overflow-y','hidden');
            },
            closeCallback: function(){
                $('body').css('overflow-y','scroll');
            }
        });
    }
    $('#birth_date:not(.readonly)').attr("readonly", false);
    // *end*

    // CHOOSE CITY AND DISTRICT
    // Step 1: Load data for city and district, but district hide
    // Step 2: Choose city, hide all district, show district appropriate, 
    // Step 3: Change city, hide all district, show district appropriate, 

    // *** User for Page profile and signup ***
    // *begin*
    // data city 
    var list_city = {'Đà Nẵng': ['Hải Châu', 'Thanh Khê', ' Sơn Trà', 'Ngũ Hành Sơn', 'Liên Chiểu', 'Hòa Vang', ' Cẩm Lệ', ' Hoàng Sa'], 
    'Hà Nội': [' Hoàn Kiếm', 'Ba Đình', 'Hai Bà Trưng'], 
    'Hồ Chí Minh': ['1','2','3', '4', '5', '6', 'Tân Bình'], 'Khác': ['Khác']};
    
    // load city and district but district hide
    var current_city = $("#id_city").val();
    var current_district = $("#id_district").val();

    // Check browser there must be IE
    var isIE = window.navigator.userAgent.indexOf("Trident");
    var isIOS = navigator.userAgent.match(/(\(iPod|\(iPhone|\(iPad)/);
    if(isIE > 0 || isIOS){
        // Browser IE

        // *** CHOOSE CITY AND DISTRICT ***
        // Step 1: Get current city and current district
        // Step 2: 
        // - TH1: load first page, call function selectDistrict
        // --- Get all district of current city
        // - TH2: change city
        // --- Remove all list city and dictrict, not remove "Chon Quan" (disavled).
        // --- callback function selectDictrict, back TH1.

        selectDistrict(list_city, current_city);
        // funtion show district for each city
        function selectDistrict(list_city, current_name_city){
            $.each(list_city, function(index, val) {
                var name_city= index;
                if(current_name_city && name_city==current_name_city){
                    $('.list-city').append('<option value="' + name_city + '" selected>' +name_city + '</option>');
                }else{
                    $('.list-city').append('<option value="' + name_city + '">' +name_city + '</option>');    
                }

                if(current_name_city && name_city==current_name_city){
                    $.each(val, function(index, val) {
                        if(current_district && val==current_district){
                            $('.list-district').append('<option value="' + val + '" class = "' + name_city + '" selected>' +val + '</option>');
                        }else{
                            $('.list-district').append('<option value="' + val + '" class = "' + name_city + '">' +val + '</option>');     
                        }
                    });
                }
            });
        };

        $('.list-city').on('change', function(event) {
            event.preventDefault();
            var name_city= $('.list-city').val();
            $('.list-city option').not(":disabled").remove();
            $('.list-district option').not(":disabled").remove();
            $('.list-district option').attr('selected', 'selected');
            selectDistrict(list_city, name_city);
        });
    }else{
        // Browser not IE
        $.each(list_city, function(index, val) {
            var name_city= index;
            if(current_city && name_city==current_city){
                $('.list-city').append('<option value="' + name_city + '" selected>' +name_city + '</option>');
            }else{
                $('.list-city').append('<option value="' + name_city + '">' +name_city + '</option>');    
            }
            
            $.each(val, function(index, val) {
                if(current_city && name_city==current_city){
                    if(current_district && val==current_district){
                        $('.list-district').append('<option value="' + val + '" class = "' + name_city + ' show-district" selected>' +val + '</option>');
                    }else{
                        $('.list-district').append('<option value="' + val + '" class = "' + name_city + ' show-district">' +val + '</option>');     
                    }
                }
                else{
                    if(current_district && val==current_district){
                        $('.list-district').append('<option value="' + val + '" class = "' + name_city + '" selected>' +val + '</option>');
                    }else{
                        $('.list-district').append('<option value="' + val + '" class = "' + name_city + '">' +val + '</option>');     
                    }
                }
            });
        });
        $('.list-district').children().hide();
        $('.list-district .show-district').css('display','block');

        // funtion show district for each city
        function selectDistrict(list_city){
            var name_city= $('.list-city').val();
            $('.list-district').children().hide();
            $('.list-district option').first().css('display', 'block').prop("selected", true);
            $.each(list_city, function(index, val) {
                if (index == name_city ) {
                    $('.list-district option').each(function(index, el) {
                        if ($(this).hasClass(name_city)) {
                            $(this).show();
                        }
                    });
                }
             });
        };

        $('.list-city').on('change', function(event) {
            event.preventDefault();
            selectDistrict(list_city);
        });
    }
});
// Press key tab open popup calendar
// Close popup calender when tab press another
$(document).keydown(function(objEvent) {
    if (objEvent.keyCode == 9) {  //tab pressed
        $(".profile-custom .ui-datebox-container").css("display","none");
    }
})