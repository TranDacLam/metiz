
// plugin cho nut like facebook
	(function(d, s, id) {
		var js, fjs = d.getElementsByTagName(s)[0];
		if (d.getElementById(id)) return;
		js = d.createElement(s); js.id = id;
		js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.0";
		fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk'));

// function mua ve' roi tra ve hong bao	
	function Quickbooking(obj)
	{
		$j.ajax({
			type: 'post',
			url: '#',
			data: 'id=' + obj,
			beforeSend: function(){
				$j.colorbox();
			},
		}).done(function(result) {
			html =result;
			$j.colorbox({html: '<div class="product-view quick-booking cgv-schedule-popup">'+html+'</div>', width:"88%", height:"88%",fixed:true,modal: false});
			togglecontent('cgv-schedule-popup .tabs-cgv-movie-type');
			togglecontent('cgv-schedule-popup .tabs-cgv-movie-cites');
			togglecontent('cgv-schedule-popup .tabs-cgv-movie-view-date');
		});
	}
