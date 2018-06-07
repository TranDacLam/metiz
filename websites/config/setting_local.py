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
SYSTEM_ADMIN_CINEMA_EMAIL = "thaophan@vooc.vn, diemnguyen@vooc.vn"
SYSTEM_ADMIN_CINEMA_EMAIL_CC = ["diemnt.pnv@gmail.com", "diemnguyen.2t@gmail.com"]

# VNPAY CONFIG
VNPAY_RETURN_URL = 'http://metiz.dht:8000/payment_return'  # get from config
VNPAY_PAYMENT_URL = 'http://sandbox.vnpayment.vn/paymentv2/vpcpay.html'  # get from config
VNPAY_API_URL = 'http://sandbox.vnpayment.vn/merchant_webapi/merchant.html'
VNPAY_TMN_CODE = 'HELIOKP1'  # Website ID in VNPAY System, get from config
VNPAY_HASH_SECRET_KEY = 'YTDBTUZONRERICMBLYIRTRTEJDPCZDFK'  # Secret key for create checksum,get from config

# POS Cinestar config
CINESTAR_SERECT_KEY = '5ba90f1cc2d540edbb01e3ffc85bc7f2'
BASE_URL_CINESTAR = 'http://172.16.12.13:8080/helio.asmx'

# SMS Config
SMS_BRAND = "MetizCinema"
SMS_USER = "metizcinema"
SMS_PASSWORD = "metizcinema123"
SMS_KEY = "VNFPT123BLUESEA1"
SMS_KEY_IV = "154dxc1scfzzad21"
SMS_URL = "http://ws.ctnet.vn/servicectnet.asmx?op=sendsms"

FB_APP_ID = '1761455193886139'

RECAPTCHA_PUBLIC_KEY = '6LfP2zoUAAAAAGhMBQuEguqc6ZV7JHIUdGuOGFJ0'
RECAPTCHA_PRIVATE_KEY = '6LfP2zoUAAAAACZmN3tAOOVCCE0U5BZeCtpTRAki'

MOVIE_ID_TEST = 'd8147d70-ee34-4a44-af46-36956f636fa9'


# POS API config
AUTH_PREFIX = "Bearer "
BASE_URL_POS_API = "http://127.0.0.1:8003/api/"
POS_API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImRpZW1uZ3V5ZW5Adm9vYy52biIsIm9yaWdfaWF0IjoxNTIxMDk4NDk1LCJ1c2VyX2lkIjoxLCJlbWFpbCI6ImRpZW1uZ3V5ZW5Adm9vYy52biIsImV4cCI6MTUyMTA5ODc5NX0.UYRCf2Pvc0HXYXfhKDVE0kZelBxaRWpPOA4GRgE_vI4"
POS_API_AUTH_HEADER = AUTH_PREFIX + POS_API_TOKEN