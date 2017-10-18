$(document).ready(function() {
	$('#create_form').validate({
		rules:{
			order_id:{
				required: true
			},
			trans_date:{
				required: true,
				validateDate: true
			},
		},
	})
	$.datetimepicker.setLocale('vi');
	$('#trans_date').datetimepicker({
		timepicker:false,
		format:'d-m-Y',
	});
	$.validator.addMethod(
      "validateDate",
      function (value, element) {
        // put your own logic here, this is just a (crappy) example 
        return value.match(/^\d\d?\-\d\d?\-\d\d\d\d$/);
      },
      "Please enter a date in the format dd-mm-yyyy"
    );
});