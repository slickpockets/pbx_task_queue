from app import celery
import requests
import phonenumbers
import hashlib
import hmac






@celery.task()
def requester(message, phonenumbers, password):
    finished_numbers = format_numbers(phonenumbers)
    data = {
     "password" : password,
     "phonenumbers" : finished_numbers,
     "message": message
    }
    r = requests.post("http://10.0.0.8/sms/index.php", data=data)

"""@celery.task()
def truexprochecker():
    url = "https://txpdev.txp.systems"
    r = requests.get(url)
    if r.status_code != 200 or 203:"""
