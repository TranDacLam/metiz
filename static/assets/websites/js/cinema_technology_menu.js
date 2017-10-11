$(document).ready(function() {
	// action for menu cinema technology
	 $(".special-items li a").each(function(){   
        var name = $(this).attr("href");           
        if(window.location.href.indexOf(name) > -1){
            $(this).parent().addClass('actived');
        }
    });
	
});