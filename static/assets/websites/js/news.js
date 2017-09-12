
// chuyen sang trang khac
function news(obj)
	{
		var href = $j(obj).find('.aw-blog-read-more').attr('href');
		location.href = href;
	}