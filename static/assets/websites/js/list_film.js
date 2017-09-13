
// js for showing.html, arthouse.html
// include js for button facebook like, resize for class product-info and function Quickbooking 
 
// noconflict.js khai bao $j= $

// plugin cho nut like facebook
$j(window).bind('load', function() {
	(function(d, s, id) {
	var js, fjs = d.getElementsByTagName(s)[0];
	if (d.getElementById(id)) return;
	js = d.createElement(s); js.id = id;
	js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.0";
	fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk'));
});


// lay gia tri lon nhat cua height, roi dat cho tat ca phan tu
function equalizeHeights(selector) {
		var heights = new Array();
		$j(selector).each(function() {

			$j(this).css('min-height', '0');
			$j(this).css('max-height', 'none');
			$j(this).css('height', 'auto');

	 		heights.push($j(this).height());
		});

		var max = Math.max.apply( Math, heights );

		$j(selector).each(function() {
			$j(this).css('height', max + 'px');
		});	
	}

// CGV Mới update function resize
// set lai height sau khi resize
	$j(window).load(function() {
		equalizeHeights('.product-info');
		$j('li.category3').find('a').contents().unwrap();
		var iv = null;
		$j(window).resize(function() {
			if(iv !== null) {
				window.clearTimeout(iv);
				console.log('stop');
			}

			iv = setTimeout(function() {
	      			equalizeHeights('.product-info');
	      			console.log('start');
			}, 120);
			$j('li.category3').find('a').contents().unwrap();
		});
	});

// function mua ve' roi tra ve hong bao	
function Quickbooking(obj)
{
	$j.ajax({
		type: 'post',
		url: '',
		data: 'id='+ obj,
		//dataType: 'json',
		beforeSend: function(){
			$j.colorbox();
		},
	}).done(function(result) {
		html =result;
		$j.colorbox({html: '<div class="product-view quick-booking">'+html+'</div>', width:"88%", height:"88%",fixed:true,modal: false});
		togglecontent('tabs-cgv-movie-type');
		togglecontent('tabs-cgv-movie-cites');
		togglecontent('tabs-cgv-movie-view-date');
	});
};
					
