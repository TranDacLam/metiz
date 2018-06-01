$(document).ready(function() {

    // active menu profile
    $('#transaction-history').addClass('active');
    $.ajax({
		url: "/profile/transaction_history/",
		type: 'POST',
		data: {
			'page': 2
		},
		crossDomain:false,
		context: this,
	})
	.done(function(response) {

		console.log(response);
	})
	.fail(function(error) {
		console.log(error);
	});
});