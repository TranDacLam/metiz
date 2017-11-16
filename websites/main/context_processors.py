from django.conf import settings


def get_app_fb_id(request):
    FB_APP_ID = ''
    try:
        FB_APP_ID = settings.FB_APP_ID
    except:
        pass
    return {'FB_APP_ID': FB_APP_ID}
