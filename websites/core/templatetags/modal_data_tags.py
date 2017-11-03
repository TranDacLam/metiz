# -*- coding: utf-8 -*-
from django import template
from datetime import timedelta
from django.utils import timezone
from core.models import Movie
from booking.models import MovieSync

register = template.Library()


@register.filter
def floatdot(value, decimal_pos=4):
    return format(value, '.%if' % decimal_pos)


floatdot.is_safe = True


@register.simple_tag
def get_movie_name(movie_id):
    try:
        m = Movie.objects.get(movie_api_id=movie_id)
        return m.name
    except Movie.DoesNotExist, e:
        return None
    except Exception, e:
        return None


@register.simple_tag
def verify_showtime_by_id(cinema_id, movie_api_id):
    try:
        """
            Get all movie sync with condition date show greater than or equal to current date
            Check data movie contain movie_api_id 
        """
        result = False

        data_movie = MovieSync.objects.filter(
            name="showtime_current", date_show__gte=timezone.localtime(timezone.now()).date(), cinema_id=1)
        
        if data_movie:
            for item in data_movie:
                if item.data.find(movie_api_id) > -1:
                    result = True
                    break
        return result
    except Exception, e:
        return False


@register.simple_tag
def get_date_showing():
    current_date = timezone.localtime(timezone.now()).date()
    end_date = current_date + timedelta(days=6)
    step_date = timedelta(days=1)

    result = []
    while current_date <= end_date:
        result.append(current_date)
        current_date = current_date + step_date
    return result


@register.simple_tag
def get_cites():
    return {"data": ["Đà Nẵng"]}


@register.simple_tag
def get_cinema_cites():
    return ["Metiz Cinema"]

@register.simple_tag
def get_term():
	return "ĐIỀU KIỆN VÀ ĐIỀU KHOẢN KHI ĐẶT VÉ: \n Xin vui lòng đọc các điều khoản sau cẩn thận trước khi sử dụng dịch vụ thanh toán trực tuyến. Với việc truy cập vào phần này của website, bạn đã đồng ý với các điều khoản sử dụng của chúng tôi. Các điều khoản này có thể thay đổi theo thời gian và bạn sẽ phải tuân theo các điều khoản được hiển thị từ thời điểm bạn đọc được các điều khoản này. Metiz Cinema luôn luôn mong muốn đem đến những giây phút giải trí tuyệt vời cho khách hàng với chất lượng dịch vụ tốt nhất. Dưới đây sẽ là một số hướng dẫn cho chính sách thanh toán vé trực tuyến.1. Đối tượng áp dụngChương trình thanh toán online chỉ áp dụng cho các suất chiếu quy định tại Metiz Cinema. Mỗi giao dịch đặt vé có thể thanh toán trực tuyến tối đa 8 vé cho một lần. Nếu bạn có nhu cầu mua vé với số lượng lớn hơn, vui lòng liên hệ với bộ phận Quan Hệ Khách Hàng của chúng tôi qua số điện thoại 1900 6017"