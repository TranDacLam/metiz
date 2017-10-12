$(document).ready(function() {
	 $(".special-items li a").each(function(){   
        var name = $(this).attr("href");           
        if(window.location.href.indexOf(name) > -1){
            $(this).parent().addClass('actived');
        }
    });
	$('.menu-technology').click(function(event) {
		/* Act on the event */
		event.preventDefault();
		var name = $(this).attr('title');
		$.ajax({
			url: '/technology/',
			type: 'GET',
			data: {
				'name': name,
			}
		})
		.done(function(data) {
			// aminate when click on menu technology
			$(".special-items li").removeClass('actived');
			$(".special-items li a").each(function(){   
		        var name = $(this).attr("title");           
		        if(name == data.name){
		            $(this).parent().addClass('actived');
		        }
		    });
		    // trigger slide
			$('.content-technology').html(data.content);
			jssor_1_slider_init();
		});
	});
});