$(document).ready(function() {

	// Call ajax load page
	loadAjaxBlog();

    //Filter News
	$('select#blog-filter').change(function() {
		// When user choose select box return default data-page =2
		$("#load-more-blogs").attr('data-page', 2);
		// Remove total page element before call ajax. 
		$('#data-total-page').remove();
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
				// paginator for total-page < 9 page
				// hide button load-more
				var total_page = parseInt($('#data-total-page').val());
				var page = parseInt($("#load-more-blogs").attr('data-page'));
				if(page > total_page){
					$('.blog-custom>.text-center button').hide();
				} else {
					$('.blog-custom>.text-center button').show();
				}
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
		var total_page = parseInt($('#data-total-page').val());
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
