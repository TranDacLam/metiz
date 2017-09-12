
// silde dung trong sweetbox.html, 4dx.html, dolbay-atmos.html, imax.html, gold-class.html, 
// lamour.html, starium.html, premium.html, screenx.html

// slide dung thu vien jquery.cycle2.min.js
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
});
