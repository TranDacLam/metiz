

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
		

	!function(f,b,e,v,n,t,s){
		if(f.fbq)
			return;
		n=f.fbq=function(){
			n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};
			if(!f._fbq)
				f._fbq=n;
			n.push=n;n.loaded=!0;
			n.version='2.0';
			n.queue=[];
			t=b.createElement(e);
			t.async=!0;
			t.src=v;
			s=b.getElementsByTagName(e)[0];
			s.parentNode.insertBefore(t,s)
	}
	(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
	fbq('init', '1644759925761845');
	fbq('track', 'ViewContent');


	jQuery(".large-image-about").colorbox({rel:'group2', transition:"fade", width:"80%", height:"80%"});
				