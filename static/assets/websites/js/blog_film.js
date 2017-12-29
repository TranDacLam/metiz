$(document).ready(function() {
    //Filter News
	$('select#blog-filter').change(function() {
		var filter = $(this).val();
		$.ajax({
			type: "POST",
			url: "/blog/",
			data: {'order_column': filter},
			success: function(data) {
				console.log($(".blog-custom>article").html(data));
			}
		});
	});
});
