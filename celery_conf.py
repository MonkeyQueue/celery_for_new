import tasks

broker_url = 'redis://127.0.0.1:6379/0'
result_backend = 'redis://127.0.0.1:6379/1'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Shanghai'
#imports = [tasks]
task_queues = {
    'my_reverse_queue':{
        'exchange':'reverse_str',
        'exchange_type': 'direct',
        'routing_key': 'reverse_str'
    },
}

task_routes = ({
    'tasks.reverse':{
        'queue': 'my_reverse_queue',
        'routing_key': 'reverse_str',
        'serializer':'json',
    }
},)
