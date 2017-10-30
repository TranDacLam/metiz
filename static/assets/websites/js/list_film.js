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

	// trim string name and category film
	trimNameMovie();

	//  load more
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
							+'<span class="metiz-info-normal">Hanh dong</span>' // movie.genre.name
						+'</div>'
						+'<div class="metiz-movie-info">'
							+'<span class="metiz-info-bold">'+ movie.time_running +' Phút | '
							+'<span class="rated-c18">c18</span></span>' // movie.rated.name
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

	var coutMovie = parseInt($('.load-more').attr('data-count-movie'));
	if(coutMovie < 12){
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
			if(page >= response.total_page){
				$('.metiz-movies>.text-center button').remove();
			}
			
			$(this).attr('data-page',page + 1);
			var html = '';

			// for from data reponse set function movie_showing(movie)
			$.each(response.data, function(key, value) {
				html += movie_showing(value);
			});
			
			$('.metiz-movies>ul').append(html);

			$(this).prop('disabled', false);
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

$(document).ajaxComplete(function(){
    try{
        FB.XFBML.parse(); 
        trimNameMovie();
    }catch(ex){}
});

// trim string name and category film
function trimNameMovie(){
	$('.metiz-movies .film-lists').each(function() {
            var name_film = $(this).find('.product-name a').text();
            var cate_film = $(this).find('.product-cate').text();
            if(name_film.length > 20){
            	var trimName= name_film.substring(0, 20) + "...";
            	$(this).find('.product-name a').text(trimName);
            }
            if(cate_film.length > 9){
            	var trimCate = cate_film.substring(0, 10) + "...";
            	$(this).find('.product-cate').text(trimCate);
            }
     });
}