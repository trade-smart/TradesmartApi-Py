import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import logging

#supress debug messages for prod/tests
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)


#start of our program
api = NorenApiPy()

#use following if yaml isnt used
user    = "NIKHESHP"
pan     = "AAAAA1234A" 

#userid, pan, dob
ret = api.forgot_password_OTP(userid= user, pan=pan)

print(ret)
