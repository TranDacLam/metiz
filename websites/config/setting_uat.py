import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATABASES = {
    'default': {
        'NAME': 'metiz_db',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'helio',
        'PASSWORD': 'admin@helio.vn'
    }    
}

# VNPAY CONFIG
VNPAY_RETURN_URL = 'http://103.95.197.103:8000/payment_return'  # get from config
VNPAY_PAYMENT_URL = 'http://sandbox.vnpayment.vn/paymentv2/vpcpay.html'  # get from config
VNPAY_API_URL = 'http://sandbox.vnpayment.vn/merchant_webapi/merchant.html'
VNPAY_TMN_CODE = 'ZJLNTI3D'  # Website ID in VNPAY System, get from config
VNPAY_HASH_SECRET_KEY = 'LAJRLYXKVBAOGGQIRTKTNRYCWQOVJBZR'  # Secret key for create checksum,get from config
