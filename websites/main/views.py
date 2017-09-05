# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def custom_404(request):
	return render(request, 'websites/errors/404.html', {}, status=404)

def custom_500(request):
	return render(request, 'websites/errors/500.html', {}, status=500)

def home(request):
	data={'banner': ["assets/websites/images/banner-cgv/a.jpg","assets/websites/images/banner-cgv/b.jpg","assets/websites/images/banner-cgv/c.jpg","assets/websites/images/banner-cgv/d.jpg"],
		'movie': ["assets/websites/images/movie-selection/movie1.png","assets/websites/images/movie-selection/movie2.jpg","assets/websites/images/movie-selection/movie3.jpg","assets/websites/images/movie-selection/movie4.jpg","assets/websites/images/movie-selection/movie5.jpg"],
		'event':["assets/websites/images/events/event1.jpg","assets/websites/images/events/event2.jpg","assets/websites/images/events/event3.jpg","assets/websites/images/events/event4.jpg","assets/websites/images/events/event6.png","assets/websites/images/events/event7.jpg"],
		'tv_cgv':["assets/websites/images/thanhvien-cgv/tv1.jpg","assets/websites/images/thanhvien-cgv/tv2.jpg","assets/websites/images/thanhvien-cgv/tv3.jpg","assets/websites/images/thanhvien-cgv/tv4.jpg","assets/websites/images/thanhvien-cgv/tv5.jpg"]
	}
	
	return render(request, 'websites/home.html', {'data': data})

def comingsoon(request):
	data=[{'img':"/assets/websites/images/movie-selection/movie1.png"}, {'img':"/assets/websites/images/movie-selection/movie1.png"}, {'img': "/assets/websites/images/movie-selection/movie1.png"},{'img': "/assets/websites/images/movie-selection/movie1.png"}	,{'img': "/assets/websites/images/movie-selection/movie1.png"}]	
	return render(request, 'websites/coming_soon.html', {'data':data })

def cinox(request):
	
	return render(request, 'websites/cinox.html', {})

def gift_card(request):
	
	return render(request, 'websites/gift_card.html', {})

def membership(request):
	
	return render(request, 'websites/membership.html', {})


def account_create(request):
	
	return render(request, 'websites/account_create.html', {})

def account_login(request):
	
	return render(request, 'websites/account_login.html', {})


def account_findmember(request):
	return render(request, 'websites/account_findmember.html', {})

def account_forgot_password(request):
	
	return render(request, 'websites/account_forgot_password.html', {})


def showing(request):
	data=[{'img':"/assets/websites/images/american_made_240x355.png",'tc':"c18", 'rating':1},{'img':"/assets/websites/images/american_made_240x355.png"
	,'tc': 'c16','rating':2},{'img': "/assets/websites/images/american_made_240x355.png",'tc': "p", 'rating':3}
	,{'img': "/assets/websites/images/american_made_240x355.png",'tc': "p", 'rating':4}
	,{'img': "/assets/websites/images/american_made_240x355.png",'tc': "p", 'rating':5}]
	return render(request, 'websites/showing.html', {'data':data})


def movie_voucher(request):	
	data=[{'product_name':'2D_Voucher','price':'100.000','img':"/assets/websites/images/ticket_voucher_2_.png"}, {'product_name':'3D_Voucher','price':'200.000','img':"/assets/websites/images/ticket_voucher_2__1.png"	} ,{'product_name':'4D_Voucher','price':'300.000','img': "/assets/websites/images/special_cinema-02-cropped.jpg"} ]	
	return render(request, 'websites/movie_voucher.html', {'data':data})

def arthouse(request):
	data=[{'img':"/assets/websites/images/american_made_240x355.png",'tc':"c18", 'rating':1},{'img':"/assets/websites/images/american_made_240x355.png"
	,'tc': 'c16','rating':2},{'img': "/assets/websites/images/american_made_240x355.png",'tc': "p", 'rating':3}
	,{'img': "/assets/websites/images/american_made_240x355.png",'tc': "p", 'rating':4}]
	return render(request, 'websites/arthouse.html', {'data': data})

def about_cinema(request):
	return render(request, 'websites/about_cinema.html',{})

def gift_card_detail(request):
	return render(request, 'websites/gift_card_detail.html',{})

