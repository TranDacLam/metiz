// function mua ve' roi tra ve hong bao	
	function Quickbooking(obj)
	{
		$.ajax({
			type: 'post',
			url: '#',
			data: 'id=' + obj,
			beforeSend: function(){
				$.colorbox();
			},
		}).done(function(result) {
			html =result;
			$.colorbox({html: '<div class="product-view quick-booking cgv-schedule-popup">'+html+'</div>', width:"88%", height:"88%",fixed:true,modal: false});
			togglecontent('cgv-schedule-popup .tabs-cgv-movie-type');
			togglecontent('cgv-schedule-popup .tabs-cgv-movie-cites');
			togglecontent('cgv-schedule-popup .tabs-cgv-movie-view-date');
		});
	}
