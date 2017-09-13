	
	// active menu (dòng 3-14)
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
	
	// Hiển thị nội dung khi click vào 1 tab cụ thể
	jQuery(document).ready(function(){
			jQuery( ".col-main" ).tabs();
			jQuery( ".accordion" ).accordion({
				heightStyle: "content" // chiều cao của tab phụ thuộc vào độ dài nội dung
			});
	});
	