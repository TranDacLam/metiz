// js for showing.html, arthouse.html
 
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


};
					
