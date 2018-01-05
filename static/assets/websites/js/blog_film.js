$(document).ready(function() {

	// Call ajax load page
	loadAjaxBlog();

    //Filter News
	$('select#blog-filter').change(function() {
		// When user choose select box return default data-page =2
		$("#load-more-blogs").attr('data-page', 2);
		// check total page let remove button load more
		var total_page = parseInt($('.load-more').attr('data-total-page'));
		if(parseInt($('.load-more').attr('data-page')) <= total_page){
			$('.blog-custom>.text-center button').show();
		}
		loadAjaxBlog();
	});
	// Create function load Ajax
	function loadAjaxBlog() {
		var filter = $('select#blog-filter').val();
		$.ajax({
			type: "POST",
			url: "/blog/",
			data: {
				'order_column': filter
			},
			success: function(data) {
				$(".blog-custom>article").html(data);
			},
			error: function(error){
				$('.blog-custom>.text-center button').hide();
				displayMsg();
				if(error.status == 400){
	        		$('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
				}else{
					$('.msg-result-js').html(msgResult("Error load more movie", "danger"));
				}
				}
		});
	}

	$('#load-more-blogs').on('click', function(e){
		e.preventDefault();
		$(this).prop('disabled', true);
		var page = parseInt($(this).attr('data-page'));
		// Check totla page to paginator
		var total_page = parseInt($('.load-more').attr('data-total-page'));
		$.ajax({
			url: "/blog/",
			type: 'POST',
			data: {
				'page': page,
				'order_column': $('select#blog-filter').val()
			},
			crossDomain:false,
			context: this,
		})
		.done(function(response) {

			$('.blog-custom>article').append(response);
			// Check total page let remove button load more
			if(page >= total_page){
				$('.blog-custom>.text-center button').hide();
			}
			
			// increase the value page +1
			$(this).attr('data-page',page + 1);

			$(this).prop('disabled', false);
		})
		.fail(function(error) {
			$('.blog-custom>.text-center button').hide();
			displayMsg();
			if(error.status == 400){
        		$('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
			}else{
				$('.msg-result-js').html(msgResult("Error load more movie", "danger"));
			}
		});
	});
});
