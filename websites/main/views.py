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
	data=[
	{'img':"/assets/websites/images/american_made_240x355.png",'tc':"c18", 'rating':1,'name': 'Lách Luật Kiểu Mỹ',
	'category': 'Hành Động, Hồi hộp, Phiêu Lưu', 'technology': 'imax2d' ,
	'time': '180 phút', 'date': '20/8/2017',},
	{'img':"/assets/websites/images/american_made_240x355.png",'tc': 'c16','rating':2, 'name': 'Lách Luật Kiểu Mỹ',
	'category': 'Hành Động, Hồi hộp, Phiêu Lưu', 'technology': 'imax2d' ,
	'time': '180 phút', 'date': '20/8/2017',}
	,{'img': "/assets/websites/images/american_made_240x355.png",'tc': "p", 'rating':3, 'name': 'Lách Luật Kiểu Mỹ',
	'category': 'Hành Động, Hồi hộp, Phiêu Lưu', 'technology': 'imax2d' ,
	'time': '180 phút',  'date': '20/8/2017',}
	,{'img': "/assets/websites/images/american_made_240x355.png",'tc': "p", 'rating':4, 'name': 'Lách Luật Kiểu Mỹ',
	'category': 'Hành Động, Hồi hộp, Phiêu Lưu', 'technology': 'imax2d' ,
	'time': '180 phút', 'date': '20/8/2017',}
	,{'img': "/assets/websites/images/american_made_240x355.png",'tc': "p", 'rating':5, 'name': 'Lách Luật Kiểu Mỹ',
	'category': 'Hành Động, Hồi hộp, Phiêu Lưu', 'technology': 'imax2d' ,
	'time': '180 phút', 'date': '20/8/2017',}]

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
	
	data_content = [{'content': 'CJ CGV trực thuộc CJ Group, một trong những tập đoàn kinh tế đa ngành lớn nhất của Hàn Quốc có mặt ở 21 quốc gia trên thế giới. CJ CGV là một trong top 5 cụm rạp chiếu phim lớn nhất toàn cầu và là nhà phát hành, cụm rạp chiếu phim lớn nhất Việt Nam'},
	{'content': 'CJ CGV trực thuộc CJ Group, một trong những tập đoàn kinh tế đa ngành lớn nhất của Hàn Quốc có mặt ở 21 quốc gia trên thế giới. CJ CGV là một trong top 5 cụm rạp chiếu phim lớn nhất toàn cầu và là nhà phát hành, cụm rạp chiếu phim lớn nhất Việt Nam'},
	{'content': 'CJ CGV đã tạo nên khái niệm độc đáo về việc chuyển đổi rạp chiếu phim truyền thống thành tổ hợp văn hóa “Cultureplex”, nơi khán giả không chỉ đến thưởng thức điện ảnh đa dạng thông qua các công nghệ tiên tiến như IMAX, STARIUM, 4DX, Dolby Atmos, cũng như thưởng thức ẩm thực hoàn toàn mới và khác biệt trong khi trải nghiệm dịch vụ chất lượng nhất tại CGV'},]
	return render(request, 'websites/about_cinema.html',{'data': data,'data_content':data_content})

