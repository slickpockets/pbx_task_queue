from app import celery
import requests

@celery.task()
def make_file(fname, content):
    with open(fname, "w") as f:
        f.write(content)

@celery.task()
def requester(message, phonenumbers):
    r = requests.post("http://10.0.0.8/sms/index.php")
    data = {
     "password" : "Prudence33",
     "phonenumbers" : phonenumbers,
     "message": message
    }
    print(phonenumbers, message)
    r = requests.post("http://10.0.0.8/sms/index.php", data=data)
