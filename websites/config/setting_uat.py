import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATABASES = {
    'default': {
        'NAME': 'metiz_uat',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'metiz_admin',
        'PASSWORD': 'Admin@Met1z.vn'
    }    
}

# Default Email Contact
DEFAULT_TO_ADMIN_EMAIL = "contact@metiz.vn"

# VNPAY CONFIG
VNPAY_RETURN_URL = 'http://uat.metiz.vn/payment_return'  # get from config
VNPAY_PAYMENT_URL = 'http://sandbox.vnpayment.vn/paymentv2/vpcpay.html'  # get from config
VNPAY_API_URL = 'http://sandbox.vnpayment.vn/merchant_webapi/merchant.html'
VNPAY_TMN_CODE = 'HELIOKP1'  # Website ID in VNPAY System, get from config
VNPAY_HASH_SECRET_KEY = 'YTDBTUZONRERICMBLYIRTRTEJDPCZDFK'  # Secret key for create checksum,get from config


# POS Cinestar config
CINESTAR_SERECT_KEY = '5ba90f1cc2d540edbb01e3ffc85bc7f2'
BASE_URL_CINESTAR = 'http://113.176.107.20:8080/helio.asmx'

# SMS Config
SMS_BRAND = "HelioCenter"
SMS_USER = "heliocenter"
SMS_PASSWORD = "truyenthonghelio"
SMS_KEY = "VNFPT123BLUESEA1"
SMS_KEY_IV = "154dxc1scfzzad21"
SMS_URL = "http://ws.ctnet.vn/servicectnet.asmx?op=sendsms"

FB_APP_ID = '156569091618914'

RECAPTCHA_PUBLIC_KEY = '6LfW2zoUAAAAAANgpuK2Yw5-z7P8S6TeODY2qNsS'
RECAPTCHA_PRIVATE_KEY = '6LfW2zoUAAAAANhdyvbJnq9Hg4jxOFKFR3T2yU9A'