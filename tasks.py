from celery import Celery
import celery_conf

APP_NAME = 'tasks'
# BROKER_NAME = 'redis://127.0.0.1:6379/0'
# BACKEND = 'redis://127.0.0.1:6379/1'
app = Celery(name=APP_NAME)
app.config_from_object(celery_conf)


@app.task
def reverse(my_str):
    return my_str[::-1]
