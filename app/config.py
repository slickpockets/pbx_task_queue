import os

for line in open('../.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace("\"", "")



TESTING=os.environ['TESTING']
DEBUG=os.environ['DEBUG']
FLASK_ENV=os.environ['FLASK_ENV']
SECRET_KEY=os.environ['SECRET_KEY']
