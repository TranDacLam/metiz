from calendar import timegm
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import exceptions
from django.utils.translation import ugettext_lazy as _


class CustomJSONWebTokenAuthentication(JSONWebTokenAuthentication):

    def authenticate_credentials(self, payload):
        """
            While changing password: when the user changes his password, 
            note the change password time in the user db, so when the change password time is greater than the token creation time, 
            then token is not valid. Hence the remaining session will get logged out soon.
        """
        try:
            user = super(CustomJSONWebTokenAuthentication,
                         self).authenticate_credentials(payload)
            iat_timestamp = timegm(user.token_last_expired.utctimetuple())

            if iat_timestamp > payload['orig_iat']:
                raise exceptions.AuthenticationFailed(_('Invalid token.'))
        except Exception, e:
            print "JWT authenticate_credentials ", e
            raise exceptions.AuthenticationFailed(_('Invalid token.'))
        return user
