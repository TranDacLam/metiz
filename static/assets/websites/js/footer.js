$(document).ready(function() {
	//action for show map in footer 
    $('.map-trigger').click(function(event) {
        event.preventDefault();
        $('#content-map').slideToggle();
        $('.map-trigger').toggleClass('show');
        if ($('.map-trigger').hasClass('show')) {
        	$('html,body').animate({ scrollTop: $('#content-map').offset().top }, 500);
        }
       
    });
});
$( window ).resize(function() {
    var container_width = $('#pageFacebook').width();    
    $('#pageFacebook').html('<div class="fb-page" data-href="https://www.facebook.com/metizcinema" data-width="' + container_width + '" data-height="210" data-small-header="false" data-adapt-container-width="true" data-hide-cover="false" data-show-facepile="true" data-show-posts="true"><div class="fb-xfbml-parse-ignore"><blockquote cite="https://www.facebook.com/metizcinema"><a href="https://www.facebook.com/metizcinema">Metiz Cinema</a></blockquote></div></div>');
    FB.XFBML.parse();    
});
