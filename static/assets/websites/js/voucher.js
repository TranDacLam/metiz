$(document).ready(function() {
	$('#btn_get_voucher').click(function(e) {
		$('#btn_get_voucher').prop('disabled', 'disabled');
		$.ajax({
			type: "POST",
			url: "/voucher/",
			success: function(data) {
				if (typeof data.message !== "undefined") {
					$("#message").text(data.message);
					$('.msg-result-js').html(msgResult(data.message, "danger"));
					displayMsg();
				} else {
					$("#code_str").val(data.code);
					JsBarcode("#code_img", data.code, {
					  	format:"CODE39",
					  	displayValue:false,
					  	fontSize:24
					});
					$('#get_voucher_modal').modal('show');
				}
				$('#btn_get_voucher').prop('disabled', false);

			},
			error: function(error){
				$('.msg-result-js').html(msgResult("Internal Server Error", "danger"));
				displayMsg();
				$('#btn_get_voucher').prop('disabled', false);
			}
		});
	});

	$("#copy_btn").click(function(e) {
		var $temp = $("<input>");
	  	$("body").append($temp);
	  	$temp.val($('#code_str').val()).select();
	  	document.execCommand("copy");
	  	$temp.remove();
	  	$(this).find('.btn-copy-text').text('COPIED')
	});
});