from app import celery
import requests


@celery.task()
def requester(message, phonenumbers, password):
    data = {
     "password" : password,
     "phonenumbers" : phonenumbers,
     "message": message
    }
    print(phonenumbers, message)
    r = requests.post("http://10.0.0.8/sms/index.php", data=data)