def sweetbox(request):
	data= { 'technology': 
	[{'name': 'sweet box', 'class': 'item-sweetbox', 'flag': 'actived'}
	, {'name': 'sweet box', 'class': 'item-4dx'}
	, {'name': 'sweet box', 'class': 'item-dolby-atmos'}
	, {'name': 'sweet box', 'class': 'item-imax'}
	, {'name': 'sweet box', 'class': 'item-gold-class'}
	, {'name': 'sweet box', 'class': 'item-lamour'}
	, {'name': 'sweet box', 'class': 'item-starium'}
	, {'name': 'sweet box', 'class': 'item-premium'}
	, {'name': 'sweet box', 'class': 'item-screenx'}],
	'address':
	[{'name': 'CGV Da Nang', 'href': '#'}
	, {'name': 'CGV Quang Nam', 'href': '#'}
	, {'name': 'CGV Ha Noi', 'href': '#'}],
	'slide':
	[{'img': '/assets/websites/images/special-theater/sw-1.jpg', 'content': 'Với nỗ lực không ngừng mang đến cho người yêu phim Việt Nam trải nghiệm điện ảnh tốt nhất, CGV hân hạnh mang đến loại ghế đôi <strong> SWEETBOX </strong> cực kỳ độc đáo và mới lạ.'}
	, {'img': '/assets/websites/images/special-theater/sweetbox_03.jpg', 'content':'<strong> SWEETBOX </strong> được đặt ở hàng ghế cuối cùng trong phòng chiếu. Với vách ngăn cao cũng như sự khéo léo trong thiết kế giấu đi tay gác chính giữa giúp cho đôi bạn càng thêm gần gũi và ấm áp, tạo không gian hoàn hảo cho các cặp đôi.'}
	, {'img': '/assets/websites/images/special-theater/sweetbox_02_1.jpg', 'content': '<strong>SWEETBOX</strong> hiện đang có tại <strong>CGV Hùng Vương Plaza</strong>, <strong>CGV Vincom Center Bà Triệu</strong>, <strong>CGV Quy Nhơn Kim Cúc Plaza</strong>, <strong>CGV Vũng Tàu Lam Sơn Square</strong> và <strong>CGV Bình Dương Square</strong>.'}
	, {'img': '/assets/websites/images/special-theater/sw-2.jpg', 'content': 'Hãy đến và trải nghiệm không gian hoàn hảo cho các cặp đôi với <strong>SWEETBOX</strong>.'}],
	}
	technology=[{'name': 'sweet box', 'class': 'sweetbox'}, {'name': 'sweet box', 'class': 'sweetbox'}]
	print data
	return render(request, 'websites/sweetbox.html', {'data': data})
def show_4dx(request):
	data= { 'technology': 
	[{'name': 'sweet box', 'class': 'item-sweetbox'}
	, {'name': 'sweet box', 'class': 'item-4dx', 'flag': 'actived'}
	, {'name': 'sweet box', 'class': 'item-dolby-atmos'}
	, {'name': 'sweet box', 'class': 'item-imax'}
	, {'name': 'sweet box', 'class': 'item-gold-class'}
	, {'name': 'sweet box', 'class': 'item-lamour'}
	, {'name': 'sweet box', 'class': 'item-starium'}
	, {'name': 'sweet box', 'class': 'item-premium'}
	, {'name': 'sweet box', 'class': 'item-screenx'}],
	'address':
	[{'name': 'CGV Da Nang', 'href': '#'}
	, {'name': 'CGV Quang Nam', 'href': '#'}
	, {'name': 'CGV Ha Noi', 'href': '#'}],
	'slide':
	[{'img': '/assets/websites/images/special-theater/4DX_1.png', 'content': '<h2>4DX® - Trải Nghiệm Điện Ảnh Toàn Diện</h2><p>Đã đến lúc thưởng thức phim ảnh theo cách hoàn toàn khác!</p><p>Hòa mình và trải nghiệm cảm giác sống động chân thực trên màn ảnh bằng tất cả các giác quan của bạn.</p>'}
	, {'img': '/assets/websites/images/special-theater/4DX_2.png', 'content':'<h2>Đặc Trưng Nổi Bật Của <strong>4DX® </strong></h2><p>4DX® mang đến cho khán giả hai loại hiệu ứng: hiệu ứng ghế chuyển động đa chiều và hiệu ứng môi trường tương tác xung quanh.</p><p>Ghế 4D bao gồm 3 kiểu chuyển động cơ bản: Xoay, rung lắc và nâng. Các chuyển động này được kết hợp để tạo ra cảm giác sống động vượt trội.</p>'}
	, {'img': '/assets/websites/images/special-theater/4DX_3.png', 'content': '<h2>Các Hiệu Ứng Đặc Trưng Của 4DX®</h2><p>- Chuyển động: Ghế chuyển động đa chiều cho phản ứng chân thực với các tác động từ màn ảnh.</p><p>- Nước: Thiết bị phun nước đặc biệt mang lại những trải nghiệm điện ảnh sống động.</p><p>- Gió: Hệ thống “Phun khí cổ” được cài đặt trên ghế thổi luồng gió trực tiếp lên cổ.</p><p>- Mùi Hương: Chìm đắm vào không gian trong mỗi cảnh phim với trải nghiệm mùi Hương chân thật.</p><p>- Ánh sáng: Hiệu ứng ánh sáng đặc biệt tạo tia chớp được lắp đặt ngay bên trên trần khán phòng.</p>'}
	, {'img': '/assets/websites/images/special-theater/4DX_4.png', 'content': '<h2>Những Điều Cần Biết Khi Thưởng Thức 4DX®</h2><p>- Trẻ em dưới 4 tuổi hoặc cao dưới 1 mét không được sử dụng ghế 4DX®. Trẻ em dưới 7 tuổi phải có bố mẹ hoặc người lớn đi kèm.</p><p>- Phụ nữ đang mang thai, người già, người có thể chất và thần kinh yếu không nên sử dụng ghế 4DX®.</p><p>- Không để trẻ nhỏ ngồi ghế nâng hoặc ngồi chung với bố mẹ.</p>'}],
	}
	return render(request, 'websites/4dx.html', {'data': data})
