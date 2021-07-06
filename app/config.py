import os

for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace("\"", "")

def setupdb(url, password, db, port):
    db = redis.Redis(
        host=url,
        password=password,
        port=port,
        db=db
    )
    return(db)



TESTING=os.environ['TESTING']
DEBUG=os.environ['DEBUG']
QUART_ENV=os.environ['QUART_ENV']
SECRET_KEY=os.environ['SECRET_KEY']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
server = os.environ['SERVER']
redis_pass= os.environ['REDISPASS']
redis_server = os.environ['REDISURL']
redis_port = os.environ['REDISPORT']
redis_db = os.environ['REDISDB']
