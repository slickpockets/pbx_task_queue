from celery import Celery
import redis
import os
for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace("\"", "")


redis_pass= os.environ['REDISPASS']
redis_server = os.environ['REDISURL']
redis_port = os.environ['REDISPORT']
redis_db = os.environ['REDISDB']

def setupdb(url, password, db, port):
    db = redis.StrictRedis(
        host=url,
        password=password,
        port=port,
        db=db,
        decode_responses=True
    )
    return(db)


def make_celery(app_name =__name__):
    redis_uri = "redis://localhost:6379"
    return Celery(app_name, backend=redis_uri, broker=redis_uri)



db = setupdb(redis_server, redis_pass, redis_port, redis_db)
celery = make_celery()
