$(document).ready(function() {
	// Paginator page for blog
	// check total page let remove button load more
	var total_page = parseInt($('.load-more').attr('data-total-page'));
	
	if(parseInt($('.load-more').attr('data-page')) > total_page){
		$('.blog-custom>.text-center button').hide();
	}

	// Set filter default is created( fix bugs back on browser)
	$('select#blog-filter').val('-created');

    //Filter News
	$('select#blog-filter').change(function() {
		$("#load-more-blogs").attr('data-page', 2);
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
			data: {'order_column': filter},
			success: function(data) {
				$(".blog-custom>article").html(data);
			},
			error: function(){
				alert("error");
			}
		});
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
