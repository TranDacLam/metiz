from django.conf import settings


def get_app_fb_id(request):
    FB_APP_ID = ''
    try:
        FB_APP_ID = settings.FB_APP_ID
    except:
        pass
    return {'FB_APP_ID': FB_APP_ID}


def get_app_recaptcha_key(request):
    RECAPTCHA_PUBLIC_KEY = ''
    try:
        RECAPTCHA_PUBLIC_KEY = settings.RECAPTCHA_PUBLIC_KEY
    except:
        pass
    return {'RECAPTCHA_PUBLIC_KEY': RECAPTCHA_PUBLIC_KEY}