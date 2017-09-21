	//co giãn độ cao height tại vị trí class product-info (dòng 15-34) 
	$(document).ready(function(){
		var highest = 0;
		var hi = 0;
		$('.product-info').each(function(){
		var h = $(this).height();
		if(h > hi){
				hi = h;
				highest = h;
			}
		});
		if ($(window).width()>320){
			$('.product-info').css('height',highest+10+'px');
		}
		else{
			$('.products-grid .product-info').css('padding-bottom','0');
		}
		// (dòng 32) remove các phần tử bọc bên ngoài nội dung của thẻ a tính từ class li .category3
		$('li.category3').find('a').contents().unwrap();
		//console.log(abc);
	});
	
	// co giãn độ cao height tại vị trí class product-info khi resize màn hình (dòng 37-54)
	$(window).on('resize', function() {
		var highest2 = 0;
		var hi = 0;
		$('.product-info').each(function(){
		var h = $(this).height();
		if(h > hi){
				hi = h;
				highest2 = h;
			}
		});
		if ($(window).width()>320){
			$('.product-info').css('height',highest2+10+'px');
		}
		else{
			$('.products-grid .product-info').css('padding-bottom','0');
		}
		$('li.category3').find('a').contents().unwrap();
	});
	
	function Quickbooking(obj)
	{
		$.ajax({
			type: 'post',
			url: '#',
			data: 'id='+ obj,
			//dataType: 'json',
			beforeSend: function(){
				$.colorbox();
			},
		}).done(function(result) {
			html =result;
			$.colorbox({html: '<div class="product-view quick-booking">'+html+'</div>', width:"88%", height:"88%",fixed:true,modal: false});
			togglecontent('tabs-cgv-movie-type');
			togglecontent('tabs-cgv-movie-cites');
			togglecontent('tabs-cgv-movie-view-date');
		});
	}