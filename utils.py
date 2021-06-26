import hashlib
import hmac
import datetime
import time
#import uuid
#new = uuid.uuid4()
uuid = 'fb480c4d-a561-4f9b-acb3-879112cf9bd9'
nonce = 1619167325
def calculate_hash(uuid, nonce):
    new = hashlib.new('sha512_256')
    new.update(uuid)
    new.update(nonce)
    return new.hexidgest()
