import redis

redis_host = 'redis-19644.c9.us-east-1-2.ec2.redns.redis-cloud.com'  
redis_port = 19644  
redis_password = 's5vOM3EjiNwFNji9QToofIpJZL0v11tX'

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

def publisher():
    while True:
        message = input("Introduce un mensaje para publicar: ")
        redis_client.publish('canal_prueba', message)
        print(f"Publicado: {message}")

if __name__ == "__main__":
    publisher()

