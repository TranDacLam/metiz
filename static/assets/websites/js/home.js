$(document).ready(function() {
	// Play trailer for each movie page home
    $('.play-button').on('click', function (event) {
    	$.magnificPopup.open({
		    items: {
		        src: $(this).find('a').attr("href"),
		    },
		    disableOn: 700,
	        type: 'iframe',
	        mainClass: 'mfp-fade',
	        removalDelay: 160,
	        preloader: false,
	        fixedContentPos: false
		  });
    });
    //action for div #show_more hover 
    $('#show_more').hover(function() {
    	$('#more').css('display', 'none');
    	$('#more_hover').css('display', 'block');
    }, function() {
    	/* Stuff to do when the mouse leaves the element */
    	$('#more').css('display', 'block');
    	$('#more_hover').css('display', 'none');
    });
    $('.map-trigger').click(function(event) {
        event.preventDefault();
        $('#content-map').toggle('slow/400/fast');
    });
});