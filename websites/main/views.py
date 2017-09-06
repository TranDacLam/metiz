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
	data_cinema_area = [{'id':'cgv_city_1', 'name':'Hồ Chí Minh'},{'id':'cgv_city_3', 'name':'Hà Nội'},
	{'id':'cgv_city_5', 'name':'Đà Nẵng'},{'id':'cgv_city_7', 'name':'Cần Thơ'},{'id':'cgv_city_9', 'name':'Đồng Nai'},
	{'id':'cgv_city_11', 'name':'Hải Phòng'},{'id':'cgv_city_13', 'name':'Quảng Ninh'},{'id':'cgv_city_15', 'name':'Bà Rịa-Vũng Tàu'},
	{'id':'cgv_city_17', 'name':'Bình Định'},{'id':'cgv_city_19', 'name':'Bình Dương'}]

	data_cinema_list = [{'id':'cgv_site_004','class':'cgv_city_1','name':'CGV Hùng Vương Plaza'},{'id':'cgv_site_007','class':'cgv_city_1','name':'CGV Paragon'},
	{'id':'cgv_site_008','class':'cgv_city_1','name':'CGV Cresent Mall'},{'id':'cgv_site_021','class':'cgv_city_1','name':'CGV Thảo Điền Pearl'},{'id':'cgv_site_023','class':'cgv_city_1','name':'CGV Vincom Thủ Đức'},
	{'id':'cgv_site_024','class':'cgv_city_1','name':'CGV Vivo City'},{'id':'cgv_site_021','class':'cgv_city_1','name':'CGV Thảo Điền Pearl'},{'id':'cgv_site_030','class':'cgv_city_1','name':'CGV Pearl Plaza'},
	{'id':'cgv_site_040','class':'cgv_city_1','name':'CGV Golden Plaza'},{'id':'cgv_site_001','class':'cgv_city_3','name':'CGV Vincom Center Bà Triệu'},{'id':'cgv_site_009','class':'cgv_city_3','name':'CGV Mipec Tower'}]
	return render(request, 'websites/cinox.html', {'data_cinema_area':data_cinema_area,'data_cinema_list':data_cinema_list})

def gift_card(request):
	data=[{'img':'/assets/websites/images/gift_card_-_cinox_1.png','title':'Thẻ Quà Tặng - 300.000đ','price':'300.000,00 ₫','description':'Có giá trị như tiền mặt'},
	{'img':'/assets/websites/images/gift_card_-_cinox_1.png','title':'Thẻ Quà Tặng - 500.000đ','price':'500.000,00 ₫','description':'Có giá trị như tiền mặt'}]

	return render(request, 'websites/gift_card.html', {'data':data})

def membership(request):
	
	return render(request, 'websites/membership.html', {})

def account_create(request):
	data_country = [{'value':'','name':''},{'value':'AF','name':'Afghanistan'},
	{'value':'EG','name':'Ai Cập'},{'value':'IE','name':'Ai-len'},
	{'value':'AL','name':'Albani'},{'value':'DZ','name':'Algeria'}]

	data_city = [{'value':'65','name':'Hồ Chí Minh'},{'value':'64','name':'Hà Nội'},
	{'value':'60','name':'Đà Nẵng'},{'value':'48','name':'Cần Thơ'},
	{'value':'39L','name':'Đồng Nai'},{'value':'62','name':'Hải Phòng'}]

	data_day = [{'value':'01','day':'01'},{'value':'02','day':'02'},
	{'value':'03','day':'03'},{'value':'04','day':'04'},
	{'value':'05','day':'05'},{'value':'06','day':'06'}]

	data_month = [{'value':'01','month':'01'},{'value':'02','month':'02'},{'value':'03','month':'03'},
	{'value':'04','month':'04'},{'value':'05','month':'05'},{'value':'06','month':'06'},{'value':'07','month':'07'}]

	data_year = [{'value':'1990','year':'1990'},{'value':'1991','year':'1991'},{'value':'1992','year':'1992'},
	{'value':'1993','year':'1993'},{'value':'1994','year':'1994'},{'value':'1995','year':'1995'},{'value':'1996','year':'1996'}]

	data_cgv = [{'value':'017', 'name':'CGV Aeon Canary'},{'value':'018', 'name':'CGV Aeon Long Bien'},
	{'value':'019', 'name':'CGV Aeon Mall Binh Tan'},{'value':'020', 'name':'CGV Artemis Ha Noi'},
	{'value':'021', 'name':'CGV Aeon Tan Phu'}]

	data_prefergenre = [{'value':'06','name':'ACTION'},{'value':'07','name':'ADVENTURE'},{'value':'08','name':'ANIMATION'},
	{'value':'09','name':'COMEDY'},{'value':'14','name':'CRIME'}]
	
	return render(request, 'websites/account_create.html', {'data_country':data_country, 'data_city':data_city,'data_day':data_day,'data_month':data_month,'data_year':data_year,'data_cgv':data_cgv, 'data_prefergenre':data_prefergenre})

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
	data = [{'img':'/assets/websites/images/about-1.jpg'},{'img':'/assets/websites/images/about-2.PNG'},{'img':'/assets/websites/images/about-3.PNG'},
	{'img':'/assets/websites/images/about-4.PNG'},{'img':'/assets/websites/images/about-5.PNG'},{'img':'/assets/websites/images/about-6.PNG'},
	{'img':'/assets/websites/images/about-7.JPG'},{'img':'/assets/websites/images/about-8.JPG'},{'img':'/assets/websites/images/about-9.PNG'}]
	
	return render(request, 'websites/about_cinema.html',{'data': data})

