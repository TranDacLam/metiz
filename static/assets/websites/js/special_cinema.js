$j(document).ready(function () {
	$j('.slideshow-container-dx .slideshow-dx')
		.cycle({
			slides: '> li',
				speed: 600,
				pauseOnHover: true,
				swipe: true,
			prev: '.slideshow-prev',
			next: '.slideshow-next',
		fx: 'scrollHorz'
	});
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
//]]>
