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
	return render(request, 'websites/gift_card_detail.html',{} )

def cgv_online(request):
	return render(request, 'websites/cgv_online.html', {} )

def careers(request):
	return render(request, 'websites/careers.html', {})

def contacts(request):
	return render(request, 'websites/contacts.html', {})

def terms_conditions(request):
	return render(request, 'websites/terms_conditions.html', {})

def terms_use(request):
	return render(request, 'websites/terms_use.html', {})

def payment_policy(request):
	return render(request, 'websites/payment_policy.html', {})

def privacy_policy(request):
	return render(request, 'websites/privacy_policy.html', {})

def faq(request):
	return render(request, 'websites/faq.html', {})



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
	, {'name': 'sweet box', 'class': 'item-arthouse'}
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
	, {'name': 'sweet box', 'class': 'item-arthouse'}
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
	, {'name': 'sweet box', 'class': 'item-arthouse'}
	, {'name': 'sweet box', 'class': 'item-screenx'}],
	'address': 
	[{'name': 'CGV Da Nang', 'href': '#'}
	, {'name': 'CGV Quang Nam', 'href': '#'}
	, {'name': 'CGV Ha Noi', 'href': '#'}],}
	return render(request , 'websites/dolby_atmos.html', {'data': data})
