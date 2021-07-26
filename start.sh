export AUTHLIB_INSECURE_TRANSPORT=true
celery -A tasks worker --loglevel=info -Q my_reverse_queue --pidfile=logs/%n.pid --logfile=logs/%n%I.log -D
##sleep 5
nohup celery -A tasks flower --address=127.0.0.1 --port=5577 > logs/flower.log 2>&1 &
# nohup celery -A tasks.reverse flower --port=5557 > logs/flower.log 2>&1 &
# nohup celery -A tasks flower --port=5555 > logs/flower.log 2>&1 &
