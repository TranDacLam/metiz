
	$j(window).bind('load', function() {
		(function(d, s, id) {
		var js, fjs = d.getElementsByTagName(s)[0];
		if (d.getElementById(id)) return;
		js = d.createElement(s); js.id = id;
		js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.0";
		fjs.parentNode.insertBefore(js, fjs);
		}(document, 'script', 'facebook-jssdk'));
});
	
	$j(document).ready(function(){
		var highest = 0;
		var hi = 0;
		$j('.product-info').each(function(){
		var h = $j(this).height();
		if(h > hi){
				hi = h;
				highest = h;
			}
		});
		if ($j(window).width()>320){
			$j('.product-info').css('height',highest+10+'px');
		}
		else{
			$j('.products-grid .product-info').css('padding-bottom','0');
		}
		$j('li.category3').find('a').contents().unwrap();
		//console.log(abc);
	});
	
	$j(window).on('resize', function() {
		var highest2 = 0;
		var hi = 0;
		$j('.product-info').each(function(){
		var h = $j(this).height();
		if(h > hi){
				hi = h;
				highest2 = h;
			}
		});
		if ($j(window).width()>320){
			$j('.product-info').css('height',highest2+10+'px');
		}
		else{
			$j('.products-grid .product-info').css('padding-bottom','0');
		}
		$j('li.category3').find('a').contents().unwrap();
	});
	
	function Quickbooking(obj)
	{
		$j.ajax({
			type: 'post',
			url: '#',
			data: 'id='+ obj,
			//dataType: 'json',
			beforeSend: function(){
				$j.colorbox();
			},
		}).done(function(result) {
			html =result;
			$j.colorbox({html: '<div class="product-view quick-booking">'+html+'</div>', width:"88%", height:"88%",fixed:true,modal: false});
			togglecontent('tabs-cgv-movie-type');
			togglecontent('tabs-cgv-movie-cites');
			togglecontent('tabs-cgv-movie-view-date');
		});
	}
		