from app import redis_client

import json

def if_cache_hit(key):
    cached_result = redis_client.get(key)
    
    if cached_result:
        cached_result = json.loads(cached_result)
        print("cache hit")
        return cached_result
    else:
        return None

def cache_result(key, result):
    redis_client.setex(key,30, json.dumps(result))
