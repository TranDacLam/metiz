import pyotp, datetime
from django.conf import settings


"""
    Author : TienDang
    Description: Action Generate OTP for User by Secret key ramdom
"""
def opt_user():
    try:
        serect_key = pyotp.random_base32()
        totp = pyotp.TOTP(serect_key, interval=settings.TIME_OTP)
        print "secret_key_otp store ",serect_key
        code = totp.at(datetime.datetime.now())
        return {"secret_key_otp": serect_key, "code_otp":code}
    except Exception, e:
        print "Error generate otp for user : ",e
        return  {"code_otp":"000000"}

"""
    Author : TienDang
    Description: Action Verify OTP for User
"""
def verify_otp_user(secret_key_otp, code_otp):
    # init data return with status is False
    result = {"status":False, "message":""}
    try:
        print "IMPUT OTP ",code_otp
        totp = pyotp.TOTP(str(secret_key_otp), interval=settings.TIME_OTP)
        code_generate = totp.at(datetime.datetime.now())

        # Check otp input macthing with otp generate
        # print "secret_key_otp ",secret_key_otp
        # print "code_generate OTP ",code_generate
        # if str(code_generate) != code_otp:
        #     result["message"] = "OTP wrong."
        #     return result
        
        # verify OTP check time expired
        verify_time_otp = totp.verify(code_otp, datetime.datetime.now())
        print "### Verify OTP Timeout"
        if not verify_time_otp:
            result["message"] = "OTP wrong or expired."
        
        result["status"] = verify_time_otp
        return result
    except Exception, e:
        print "Error generate otp for user : ",e
        result["message"] = "System Error. Please Contact Administrator."
        return result