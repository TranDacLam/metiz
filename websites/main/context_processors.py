from django.conf import settings
from django.template import Context


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

def get_app_fb_id(request):
    HOT_LINE = ''
    try:
        HOT_LINE = settings.HOT_LINE
    except:
        pass
    return {'HOT_LINE': HOT_LINE}

def get_movie_id_test(request):
    MOVIE_ID_TEST = ''
    try:
        MOVIE_ID_TEST = settings.MOVIE_ID_TEST
    except:
        pass

    return {'MOVIE_ID_TEST': MOVIE_ID_TEST}