def dolby_atmos(request):
	data= {'technology': 
	[{'name': 'sweet box', 'class': 'item-sweetbox'}
	, {'name': 'sweet box', 'class': 'item-4dx'}
	, {'name': 'sweet box', 'class': 'item-dolby-atmos', 'flag': 'actived'}
	, {'name': 'sweet box', 'class': 'item-imax'}
	, {'name': 'sweet box', 'class': 'item-gold-class'}
	, {'name': 'sweet box', 'class': 'item-lamour'}
	, {'name': 'sweet box', 'class': 'item-starium'}
	, {'name': 'sweet box', 'class': 'item-premium'}
	, {'name': 'sweet box', 'class': 'item-screenx'}],
	'address': 
	[{'name': 'CGV Da Nang', 'href': '#'}
	, {'name': 'CGV Quang Nam', 'href': '#'}
	, {'name': 'CGV Ha Noi', 'href': '#'}],}
	return render(request , 'websites/dolby_atmos.html', {'data': data})
def imax(request):
	data= { 'technology': 
	[{'name': 'sweet box', 'class': 'item-sweetbox'}
	, {'name': 'sweet box', 'class': 'item-4dx'}
	, {'name': 'sweet box', 'class': 'item-dolby-atmos'}
	, {'name': 'sweet box', 'class': 'item-imax', 'flag': 'actived'}
	, {'name': 'sweet box', 'class': 'item-gold-class'}
	, {'name': 'sweet box', 'class': 'item-lamour'}
	, {'name': 'sweet box', 'class': 'item-starium'}
	, {'name': 'sweet box', 'class': 'item-premium'}
	, {'name': 'sweet box', 'class': 'item-screenx'}],
	'address':
	[{'name': 'CGV Da Nang', 'href': '#'}
	, {'name': 'CGV Quang Nam', 'href': '#'}
	, {'name': 'CGV Ha Noi', 'href': '#'}],
	'slide':
	[{'img': '/assets/websites/images/special-theater/big-screen-imax.png', 'content': '<h2>Trải nghiệm trọn vẹn bộ phim với màn hình cong cỡ lớn</h2><p>Màn hình của phòng chiếu <strong>IMAX®</strong> không chỉ đơn thuần là màn hình cỡ lớn, mà độ cong của màn hình cũng được thiết kế đến mức cực đại. Thiết kế cong của màn hình nhằm đưa hình ảnh lấp đầy tầm nhìn, biến mỗi thước phim trở nên ấn tượng tuyệt đối. Góc nhìn của người xem trong phòng chiếu thường là 54 độ, với <strong>IMAX®</strong> đó là 70 độ!</p><p>ặc biệt, với khoảng cách giữa màn hình, ghế ngồi và độ nghiêng của sàn, khán giả có thể thưởng thức trọn vẹn bộ phim tại bất kì vị trí nào trong phòng chiếu <strong>IMAX®</strong>.</p>'}
	, {'img': '/assets/websites/images/special-theater/hight-light-screen-imax.jpg', 'content':'<h2>Hình ảnh sắc nét với <strong>IMAX DMR® </strong></h2><p>Với phòng chiếu <strong>IMAX®</strong>, bạn như đang bước vào thế giới của chính bộ phim. Hình ảnh không chỉ được mở rộng để phù hợp với kích thước cực đại của màn hình, mà nó còn được chuyển hóa hoàn toàn.</p><p>phối hợp chặt chẽ với các nhà làm phim trong quá trình được gọi là <strong>IMAX DMR® </strong> (Digital Re-mastering), để nâng cao chất lượng của hàng trăm chi tiết trong phần lớn các cảnh phim và mang tới hình ảnh cực kỳ sắc nét.</p>'}
	, {'img': '/assets/websites/images/special-theater/double-screen-imax.png', 'content': '<h2>Chân thực tuyệt đối với máy chiếu đôi</h2><p>Khác với phòng chiếu thường chỉ 1 máy chiếu, phòng chiếu <strong>IMAX®</strong> sở hữu độc quyền và trang bị hệ thống máy chiếu đôi, giúp tăng cường màu ảnh lên tới 40% và độ sáng tới 60%. Đặc biệt, hệ thống còn được tích hợp cảm biến để ghi lại sự thiếu đồng nhất và tự động điều chỉnh, nhằm đảm bảo chất lượng hình ảnh đẹp tối đa trong suốt thời gian của bộ phim</p>'}
	, {'img': '/assets/websites/images/special-theater/senior-imax.png', 'content':'<h2>Tầm cao mới cùng <strong>IMAX® 3D</strong></h2><p>Khi thưởng thức <strong>IMAX® 3D</strong>, người xem sẽ cảm nhận màu sắc và độ sáng của từng hình ảnh được tăng cường tối đa. Đây là kết quả của hiệu ứng xuất ảnh từ 2 máy chiếu vào màn hình tráng bạc đặc biệt, mang đến trải nghiệm 3D khác biệt hoàn toàn với tất cả các công nghệ 3D khác.</p>'}
	, {'img': '/assets/websites/images/special-theater/sound-imax.png', 'content': '<h2>Âm thanh sống động với <strong>IMAX® Sound</strong></h2><p>Hệ thống loa của phòng chiếu <strong>IMAX®</strong> được xây dựng từ sàn tới trần nhà và sắp xếp cực kỳ chuẩn xác nhằm phân bổ âm thanh tới từng vị trí ghế ngồi. Khán giả sẽ có không gian tối ưu nhất để thưởng thức và cảm nhận cả những âm thanh nhỏ nhất của bộ phim. <strong>IMAX®</strong> cũng sử dụng micro để thu thập dữ liệu từ hệ thống loa và tự động điều chỉnh hàng ngày. Đặc biệt, với âm thanh đã được điều chỉnh trong quá trình <strong>IMAX DMR® </strong>, kết hợp với hệ thống âm thanh của phòng chiếu <strong>IMAX®</strong>, cả khán phòng sẽ cùng đắm chìm trong thế giới của bộ phim.</p>'}],
	
	}
	return render( request, 'websites/imax.html',{'data': data})
