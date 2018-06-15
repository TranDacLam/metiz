    var lang = $('html').attr('lang');
    if (lang == 'vi') {
        message_translate = {
            'required': 'Trường này bắt buộc',
            'phone': 'Số điện thoại không hợp lệ',
            'minlength_2': 'Nhập ít nhất 2 kí tự',
            'minlength_6': 'Nhập ít nhất 6 kí tự',
            'minlength_8': 'Mật khẩu chứa ít nhất 8 ký tự, bao gồm chữ, số và ký tự hoa hoặc ký tự đặc biệt.',
            'minlength_9' :'Nhập ít nhất 9 kí tự',
            'email': 'Email không hợp lệ',
            'rangelength_1_70': 'Họ và tên chứa ít nhất 1 kí tự và nhiều nhất 70 kí tự',
            'number': 'Vui lòng chỉ nhập các chữ số',
            'equalTo': 'Mật khẩu không khớp. Vui lòng nhập lại',
            'validatePassword': 'Mật khẩu chứa ít nhất 8 ký tự, bao gồm chữ, số và ký tự hoa hoặc ký tự đặc biệt.',
            'validateDate': 'Nhập ngày theo định dạng dd-mm-yyyy',
        }
    } else {
        message_translate = {
            'required': 'This field is required',
            'phone': 'Invalid telephone number',
            'minlength_2': 'Please enter at least 2 characters',
            'minlength_6': 'Please enter at least 6 characters',
            'minlength_8': 'Please enter at least 8 characters',
            'minlength_9' :'Please enter at least 9 characters',
            'email': 'Please enter a valid email address',
            'rangelength_1_70': 'Please enter a value between 1 and 70 characters long',
            'number': 'Please enter a valid number',
            'equalTo': "Password don't same. Please enter again",
            'validatePassword': 'Passwords must contain characters, numbers and at least 1 special character',
            'validateDate': 'Please enter a date in the format dd-mm-yyyy'
        }
    }