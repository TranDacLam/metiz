$(document).ready(function() {
	$('#create_form').validate({
		rules:{
			order_id:{
				required: true
			},
			amount:{
				required: true,
				number: true
			},
			order_desc:{
				required: true,
			},
			trans_date:{
				required: true,
				validateDate:true
			},
			trans_time:{
				required: true,
				validateTime: true
			}
		},
	})
	$.datetimepicker.setLocale('vi');
	$('#trans_date').datetimepicker({
		timepicker:false,
		format:'d-m-Y',
	});
	$('#trans_time').datetimepicker({
		datepicker:false,
		format:'H:i',
		step: 30,
	});
	$.validator.addMethod(
      "validateDate",
      function (value, element) {
        // put your own logic here, this is just a (crappy) example 
        return value.match(/^\d\d?\-\d\d?\-\d\d\d\d$/);
      },
      "Please enter a date in the format dd-mm-yyyy"
    );
    $.validator.addMethod(
      "validateTime",
      function (value, element) {
        // put your own logic here, this is just a (crappy) example 
        return value.match(/^\d\d?\:\d\d$/);
      },
      "Please enter a time in the format H:i"
    );
});