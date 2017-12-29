$(document).ready(function() {
    //Filter News
	$('select#blog-filter').change(function() {
		var filter = $(this).val();
		$.ajax({
			type: "POST",
			url: "/blog/",
			data: {'order_column': filter},
			success: function(data) {
				$(".blog-custom>article").html(data);
			}
		});
	});

	// Paginator page for blog
	// check total page let remove button load more
	var total_page = parseInt($('.load-more').attr('data-total-page'));
	
	if(parseInt($('.load-more').attr('data-page')) > total_page){
		$('.blog-custom>.text-center button').remove();
	}

	$('#load-more-blogs').on('click', function(e){
		e.preventDefault();
		$(this).prop('disabled', true);
		var page = parseInt($(this).attr('data-page'));
		$.ajax({
			url: "/blog/",
			type: 'POST',
			data: {
				'page': page,
			},
			crossDomain:false,
			context: this,
		})
		.done(function(response) {
			$('.blog-custom>article').append(response);
			// Check total page let remove button load more
			if(page >= total_page){
				$('.blog-custom>.text-center button').remove();
			}
			
			// increase the value page +1
			$(this).attr('data-page',page + 1);

			$(this).prop('disabled', false);
		})
		.fail(function(error) {
			$('.blog-custom>.text-center button').remove();
			displayMsg();
			if(error.status == 400){
        		$('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
			}else{
				$('.msg-result-js').html(msgResult("Error load more movie", "danger"));
			}
		});
	});
});