def gift_card_detail(request):
	terms_conditions = [{'description':'Thẻ này dùng để đổi vé xem phim hoặc thức ăn, đồ uống tại tất cả các rạp CGV, áp dụng tại quầy & trực tuyến.'},
	{'description':'Thẻ có thẻ được nạp thêm tiền và gia hạn tại quầy hoặc trực tuyến bất cứ lúc nào với số tiền tối thiểu 300,000đ.'},
	{'description':'Riêng với thẻ quà tặng được đăng ký trực tuyến, ngày hết hạn của tất cả thẻ trước đó sẽ được gia hạn theo ngày hết hạn của thẻ mới nhất.'},
	{'description':'Thẻ có giá trị tích lũy điểm và tổng chi tiêu cho người sử dụng, không có giá trị tích lũy điểm và tổng chi tiêu cho người mua.'},
	{'description':'Thẻ không được dùng để đổi sang tiền mặt hoặc mua thẻ khác.'},
	{'description':'Nếu thẻ bị mất hoặc hư hại, giá trị sử dụng sẽ không còn hiệu lực hay cấp lại nếu không có bằng chứng xác thực hợp lệ nào.'}]
	
	data_description = [{'description':'CGV hân hạnh phát hành Thẻ Quà Tặng - Phương tiện thanh toán hiện đại và thuận tiện. Đây là một món quà điện ảnh tuyệt vời mà bạn có thể chia sẻ và gửi tặng bạn bè, gia đình, đồng nghiệp và đối tác. Chắc chắn đây sẽ là món quà ngập tràn sắc màu điện ảnh thật ý nghĩa và tuyệt vời dành cho những người bạn yêu quý.'},
	{'description':'Thẻ Quà Tặng CGV là loại thẻ trả trước. Với số tiền trong thẻ, bạn có thể sử dụng Thẻ để đổi vé xem phim hoặc bất kì sản phẩm nào tại quầy Bắp Nước của CGV Cinemas.Với vẻ ngoài sang trọng và sự tiện lợi, bạn có thể lựa chọn các mệnh giá cho Thẻ Quà Tặng như 300.000đ; 500.000đ; hoặc 1.000.000đ. Thẻ có thời hạn sử dụng trong 1 năm và đặc biệt bạn có thể nạp thêm tiền để gia hạn bất cứ lúc nào. Bạn có thể mua thẻ thật dễ dàng mà không cần đăng ký thông tin chủ thẻ.'}]	

	data_content = [{'content':'Thẻ Quà Tặng CGV là loại thẻ trả trước. Với số tiền trong thẻ, bạn có thể sử dụng Thẻ để đổi vé xem phim hoặc bất kì sản phẩm nào tại quầy Bắp Nước của CGV Cinemas.'},
	{'content':'Với vẻ ngoài sang trọng và sự tiện lợi, bạn có thể lựa chọn các mệnh giá cho Thẻ Quà Tặng như 300.000đ; 500.000đ; hoặc 1.000.000đ. Thẻ có thời hạn sử dụng trong 1 năm và đặc biệt bạn có thể nạp thêm tiền để gia hạn bất cứ lúc nào. Bạn có thể mua thẻ thật dễ dàng mà không cần đăng ký thông tin chủ thẻ'},
	{'content':'Thẻ quà tặng đang được bán tại quầy vé các rạp CGV Cinemas trên toàn quốc, hoặc bạn có thể mua thẻ quà tặng điện tử tại đây. Thẻ quà tặng có thể được tích hợp vào tài khoản thành viên, và thanh toán tiện lợi bằng thẻ thành viên khi không mang theo thẻ quà tặng.'},
	{'content':'Hiện có loại thẻ quà tặng cho công ty / tổ chức khi bạn mua vé với số lượng lớn. Đặc biệt bạn có thể đưa logo và thông điệp của công ty / tổ chức vào thẻ. Gọi bộ phận Bán Vé Nhóm (Group Sales) để biết thêm thông tin: +84-8-3822-0333 '},
	{'content':'Các câu hỏi thường gặp, vui lòng xem ở đây.'}]
	return render(request, 'websites/gift_card_detail.html',{'data_description':data_description,'data_content':data_content,'terms_conditions':terms_conditions} )

def cgv_online(request):
	return render(request, 'websites/cgv_online.html', {} )

def careers(request):
	return render(request, 'websites/careers.html', {})

def careers_units(request):
	data_careers_units = [{'name':'C&B Executive', 'location':'Working Location: HCMC'},{'name':'C&B Team Leader', 'location':'Working Location: HCMC'},{'name':'Film Marketing Analyst', 'location':'Working location: HC'},
	{'name':'Group Sale Analyst', 'location':'Working location: Hanoi, HCMC'},{'name':'Marketing Communication', 'location':'Working locaiton: HCMC'},{'name':'PR Analyst', 'location':'Working location: HCMC'}]
	
	return render(request, 'websites/careers_units.html', {'data_careers_units':data_careers_units})

def careers_cluster(request):
	data_careers_cluster = [{'name':'Assistant Cinema Manager', 'location':'Working Location: Phu Yen'},{'name':'Nhân Viên Kỹ Thuật Bảo Trì	', 'location':'Working Location: HCMC'},{'name':'Nhân Viên Kỹ Thuật Phòng Chiếu', 'location':'Working location: HC'}]
	
	return render(request, 'websites/careers_cluster.html', {'data_careers_cluster':data_careers_cluster})