def gold_class(request):
	data= { 'technology': 
	[{'name': 'sweet box', 'class': 'item-sweetbox'}
	, {'name': 'sweet box', 'class': 'item-4dx'}
	, {'name': 'sweet box', 'class': 'item-dolby-atmos'}
	, {'name': 'sweet box', 'class': 'item-imax'}
	, {'name': 'sweet box', 'class': 'item-gold-class', 'flag': 'actived'}
	, {'name': 'sweet box', 'class': 'item-lamour'}
	, {'name': 'sweet box', 'class': 'item-starium'}
	, {'name': 'sweet box', 'class': 'item-premium'}
	, {'name': 'sweet box', 'class': 'item-screenx'}],
	'address':
	[{'name': 'CGV Da Nang', 'href': '#'}
	, {'name': 'CGV Quang Nam', 'href': '#'}
	, {'name': 'CGV Ha Noi', 'href': '#'}],
	'slide':
	[{'img': '/assets/websites/images/special-theater/goldclass-2.png', 'content': '<h2>Màn Hình Tráng Bạc</h2><p>Hình ảnh trung thực và sắc nét với màn hình tráng bạc độc đáo</p>'}
	, {'img': '/assets/websites/images/special-theater/goldclass-1.png', 'content':'<h2>Âm Thanh Hiện Đại</h2><p>Thưởng thức âm thanh sống động với hệ thống Dolby Surround</p>'}
	, {'img': '/assets/websites/images/special-theater/goldclass-3.png', 'content': '<h2>Ghế Da Sang Trọng</h2><p>Ghế bọc da cao cấp và rộng rãi với nhiều không gian để thoái mái thư giãn</p>'}
	, {'img': '/assets/websites/images/special-theater/goldclass-4.png', 'content': '<h2>Trà/Cà Phê Miễn Phí</h2><p>Thưởng thức trà/cà phê tại phòng chờ riêng yên tĩnh và được phục vụ chăn miễn phí trong phòng chiếu</p>'}],
	
	}
	return render( request, 'websites/gold_class.html', {'data': data})
