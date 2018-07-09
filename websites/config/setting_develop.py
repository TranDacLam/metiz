import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATABASES = {
    'default': {
        'NAME': 'metiz_dev',
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'Admin@v00c.vn'
    }
}
# Default Email Contact
SYSTEM_ADMIN_CINEMA_EMAIL = "thaophan@vooc.vn, diemnguyen@vooc.vn"
SYSTEM_ADMIN_CINEMA_EMAIL_CC = ["diemnt.pnv@gmail.com", "diemnguyen.2t@gmail.com"]
POS_ADMIN_EMAIL = "thaophan@vooc.vn, diemnguyen@vooc.vn"
SYSTEM_ADMIN_CINEMA_PHONE = "0905242259"
DEFAULT_TO_ADMIN_EMAIL = "thaophan@vooc.vn"

# VNPAY CONFIG
VNPAY_RETURN_URL = 'http://172.16.12.10:8000/payment_return'  # get from config
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

RECAPTCHA_PUBLIC_KEY = '6LdK2joUAAAAAPAQD6SA-lTh3gR0J6B9RXPpGDDe'
RECAPTCHA_PRIVATE_KEY = '6LdK2joUAAAAALA1kD-Bom5iUOrn31oNiZs4n7wu'

BOOKING_ERROR_CC_EMAIL = "diemnguyen@vooc.vn, thaophan@vooc.vn"

# POS API config
AUTH_PREFIX = "Bearer "
BASE_URL_POS_API = "http://172.16.12.19:9090/api/"
POS_API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InBvc19kZXZAdm9vYy52biIsIm9yaWdfaWF0IjoxNTI4NDQxMzQ2LCJ1c2VyX2lkIjoyLCJlbWFpbCI6InBvc19kZXZAdm9vYy52biIsImV4cCI6MTUyODQ0MTY0Nn0.dCazTJKBi-_aQzfeUZQ8mGxaperkitiBWqnNsVM9gDA"
POS_API_AUTH_HEADER = AUTH_PREFIX + POS_API_TOKEN


HELIO_API_DMZ_URL = "http://172.16.12.10:9000"
DMZ_API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluQHZvb2Mudm4iLCJvcmlnX2lhdCI6MTUyMTYwNjc2NSwidXNlcl9pZCI6MSwiZW1haWwiOiJhZG1pbkB2b29jLnZuIiwiZXhwIjoxNTIxNjA3MDY1fQ.9hE6nQzUboTHYdG3kexLoJiTDAVYM-jIheXBFFr0gmM"

TIME_SEAT_DELAY = 5

# Time interval for OTP
TIME_OTP = 120

BUILD_VERSION=2