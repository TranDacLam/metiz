
	// active khi click vào vị trí Tỉnh/TP (dòng 3-6)
	$j(window).load(function(){
		var city = $j('.cinemas-area li').first().find('span').attr('id');
		$j('.cinemas-area li span').removeClass('siteactive');
		$j('.cinemas-area li span#'+city).addClass('siteactive');
		$j('.cinemas-list .'+city).show(); // show tất cả rạp phim có trong Tỉnh/TP đó
		
		$j('.cinemas-area li').click(function() {
			$j('.cinemas-list li').hide();
			$j('.cinemas-list li').removeClass('current');
			
			// Current city
			var city = $j(this).find('span').attr('id');
			$j('.cinemas-area li span').removeClass('siteactive');
			$j('.cinemas-area li span#'+city).addClass('siteactive');
			$j('.cinemas-list .'+city).show();
		});
		
		$j('#loading-mask').hide();
	});
	
	// (dòng 24-57) hiển thị slide và lịch chiếu chi tiết của rạp đó
	function site(url,obj)
	{
		$j('.cinemas-list li').removeClass('current');
		$j(obj).parent('li').addClass('current');
		history.pushState({}, '', url); //thay đổi đường dẫn url mà ko load lại trang
		$j.ajax({
			url: url,
			beforeSend: function(){
				$j('.theater-container').empty(); // remove class .theater-container
				$j('.slideshow-container .slideshow').cycle('destroy'); // dừng trình chiếu slide và hủy liên kết tất cả sự kiện
				$j('#loading-mask').show(); // hiển thị ảnh gif đang loading
			},
		}).done(function(result) {
			// (dong 38-51: load slide )
			var html = $j(result).find('div.theater-container').children();
			$j('.theater-container').html(html);
			$j('.slideshow-container .slideshow').cycle({
				slides: '> li',
				pager: '.slideshow-pager',
				pagerTemplate: '<span class="pager-box"></span>',
				speed: 600,
				pauseOnHover: true,
				swipe: true,
				prev: '.slideshow-prev',
				next: '.slideshow-next',
				fx: 'scrollHorz',
				log: false
			});
			showtimestabs('tabs-format-metiz');
			showtimestabs('tabs-cgv-showtimes');
			$j('.iframe').colorbox({iframe:true, width:"80%", height:"80%"});
			$j('#loading-mask').hide();
		});
	}
	// (dòng 59-119) show các phim được chiếu theo lịch cụ thể
	function showtimestabs(clss) {
		$j('.'+clss).each(function () {
			var wrapper = $j(this);
			var hasTabs = wrapper.hasClass('tabs');
			var hasAccordion = wrapper.hasClass('accordion');
			var startOpen = wrapper.hasClass('open');
			var dl = wrapper.children('dl:first');
			var dts = dl.children('dt');
			var panes = dl.children('dd');
			var groups = new Array(dts, panes);
			//Create a ul for tabs if necessary.
			// $j('.toggle-tabs').remove();//remove to stop inserting duplicatedly
			if (hasTabs) {
			var ul = $j('<ul class="toggle-tabs"></ul>');
			dts.each(function () {
				var dt = $j(this);
				var li = $j('<li></li>');
				li.html(dt.html());
				ul.append(li);
			});
			ul.insertBefore(dl);
			var lis = ul.children();
			groups.push(lis);
		}
		//Add "last" classes.
		var i;
		for (i = 0; i < groups.length; i++) {
			groups[i].filter(':last').addClass('last');
		}
		function toggleClasses(clickedItem, group) {
			var index = group.index(clickedItem);
			var i;
			for (i = 0; i < groups.length; i++) {
				groups[i].removeClass('current');
				groups[i].eq(index).addClass('current');
			}
		}
		//Toggle on tab (dt) click.
		dts.on('click', function (e) {
			//They clicked the current dt to close it. Restore the wrapper to unclicked state.
			if ($j(this).hasClass('current') && wrapper.hasClass('accordion-open')) {
				wrapper.removeClass('accordion-open');
			} else {
				//They're clicking something new. Reflect the explicit user interaction.
				wrapper.addClass('accordion-open');
			}
			toggleClasses($j(this), dts);
		});
		//Toggle on tab (li) click.
		if (hasTabs) {
			lis.on('click', function (e) {
				toggleClasses($j(this), lis);
			});
			//Open the first tab.
			lis.eq(0).trigger('click');
		}
		//Open the first accordion if desired.
		if (startOpen) {
			dts.eq(0).trigger('click');
		}
	});
}