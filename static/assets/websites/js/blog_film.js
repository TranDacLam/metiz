//Filter News
$('select#blog-filter').change(function() {
	var filter = $(this).val()
	filterList(filter);
});

//News filter function
function filterList(value) {
	var list = $(".blog-custom .blog-content");
	$(list).fadeOut("fast");
	if (value == "getNewBlog") {
		$(".blog-custom").find("article").each(function (i) {
			$(this).delay(100).slideDown("fast");
		});
	} else {
		//Notice this *=" <- This means that if the data-category contains multiple options, it will find them
		//Ex: data-category="Cat1, Cat2"
		$(".blog-custom").find("article[data-category*=" + value + "]").each(function (i) {
			$(this).delay(100).slideDown("fast");
		});
	}
}