def lamour(request):
	data= { 'technology': 
	[{'name': 'sweet box', 'class': 'item-sweetbox'}
	, {'name': 'sweet box', 'class': 'item-4dx'}
	, {'name': 'sweet box', 'class': 'item-dolby-atmos'}
	, {'name': 'sweet box', 'class': 'item-imax'}
	, {'name': 'sweet box', 'class': 'item-gold-class'}
	, {'name': 'sweet box', 'class': 'item-lamour', 'flag': 'actived'}
	, {'name': 'sweet box', 'class': 'item-starium'}
	, {'name': 'sweet box', 'class': 'item-premium'}
	, {'name': 'sweet box', 'class': 'item-screenx'}],
	'address':
	[{'name': 'CGV Da Nang', 'href': '#'}
	, {'name': 'CGV Quang Nam', 'href': '#'}
	, {'name': 'CGV Ha Noi', 'href': '#'}],
	'slide':
	[{'img': '/assets/websites/images/special-theater/lamour-1.png', 'content': '<h2>Giường Nằm Êm Ái</h2><p>Ghế ngồi là giường nằm êm ái cùng gối và chăn mang lại cảm giác thoải mái và tinh tế</p>'}
	, {'img': '/assets/websites/images/special-theater/lamour-2.png', 'content':'<h2>Màn Hình Rộng Cùng Âm Thanh Sống Động</h2><p>Hình ảnh trung thực và sắc nét với hệ thống âm thanh hiện đại</p>'}
	, {'img': '/assets/websites/images/special-theater/lamour-3.png', 'content': '<h2>Dịch Vụ Cao Cấp Miễn Phí</h2><p>Thưởng thức trà/cà phê và thức ăn nhẹ được phục vụ miễn phí</p>'}],
	
	}
	return render( request, 'websites/lamour.html', {'data': data})
def starium(request):
	data= { 'technology': 
	[{'name': 'sweet box', 'class': 'item-sweetbox'}
	, {'name': 'sweet box', 'class': 'item-4dx'}
	, {'name': 'sweet box', 'class': 'item-dolby-atmos'}
	, {'name': 'sweet box', 'class': 'item-imax'}
	, {'name': 'sweet box', 'class': 'item-gold-class'}
	, {'name': 'sweet box', 'class': 'item-lamour'}
	, {'name': 'sweet box', 'class': 'item-starium', 'flag': 'actived'}
	, {'name': 'sweet box', 'class': 'item-premium'}
	, {'name': 'sweet box', 'class': 'item-screenx'}],
	'address':
	[{'name': 'CGV Da Nang', 'href': '#'}
	, {'name': 'CGV Quang Nam', 'href': '#'}
	, {'name': 'CGV Ha Noi', 'href': '#'}],
	'slide':
	[{'img': '/assets/websites/images/special-theater/starium-1.png', 'content': '<h2>Máy Chiếu Laser Christie</h2><p>Hệ thống máy chiếu laser RGB CHRISTIE thế hệ mới nhất cung cấp độ sáng, độ tương phản, độ phân giải và mật độ điểm ảnh cực cao, khắc phục những khuyết điểm của các phim 3D như ánh sáng bị tối, nhòe làm bật lên độ sống động đầy kinh ngạc và đạt đến đẳng cấp siêu hạng của sự chân thật.</p>'}
	, {'img': '/assets/websites/images/special-theater/starium-2.png', 'content':'<h2>Âm Thanh Dolby Atmos Hiện Đại</h2><p>Thưởng thức hệ thống âm thanh mái vòm Dolby Atmos mang đến cho khán giả cảm giác sống trong từng thước phim bởi sự thỏa mãn ở mọi giác quan.</p>'}
	, {'img': '/assets/websites/images/special-theater/starium-3.png', 'content': '<h2>Màn Hình Cực Lớn</h2><p>Màn hình cong với kích thước khổng lồ, đem đến góc nhìn tốt nhất cho mọi vị trí trong phòng chiếu.</p>'}],
	
	}
	return render( request, 'websites/starium.html', {'data': data})
