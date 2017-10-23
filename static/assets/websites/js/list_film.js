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
	// data demo
	var list_film = [
		{
			"id": 4,
			"name": "Con Giong Bao",
			"poster": "/assets/websites/images/news/Kingsman_350_X_495.jpg",
			"director": "Dong chung",
			"cast": "Tom",
			"time_running": 111,
			"release_date": "2017-4-5",
			"language": "Tieng Anh",
			"description": "hahaahaha",
			"trailer": "https://www.youtube.com/watch?v=lWX5Atc6QnY",
			"genre":{"name": "Hanh Dong"},
			"rated":{"name":"c18"}
		},
		{
			"id": 10,
			"name": "Vua bien ca",
			"poster": "/assets/websites/images/news/Kingsman_350_X_495.jpg",
			"director": "Dong chung",
			"cast": "Tom",
			"time_running": 111,
			"release_date": "2017-4-3",
			"language": "Tieng Anh",
			"description": "hahaahaha",
			"trailer": "https://www.youtube.com/watch?v=lWX5Atc6QnY",
			"genre":{"name": "Hanh Dong"},
			"rated":{"name":"c16"}
		}
	];

	// movie html, need set data for movie html in movie_showing(movie)
	function movie_showing(movie){
		return 	'<li class="film-lists">'
					+'<div class="product-images">'
						+'<a href="/film/detail/'+ movie.id +'" title="'+ movie.name +'" class="product-image">'
							+'<img src="/media/'+ movie.poster +'" alt="'+ movie.name +'">'
						+'</a>'
					+'</div>'
					+'<div class="product-info">'
						+'<h2 class="product-name">'
						+'<a href="/film/detail/'+ movie.id +'" title="'+ movie.name +'">'+ movie.name +'</a></h2>'
						+'<div class="metiz-movie-info">'
							+'<span class="metiz-info-bold">Thể loại: </span>'
							+'<span class="metiz-info-normal">'+ movie.genre.name +'</span>'
						+'</div>'
						+'<div class="metiz-movie-info">'
							+'<span class="metiz-info-bold">'+ movie.time_running +' Phút | '
							+'<span class="rated-'+ movie.rated.name +'">'+ movie.rated.name +'</span></span>'
						+'</div>'
						+'<div class="metiz-movie-info">'
							+'<span class="metiz-info-bold">Khởi chiếu: </span>'
							+'<span class="metiz-info-normal">'+ movie.release_date +'</span>'
						+'</div>'
					+'</div>'
					
					+'<ul class="add-to-links">'
						+'<li>'
							+'<div class="fb-like fb_iframe_widget" data-href="http://elearning.vooc.vn/" data-layout="button_count" '
							+'data-action="like" data-show-faces="true" data-share="true">'
                            +'</div>'
						
						+'<li>'
							+'<button type="button" title="Đặt vé" class="button">Đặt vé</button>'
						+'</li>'
					+'</ul>'
				+'</li>';
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
			var html = '';

			// for from data reponse set function movie_showing(movie)
			$.each(list_film, function(key, value) {
				html += movie_showing(value);
			});
			
			$('.metiz-movies>ul').append(html);

			$(this).prop('disabled', false);
		})
		.fail(function() {
			alert("error");
		});
	});
});
$(document).ajaxComplete(function(){
    try{
        FB.XFBML.parse(); 
    }catch(ex){}
});