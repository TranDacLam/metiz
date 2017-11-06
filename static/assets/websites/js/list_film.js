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

	// format date time
	function getDate(applyDate){
        return applyDate.replace(/([0-9]{4})\-([0-9]{2})\-([0-9]{2})/g, '$3 - $2 - $1');
    }
	
	// trim string name and category film
	function trimNameMovie(name, len){
		if(name.length >= len){
			var trimName= name.substring(0, len) + "...";
			return trimName;
		}
	    return name;
	}

	//  load more
	// list movie when load more at film showing, comming soon. Callback event click #load-more
	function movie_showing(movie){
		return 	'<li class="film-lists">'
					+'<div class="product-images">'
						+'<a href="/film/detail/'+ movie.id +'" title="'+ movie.name +'" class="product-image">'
							+'<img src="/media/'+ movie.poster +'" alt="'+ movie.name +'">'
						+'</a>'
					+'</div>'
					+'<div class="product-info">'
						+'<h2 class="product-name">'
						+'<a href="/film/detail/'+ movie.id +'" title="'+ movie.name +'">'+ trimNameMovie(movie.name, 21) +'</a></h2>'
						+'<div class="metiz-movie-info">'
							+'<span class="metiz-info-bold">Thể loại: </span>'
							+'<span class="metiz-info-normal">'+ trimNameMovie(movie.genre__name, 12) +'</span>'
						+'</div>'
						+'<div class="metiz-movie-info">'
							+'<span class="metiz-info-bold">'+ movie.time_running +' Phút | '
							+'<span class="rated-'+ movie.rated__name +'">'+ movie.rated__name +'</span></span>'
						+'</div>'
						+'<div class="metiz-movie-info">'
							+'<span class="metiz-info-bold">Khởi chiếu: </span>'
							+'<span class="metiz-info-normal">'+ getDate(movie.release_date) +'</span>'
						+'</div>'
					+'</div>'
					
					+'<ul class="add-to-links">'
						+'<li>'
							+'<div class="fb-like fb_iframe_widget" data-href="http://elearning.vooc.vn/" data-layout="button_count" '
							+'data-action="like" data-show-faces="true" data-share="true">'
                            +'</div>'
						
						+'<li>'
							+'<button href="#test-popup" type="button" title="Đặt vé" class="button open-popup-list-movie popup-movie-schedule" '
							+'data-movie-api-id="'+ movie.movie_api_id +'">Đặt vé</button>'
						+'</li>'
					+'</ul>'
				+'</li>';
	}

	// check list movie if < 12 then remove button load more
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
			console.log(response);
			$('.metiz-movies>ul').append(response);
			// Check total page let remove button load more
			// if(page >= response.total_page){
			// 	$('.metiz-movies>.text-center button').remove();
			// }
			
			// // increase the value page +1
			// $(this).attr('data-page',page + 1);
			// var html = '';

			// // for from data reponse set function movie_showing(movie)
			// $.each(response.data, function(key, value) {
			// 	html += movie_showing(value);
			// });
			
			// $('.metiz-movies>ul').append(html);

			// $(this).prop('disabled', false);

			// // ajax success load popup 
			// $('.open-popup-list-movie').magnificPopup({
	  //         	type: 'inline',
	  //         	midClick: true,
		 //    });

			// //ajax success load button facebook
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