def careers_units_detail(request):
	data_careers_units_detail = [{'location':'HCM','job_description':'-Prepare monthly input VAT report.<br />-Provide VAT, WHT data for Tax authority and External Audit fully, exactly and timely.<br />-Update tax regulation.<br />','requirement':'-Prefer to be graduated from Accounting and Auditing faculty.<br />-Having 03 years experience in Tax field specially in Advertising, Service industry.<br />'}]
	return render(request, 'websites/careers_units_detail.html', {'data_careers_units_detail':data_careers_units_detail})

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

	data = [{'title':'1. Quy định về thanh toán','content':[{'name':'Khách hàng có thể lựa chọn các hình thức thanh toán sau để thanh toán cho giao dịch đặt vé trên website CGV'},{'name':'- Điểm Thưởng thành viên'},{'name':'- Thẻ quà tặng CGV ( CGV Giftcard)'}]},
	{'title':'2. Chi tiết các hình thức thanh toán','content':[{'name':'- Điểm Thưởng Thành Viên (Membership Point): Mỗi 01 điểm thưởng tương đương với 1.000 VND. Điểm thưởng này, bạn có thể sử dụng để thanh toán vé xem phim và các sản phẩm đồ ăn thức uống tại hệ thống CGV toàn quốc. Khi sử dụng điểm thưởng, bạn vui lòng xuất trình thẻ thành viên để được nhân viên hỗ trợ thanh toán. Điểm thưởng được sử dụng phải từ 20 điểm trở lên'},{'name':'- Để kiểm tra điểm thưởng, bạn vui lòng truy cập vào đây (https://www.cgv.vn/default/customer/account/) và đăng nhập vào tài khoản của mình.'}]}]
	return render(request, 'websites/payment_policy.html', {'data':data})

def privacy_policy(request):
	return render(request, 'websites/privacy_policy.html', {})

def faq(request):

	data_film = [{'ques':'Phân loại phim P, C13, C16, C18 là gì?','answer':[{'answ1':'Căn cứ Thông tư số 12/2015/TT-BVHTTDL của Bộ trưởng Bộ Văn hóa, Thể thao và Du lịch có hiệu lực thi hành từ ngày 01/01/2017, Tiêu chí phân loại phim theo lứa tuổi được quy định như sau:'},{'answ1':'P: Phim được phép phổ biến rộng rãi đến mọi đối tượng'},{'answ1':'C13: Phim cấm phổ biến đến khán giả dưới 13 tuổi'}]},
	{'ques':'Trước khi được trình chiếu tại Việt Nam, các bộ phim phải trải qua sự kiểm duyệt và cấp phép như thế nào?','answer':[{'answ1':'Tất cả những phim được trình chiếu tại các rạp chiếu phim ở Việt Nam phải được kiểm duyệt, sau đó được cấp giấy phép phát hành và phạm vi phổ biến phim bởi Cục Điện Ảnh thuộc Bộ Văn Hóa, Thể Thao và Du Lịch Việt Nam'}]},
	{'ques':'Suất Chiếu Đặc Biệt là gì?','answer':[{'answ1':'Suất Chiếu Đặc Biệt là những suất chiếu được ra rạp trước ngày công chiếu chính thức'}]}]
	
	data_food = [{'ques':'Thức ăn, đồ uống mua bên ngoài có được mang vào rạp CGV không?','answer':[{'answ1':'Để đảm bảo vệ sinh và an toàn, chỉ thức ăn và đồ uống được mua tại CGV mới được đem vào rạp chiếu phim.'}]},
	{'ques':'Bắp bướm là gì?','answer':[{'answ1':'Bắp bướm là bắp khi nở chín có hình dạng nhiều cánh xòe ra các bên. Bắp bướm tại CGV có hai vị mặn và ngọt.'}]},
	{'ques':'Bắp nấm là gì?','answer':[{'answ1':'Bắp nấm có hình dạng tròn, hạt bắp nổ đều và giòn. Bắp nấm tại CGV có bốn vị mặn, ngọt, phô mai và caramel.'}]}]

	data_voucher = [{'ques':'CGV có các loại voucher nào?','answer':[{'answ1':'CGV phát hành nhiều loại voucher khác nhau:'},{'answ1':'- 2D Voucher'},{'answ1':'- 3D Voucher'},{'answ1':'- 4DX Voucher'}]},
	{'ques':'Mua Vé Nhóm (Group Sales) là gì?','answer':[{'answ1':'Mua Vé Nhóm là chương trình bán vé số lượng lớn với giá vé ưu đãi so với mua vé lẻ thông thường (tối thiểu 50 vé). Vé nhóm được bán dưới dạng voucher, hoặc thẻ quà tặng,... Bạn có thể liên hệ bộ phận Bán Vé Nhóm (Group Sales) để biết thêm thông tin: +84-028-3822-0333.'}]},
	{'ques':'Việc mua voucher hoặc sử dụng voucher để đổi vé có được tích điểm không?','answer':[{'answ1':'Rất tiếc các giao dịch liên quan đến voucher sẽ không được tích điểm.'}]}]
	return render(request, 'websites/faq.html', {'data_film':data_film, 'data_food':data_food, 'data_voucher':data_voucher})