def premium(request):
	data= { 'technology': 
	[{'name': 'sweet box', 'class': 'item-sweetbox'}
	, {'name': 'sweet box', 'class': 'item-4dx'}
	, {'name': 'sweet box', 'class': 'item-dolby-atmos'}
	, {'name': 'sweet box', 'class': 'item-imax'}
	, {'name': 'sweet box', 'class': 'item-gold-class'}
	, {'name': 'sweet box', 'class': 'item-lamour'}
	, {'name': 'sweet box', 'class': 'item-starium'}
	, {'name': 'sweet box', 'class': 'item-premium', 'flag': 'actived'}
	, {'name': 'sweet box', 'class': 'item-screenx'}],
	'address':
	[{'name': 'CGV Da Nang', 'href': '#'}
	, {'name': 'CGV Quang Nam', 'href': '#'}
	, {'name': 'CGV Ha Noi', 'href': '#'}],
	'slide':
	[{'img': '/assets/websites/images/special-theater/premium-1.png', }
	, {'img': '/assets/websites/images/special-theater/premium-2.png', }
	, {'img': '/assets/websites/images/special-theater/premium-3.png', }
	, {'img': '/assets/websites/images/special-theater/premium-4.png', }],
	
	}
	return render( request, 'websites/premium.html', {'data': data})
def screenx(request):
	data= { 'technology': 
	[{'name': 'sweet box', 'class': 'item-sweetbox'}
	, {'name': 'sweet box', 'class': 'item-4dx'}
	, {'name': 'sweet box', 'class': 'item-dolby-atmos'}
	, {'name': 'sweet box', 'class': 'item-imax'}
	, {'name': 'sweet box', 'class': 'item-gold-class'}
	, {'name': 'sweet box', 'class': 'item-lamour'}
	, {'name': 'sweet box', 'class': 'item-starium'}
	, {'name': 'sweet box', 'class': 'item-premium'}
	, {'name': 'sweet box', 'class': 'item-screenx', 'flag': 'actived'}],
	'address':
	[{'name': 'CGV Da Nang', 'href': '#'}
	, {'name': 'CGV Quang Nam', 'href': '#'}
	, {'name': 'CGV Ha Noi', 'href': '#'}],
	'slide':
	[{'img': '/assets/websites/images/special-theater/screenx-1.jpg', 'content': '<h2>Trải Nghiệm Thị Giác Vượt Trội</h2><p>Với độ phủ hình ảnh gấp ba lần so với tiêu chuẩn màn chiếu thông thường, ScreenX mang lại những thước phim thật sống động.</p>'}
	, {'img': '/assets/websites/images/special-theater/screenx-2.jpg', 'content': '<h2>Khung Cảnh 3D Thực Tế</h2><p>ScreenX là công nghệ chiếu phim với màn hình đa diện đầu tiên trên thế giới, cho người xem trải nghiệm hình ảnh 270 độ, mở rộng từ màn hình chính và trải dài sang hai bên tường.</p>'}
	, {'img': '/assets/websites/images/special-theater/screenx-3.jpg', 'content': '<h2>Sản Xuất Kỳ Công</h2><p>Để có những cảnh phim ScreenX chỉ từ 15 đến 20 phút trong mỗi bộ phim, các nhà làm phim phải sử dụng ít nhất 3 máy quay với 3 góc quay khác nhau cho mỗi phân cảnh để tái hiện khung cảnh bộ phim một cách chân thật.</p>'}],
	}
	return render( request, 'websites/screenx.html', {'data': data})