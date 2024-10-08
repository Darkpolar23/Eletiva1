import redis

redis_host = 'redis-19644.c9.us-east-1-2.ec2.redns.redis-cloud.com'  
redis_port = 19644  
redis_password = 's5vOM3EjiNwFNji9QToofIpJZL0v11tX'

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

def subscriber():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('canal_prueba')

    print("Esperando mensajes...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Recibido: {message['data']}")

if __name__ == "__main__":
    subscriber()