def gift_card_detail(request):
	terms_conditions = [{'description':'Thẻ này dùng để đổi vé xem phim hoặc thức ăn, đồ uống tại tất cả các rạp CGV, áp dụng tại quầy & trực tuyến.'},
	{'description':'Thẻ có thẻ được nạp thêm tiền và gia hạn tại quầy hoặc trực tuyến bất cứ lúc nào với số tiền tối thiểu 300,000đ.'},
	{'description':'Riêng với thẻ quà tặng được đăng ký trực tuyến, ngày hết hạn của tất cả thẻ trước đó sẽ được gia hạn theo ngày hết hạn của thẻ mới nhất.'},
	{'description':'Thẻ có giá trị tích lũy điểm và tổng chi tiêu cho người sử dụng, không có giá trị tích lũy điểm và tổng chi tiêu cho người mua.'},
	{'description':'Thẻ không được dùng để đổi sang tiền mặt hoặc mua thẻ khác.'},
	{'description':'Nếu thẻ bị mất hoặc hư hại, giá trị sử dụng sẽ không còn hiệu lực hay cấp lại nếu không có bằng chứng xác thực hợp lệ nào.'}]
	
	return render(request, 'websites/gift_card_detail.html',{'terms_conditions':terms_conditions} )

def cgv_online(request):
	return render(request, 'websites/cgv_online.html', {} )

def careers(request):
	return render(request, 'websites/careers.html', {})

def contacts(request):
	return render(request, 'websites/contacts.html', {})

