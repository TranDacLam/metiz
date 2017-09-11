	$j(".block-cms-menu li").each(function(){
		var self = this;
		href = $j(this).find('a');
		for(var i = 0 ; i < href.length ; i++){
			var harray = $j(href[i]).attr('href').split("/");
			var charray = window.location.href.split("/");
			if(harray[harray.length-2] == charray[charray.length-2]){
				$j(self).addClass('active');
				break;
			}
		}
	});
	

	jQuery(document).ready(function(){
			jQuery( ".col-main" ).tabs();
			jQuery( ".accordion" ).accordion({
				heightStyle: "content"
			});
	});
	