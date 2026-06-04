from datetime import datetime
import redis

r = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

current_time = datetime.now()

r.set(
    "current_time",
    str(current_time)
)

print(f"Time saved : {current_time}")