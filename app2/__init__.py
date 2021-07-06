from celery import Celery
import redis

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
