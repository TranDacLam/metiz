import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATABASES = {
    'default': {
        'NAME': 'metiz_dev',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'root'
    }
}
# Default Email Contact
DEFAULT_TO_ADMIN_EMAIL = "thaophan@vooc.vn"

# VNPAY CONFIG
VNPAY_RETURN_URL = 'http://metiz.dht:8000/payment_return'  # get from config
VNPAY_PAYMENT_URL = 'http://sandbox.vnpayment.vn/paymentv2/vpcpay.html'  # get from config
VNPAY_API_URL = 'http://sandbox.vnpayment.vn/merchant_webapi/merchant.html'
VNPAY_TMN_CODE = 'HELIOKP1'  # Website ID in VNPAY System, get from config
VNPAY_HASH_SECRET_KEY = 'YTDBTUZONRERICMBLYIRTRTEJDPCZDFK'  # Secret key for create checksum,get from config

# POS Cinestar config
CINESTAR_SERECT_KEY = 'df733de5b7394530835a2d61ce20e220'
BASE_URL_CINESTAR = 'http://kingproserver.ddns.net:8085/demo.asmx'

# SMS Config
SMS_BRAND = "HelioCenter"
SMS_USER = "heliocenter"
SMS_PASSWORD = "truyenthonghelio"
SMS_KEY = "VNFPT123BLUESEA1"
SMS_KEY_IV = "154dxc1scfzzad21"
SMS_URL = "http://ws.ctnet.vn/servicectnet.asmx?op=sendsms"

FB_APP_ID = '1761455193886139'