def sweetbox(request):
	data= { 'technology': 
	[{'name': 'sweetbox', 'class': 'item-sweetbox', 'flag': 'actived'}
	, {'name': '4dx', 'class': 'item-4dx'}
	, {'name': 'dolby-atmos', 'class': 'item-dolby-atmos'}
	, {'name': 'imax', 'class': 'item-imax'}
	, {'name': 'gold-class', 'class': 'item-gold-class'}
	, {'name': 'lamour', 'class': 'item-lamour'}
	, {'name': 'starium', 'class': 'item-starium'}
	, {'name': 'premium', 'class': 'item-premium'}
	, {'name': 'screenx', 'class': 'item-screenx'}],
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
	[{'name': 'sweetbox', 'class': 'item-sweetbox'}
	, {'name': '4dx', 'class': 'item-4dx', 'flag': 'actived'}
	, {'name': 'dolby-atmos', 'class': 'item-dolby-atmos'}
	, {'name': 'imax', 'class': 'item-imax'}
	, {'name': 'gold-class', 'class': 'item-gold-class'}
	, {'name': 'lamour', 'class': 'item-lamour'}
	, {'name': 'starium', 'class': 'item-starium'}
	, {'name': 'premium', 'class': 'item-premium'}
	, {'name': 'screenx', 'class': 'item-screenx'}],
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
	[{'name': 'sweetbox', 'class': 'item-sweetbox'}
	, {'name': '4dx', 'class': 'item-4dx'}
	, {'name': 'dolby-atmos', 'class': 'item-dolby-atmos', 'flag': 'actived'}
	, {'name': 'imax', 'class': 'item-imax'}
	, {'name': 'gold-class', 'class': 'item-gold-class'}
	, {'name': 'lamour', 'class': 'item-lamour'}
	, {'name': 'starium', 'class': 'item-starium'}
	, {'name': 'premium', 'class': 'item-premium'}
	, {'name': 'screenx', 'class': 'item-screenx'}],
	'address': 
	[{'name': 'CGV Da Nang', 'href': '#'}
	, {'name': 'CGV Quang Nam', 'href': '#'}
	, {'name': 'CGV Ha Noi', 'href': '#'}],}
	return render(request , 'websites/dolby_atmos.html', {'data': data})
