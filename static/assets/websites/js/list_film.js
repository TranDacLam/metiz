// js for showing.html, arthouse.html
 
// lay gia tri lon nhat cua height, roi dat cho tat ca phan tu
function equalizeHeights(selector) {
		var heights = new Array();
		// Loop to get all element heights
		$(selector).each(function() {

			// Need to let sizes be whatever they want so no overflow on resize
			$(this).css('min-height', '0');
			$(this).css('max-height', 'none');
			$(this).css('height', 'auto');

			// Then add size (no units) to array
	 		heights.push($(this).height());
		});

		// Find max height of all elements
		var max = Math.max.apply( Math, heights );

		// Set all heights to max height
		$(selector).each(function() {
			$(this).css('height', max + 'px');
		});	
	}
$(window).on('load', function(event) {
	// Fix heights on page load
		equalizeHeights('.product-info');
		$('li.category3').find('a').contents().unwrap();
		// Fix heights on window resize
		var iv = null;
		$(window).resize(function() {
			if(iv !== null) {
				window.clearTimeout(iv);
			}

			// Needs to be a timeout function so it doesn't fire every ms of resize
			iv = setTimeout(function() {
	      			equalizeHeights('.product-info');
			}, 120);
			$('li.category3').find('a').contents().unwrap();
		});
});

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

	//  load more
	// movie html, need set data for movie html in movie_showing(movie)
	function movie_showing(movie){
		return '<li class="film-lists">'
						+'<div class="product-images">'
							+'<a href="/film/detail/13/" title="Kingsman" class="product-image">'
								+'<img src="/media//assets/websites/images/news/new_03.png" alt="Kingsman">'
							+'</a>'
						+'</div>'
						
						+'<div class="product-info" style="min-height: 0px; max-height: none; height: 84px;">'
							+'<h2 class="product-name">'
							+'<a href="/film/detail/13/" title="Kingsman">Kingsman</a></h2>'
							+'<div class="metiz-movie-info">'
								+'<span class="metiz-info-bold">Thể loại: </span>'
								+'<span class="metiz-info-normal">Hoat hinh</span>'
							+'</div>'
							+'<div class="metiz-movie-info">'
								+'<span class="metiz-info-bold">140 Phút | <span class="rated-c12">c12</span></span>'
							+'</div>'
							+'<div class="metiz-movie-info">'
								+'<span class="metiz-info-bold">Khởi chiếu: </span>'
								+'<span class="metiz-info-normal">26-09-2017</span>'
							+'</div>'
						+'</div>'
						+'<ul class="add-to-links">'
							+'<li>'
								+'<div class="fb-like fb_iframe_widget" data-href="http://elearning.vooc.vn/" data-layout="button_count"' 
								+'data-action="like" data-show-faces="true" data-share="true"> </div>'
							+'</li>'
							
							+'<li>'
								+'<button type="button" title="Đặt vé" class="button">Đặt vé</button>'
							+'</li>'
						+'</ul>'
					+'</li>'
	}

	$('#load-more').on('click', function(e){
		e.preventDefault();
		$(this).prop('disabled', true);
		var page = parseInt($(this).attr('data-page'));
		$.ajax({
			url: '/showing/',
			type: 'get',
			data: {
				'page': page,
			},
			crossDomain:false,
			context: this,
		})
		.done(function(response) {
			$(this).attr('data-page',page + 1);

			// Check condition length record hide button "xem them"

			var html = '';

			// for from data reponse set function movie_showing(movie)
			// $.each(response, function(key, value) {
			// 	movie_showing(value);
			// })
			
			// example
			for(i=1; i<5; i++){
				html += movie_showing(response);
			}

			$('.metiz-movies>ul').append(html);

			$(this).prop('disabled', false);
		})
		.fail(function() {
			alert("error");
		});
	});
});


