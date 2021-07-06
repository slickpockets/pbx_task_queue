from app import celery
import requests
import phonenumbers
import hashlib
import hmac
import imaplib
import email
from email.header import decode_header
import webbrowser
import redis
import os

#grab configs
for line in open('.env'):
    var = line.strip().split('=')
    if len(var) == 2:
        os.environ[var[0]] = var[1]

username = os.environ['USERNAME']
password = os.environ['PASSWORD']
server = os.environ['SERVER']
redis_pass= os.environ['REDISPASS']
redis_server = os.environ['REDISURL']
redis_port = os.environ['REDISPORT']
redis_db = os.environ['REDISDB']

db = redis.Redis(
    host=redis_server,
    port=redis_port,
    password=redis_pass
)

def clean(text):
    return("".join(c if c.isalnum() else "_" for c in text))

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

def check_message_number():
    return(db.get("message_number"))

@celery.task()
def check_email():
    return("TODO")