def imax(request):
	data= { 'technology': 
	[{'name': 'sweetbox', 'class': 'item-sweetbox'}
	, {'name': '4dx', 'class': 'item-4dx'}
	, {'name': 'dolby-atmos', 'class': 'item-dolby-atmos'}
	, {'name': 'imax', 'class': 'item-imax', 'flag': 'actived'}
	, {'name': 'gold-class', 'class': 'item-gold-class'}
	, {'name': 'lamour', 'class': 'item-lamour'}
	, {'name': 'starium', 'class': 'item-starium'}
	, {'name': 'premium', 'class': 'item-premium'}
	, {'name': 'screenx', 'class': 'item-screenx'}],
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
	[{'name': 'sweetbox', 'class': 'item-sweetbox'}
	, {'name': '4dx', 'class': 'item-4dx'}
	, {'name': 'dolby-atmos', 'class': 'item-dolby-atmos'}
	, {'name': 'imax', 'class': 'item-imax'}
	, {'name': 'gold-class', 'class': 'item-gold-class', 'flag': 'actived'}
	, {'name': 'lamour', 'class': 'item-lamour'}
	, {'name': 'starium', 'class': 'item-starium'}
	, {'name': 'premium', 'class': 'item-premium'}
	, {'name': 'screenx', 'class': 'item-screenx'}],
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
	[{'name': 'sweetbox', 'class': 'item-sweetbox'}
	, {'name': '4dx', 'class': 'item-4dx'}
	, {'name': 'dolby-atmos', 'class': 'item-dolby-atmos'}
	, {'name': 'imax', 'class': 'item-imax'}
	, {'name': 'gold-class', 'class': 'item-gold-class'}
	, {'name': 'lamour', 'class': 'item-lamour', 'flag': 'actived'}
	, {'name': 'starium', 'class': 'item-starium'}
	, {'name': 'premium', 'class': 'item-premium'}
	, {'name': 'screenx', 'class': 'item-screenx'}],
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
	[{'name': 'sweetbox', 'class': 'item-sweetbox'}
	, {'name': '4dx', 'class': 'item-4dx'}
	, {'name': 'dolby-atmos', 'class': 'item-dolby-atmos'}
	, {'name': 'imax', 'class': 'item-imax'}
	, {'name': 'gold-class', 'class': 'item-gold-class'}
	, {'name': 'lamour', 'class': 'item-lamour'}
	, {'name': 'starium', 'class': 'item-starium', 'flag': 'actived'}
	, {'name': 'premium', 'class': 'item-premium'}
	, {'name': 'screenx', 'class': 'item-screenx'}],
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
	[{'name': 'sweetbox', 'class': 'item-sweetbox'}
	, {'name': '4dx', 'class': 'item-4dx'}
	, {'name': 'dolby-atmos', 'class': 'item-dolby-atmos'}
	, {'name': 'imax', 'class': 'item-imax'}
	, {'name': 'gold-class', 'class': 'item-gold-class'}
	, {'name': 'lamour', 'class': 'item-lamour'}
	, {'name': 'starium', 'class': 'item-starium'}
	, {'name': 'premium', 'class': 'item-premium', 'flag': 'actived'}
	, {'name': 'screenx', 'class': 'item-screenx'}],
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
	[{'name': 'sweetbox', 'class': 'item-sweetbox'}
	, {'name': '4dx', 'class': 'item-4dx'}
	, {'name': 'dolby-atmos', 'class': 'item-dolby-atmos'}
	, {'name': 'imax', 'class': 'item-imax'}
	, {'name': 'gold-class', 'class': 'item-gold-class'}
	, {'name': 'lamour', 'class': 'item-lamour'}
	, {'name': 'starium', 'class': 'item-starium'}
	, {'name': 'premium', 'class': 'item-premium'}
	, {'name': 'screenx', 'class': 'item-screenx', 'flag': 'actived'}],
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
	data= {'name': 'Barry Seal: Lách Luật Kiểu Mỹ','director': ' Doug Liman', 'actor':'Tom Cruise, Domhnall Gleeson, Sarah Wright, E. Roger Mitchell, Jesse Plemons, Lola Kirke, Alejandro Edda, Benito Martinez, Caleb Landry Jones, Jayma Mays',
	'category': 'Hành Động, Hồi hộp, Phiêu Lưu', 'language': 'Tiếng Anh với phụ đề tiếng Việt và phụ đề tiếng Hàn',
	'time': '180 phút', 'rated': 'C18 - Phim cấm khán giả dưới 18 tuổi', 'date': '20/8/2017',
	'img': '/assets/websites/images/american_made_160x237.png', 
	'content': 'Dựa trên một câu chuyện có thật, BARRY SEAL: LÁCH LUẬT KIỂU MỸ là cuộc phiêu lưu xuyên quốc gia của Barry Seal, tên lừa đảo và cũng là một phi công bất ngờ được chiêu mộ vào tổ chức CIA để thực hiện một trong những điệp vụ ngầm lớn nhất trong lịch sử Mỹ.',
	'trailer': '//www.youtube.com/embed/PALCTTuWkSc?rel=0&amp;showinfo=0'}
	return render(request, 'websites/film_detail.html', {'data': data})
