function blogcats(obj)
	{
		location.href = $j(obj).val();
	}
	
function news(obj)
	{
		var href = $j(obj).find('.aw-blog-read-more').attr('href');
		location.href = href;
	}