$(document).ready(function($) {
	$('#about-arthouse_contents').css('display','none');
	$('#about-arthouse').click(function(event) {
		/* Act on the event */
		$('#about-arthouse_contents').css('display','block');
		$('#arthouse-home_contents').css('display','none');
	});
	$('#arthouse-home').click(function(event) {
		/* Act on the event */
		$('#about-arthouse_contents').css('display','none');
		$('#arthouse-home_contents').css('display','block');
	});

    // active popup
    $('.open-popup-list-movie').magnificPopup({
        type: 'inline',
        midClick: true,
        enableEscapeKey: false,
        fixedContentPos: true,
    });
    
	//  load more
	// check total page let remove button load more
	var total_page = parseInt($('.load-more').attr('data-total-page'));
	if(parseInt($('.load-more').attr('data-page')) > total_page){
		$('.metiz-movies>.text-center button').remove();
	}

	$('#load-more').on('click', function(e){
		e.preventDefault();
		$(this).prop('disabled', true);
		var page = parseInt($(this).attr('data-page'));
		if($(this).attr('data-url') == "showing"){
			url = '/showing/';
		}else{
			url = '/comingsoon/';
		}
		$.ajax({
			url: url,
			type: 'get',
			data: {
				'page': page,
			},
			crossDomain:false,
			context: this,
		})
		.done(function(response) {
			$('.metiz-movies>ul').append(response);
			// Check total page let remove button load more
			if(page >= total_page){
				$('.metiz-movies>.text-center button').remove();
			}
			
			// increase the value page +1
			$(this).attr('data-page',page + 1);

			$(this).prop('disabled', false);

			// // ajax success load popup 
			$('.open-popup-list-movie').magnificPopup({
	          	type: 'inline',
	          	midClick: true,
		    });

			// ajax success load button facebook
			FB.XFBML.parse(); 
		})
		.fail(function(error) {
			$('.metiz-movies>.text-center button').remove();
			displayMsg();
			if(error.status == 400){
        		$('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
			}else{
				$('.msg-result-js').html(msgResult("Error load more movie", "danger"));
			}
		});
	});
});