def terms_conditions(request):

	data = [{'title':'1. Trách nhiệm của người sử dụng:','content':'Khi truy cập vào trang web này, bạn đồng ý chấp nhận mọi rủi ro. CGV và các bên đối tác khác không chịu trách nhiệm về bất kỳ tổn thất nào do những hậu quả trực tiếp, tình cờ hay gián tiếp; những thất thoát, chi phí (bao gồm chi phí pháp lý, chi phí tư vấn hoặc các khoản chi tiêu khác) có thể phát sinh trực tiếp hoặc gián tiếp do việc truy cập trang web hoặc khi tải dữ liệu về máy; những tổn hại gặp phải do virus, hành động phá hoại trực tiếp hay gián tiếp của hệ thống máy tính khác, đường dây điện thoại, phần cứng, phần mềm, lỗi chương trình, hoặc bất kì các lỗi nào khác; đường truyền dẫn của máy tính hoặc nối kết mạng bị chậm…'},
	{'title':'2. Về nội dung trên trang web:','content':'Tất cả những thông tin ở đây được cung cấp cho bạn một cách trung thực như bản thân sự việc. CGV và các bên liên quan không bảo đảm, hay có bất kỳ tuyên bố nào liên quan đến tính chính xác, tin cậy của việc sử dụng hay kết quả của việc sử dụng nội dung trên trang web này. Nột dung trên website được cung cấp vì lợi ích của cộng đồng và có tính phi thương mại. Các cá nhân và tổ chức không được phếp sử dụng nội dung trên website này với mục đích thương mại mà không có sự ưng thuận của CGV bằng văn bản. Mặc dù CGV luôn cố gắng cập nhật thường xuyên các nội dung tại trang web, nhưng chúng tôi không bảo đảm rằng các thông tin đó là mới nhất, chính xác hay đầy đủ. Tất cả các nội dung website có thể được thay đổi bất kỳ lúc nào.'},
	{'title':'3. Về bản quyền:','content':'CGV là chủ bản quyền của trang web này. Việc chỉnh sửa trang, nội dung, và sắp xếp thuộc về thẩm quyền của CGV. Sự chỉnh sửa, thay đổi, phân phối hoặc tái sử dụng những nội dung trong trang này vì bất kì mục đích nào khác được xem như vi phạm quyền lợi hợp pháp của CGV.'},
	{'title':'4. Về việc sử dụng thông tin:','content':'Chúng tôi sẽ không sử dụng thông tin cá nhân của bạn trên website này nếu không được phép. Nếu bạn đồng ý cung cấp thông tin cá nhân, bạn sẽ được bảo vệ. Thông tin của bạn sẽ được sử dụng với mục đích, liên lạc với bạn để thông báo các thông tin cập nhật của CGV như lịch chiếu phim, khuyến mại qua email hoặc bưu điện. Thông tin cá nhân của bạn sẽ không được gửi cho bất kỳ ai sử dụng ngoài trang web CGV, ngoại trừ những mở rộng cần thiết để bạn có thể tham gia vào trang web (những nhà cung cấp dịch vụ, đối tác, các công ty quảng cáo) và yêu cầu cung cấp bởi luật pháp. Nếu chúng tôi chia sẻ thông tin cá nhân của bạn cho các nhà cung cấp dịch vụ, công ty quảng cáo, các công ty đối tác liên quan, thì chúng tôi cũng yêu cầu họ bảo vệ thông tin cá nhân của bạn như cách chúng tôi thực hiện.'},
	{'title':'5. Về việc tải dữ liệu:','content':'Nếu bạn tải về máy những phần mềm từ trang này, thì phần mềm và các dữ liệu tải sẽ thuộc bản quyền của CGV và cho phép bạn sử dụng. Bạn không được sở hữu những phầm mềm đã tải và CGV không nhượng quyền cho bạn. Bạn cũng không được phép bán, phân phối lại, hay bẻ khóa phần mềm…'},
	{'title':'6. Thay đổi nội dung:','content':'CGV giữ quyền thay đổi, chỉnh sửa và loại bỏ những thông tin hợp pháp vào bất kỳ thời điểm nào vì bất kỳ lý do nào.'},
	{'title':'7. Liên kết với các trang khác: ','content':'Mặc dù trang web này có thể được liên kết với những trang khác, CGV không trực tiếp hoặc gián tiếp tán thành, tổ chức, tài trợ, đứng sau hoặc sát nhập với những trang đó, trừ phi điều này được nêu ra rõ ràng. Khi truy cập vào trang web bạn phải hiểu và chấp nhận rằng CGV không thể kiểm soát tất cả những trang liên kết với trang CGV và cũng không chịu trách nhiệm cho nội dung của những trang liên kết.'},
	{'title':'8. Đưa thông tin lên trang web:','content':'Bạn không được đưa lên, hoặc chuyển tải lên trang web tất cả những hình ảnh, từ ngữ khiêu dâm, thô tục, xúc phạm, phỉ báng, bôi nhọ, đe dọa, những thông tin không hợp pháp hoặc những thông tin có thể đưa đến việc vi phạm pháp luật, trách nhiệm pháp lý. CGV và tất cả các bên có liên quan đến việc xây dựng và quản lý trang web không chịu trách nhiệm hoặc có nghĩa vụ pháp lý đối với những phát sinh từ nội dung do bạn tải lên trang web.'},
	{'title':'9. Luật áp dụng:','content':'Mọi hoạt động phát sinh từ trang web có thể sẽ được phân tích và đánh giá theo luật pháp Việt Nam và toà án Tp. Hồ Chí Minh. Và bạn phải đồng ý tuân theo các điều khoản riêng của các toà án này.'}]
	
	return render(request, 'websites/terms_conditions.html', {'data':data})

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
def film_detail(request):
	data= {'director': ' Doug Liman', 'actor':'Tom Cruise, Domhnall Gleeson, Sarah Wright, E. Roger Mitchell, Jesse Plemons, Lola Kirke, Alejandro Edda, Benito Martinez, Caleb Landry Jones, Jayma Mays',
	'category': 'Hành Động, Hồi hộp, Phiêu Lưu', 'language': 'Tiếng Anh với phụ đề tiếng Việt và phụ đề tiếng Hàn',
	'time': '180 phút', 'rated': 'C18 - Phim cấm khán giả dưới 18 tuổi', 'date': '20/8/2017',
	'img': '/assets/websites/images/american_made_160x237.png', 
	'content': 'Dựa trên một câu chuyện có thật, BARRY SEAL: LÁCH LUẬT KIỂU MỸ là cuộc phiêu lưu xuyên quốc gia của Barry Seal, tên lừa đảo và cũng là một phi công bất ngờ được chiêu mộ vào tổ chức CIA để thực hiện một trong những điệp vụ ngầm lớn nhất trong lịch sử Mỹ.',
	'trailer': '//www.youtube.com/embed/PALCTTuWkSc?rel=0&amp;showinfo=0'}
	return render(request, 'websites/film_detail.html', {'data': data})
