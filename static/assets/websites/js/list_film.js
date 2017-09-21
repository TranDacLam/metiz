// js for showing.html, arthouse.html
// include js for button facebook like, resize for class product-info and function Quickbooking 
 
// lay gia tri lon nhat cua height, roi dat cho tat ca phan tu
function equalizeHeights(selector) {
		var heights = new Array();
		// Loop to get all element heights
		$(selector).each(function() {

			// Need to let sizes be whatever they want so no overflow on resize
			$(this).css('min-height', '0');
			$(this).css('max-height', 'none');
			$(this).css('height', 'auto');

			// Then add size (no units) to array
	 		heights.push($(this).height());
		});

		// Find max height of all elements
		var max = Math.max.apply( Math, heights );

		// Set all heights to max height
		$(selector).each(function() {
			$(this).css('height', max + 'px');
		});	
	}

// CGV Mới update function resize
// set lai height sau khi resize
	$(window).load(function() {
		// Fix heights on page load
		equalizeHeights('.product-info');
		$('li.category3').find('a').contents().unwrap();
		// Fix heights on window resize
		var iv = null;
		$(window).resize(function() {
			if(iv !== null) {
				window.clearTimeout(iv);
			}

			// Needs to be a timeout function so it doesn't fire every ms of resize
			iv = setTimeout(function() {
	      			equalizeHeights('.product-info');
			}, 120);
			$('li.category3').find('a').contents().unwrap();
		});
	});

// click vao button mua ve' hien len popup 
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
		// su dung library jquery.colorbox.js
		$.colorbox({html: '<div class="product-view quick-booking">'+html+'</div>', width:"88%", height:"88%",fixed:true,modal: false});
		// tuy chinh cac class vao trong popup
		// funtion trong cgv.js
		togglecontent('tabs-cgv-movie-type');
		togglecontent('tabs-cgv-movie-cites');
		togglecontent('tabs-cgv-movie-view-date');
	});
};
					
