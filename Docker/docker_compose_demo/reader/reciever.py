import redis
import time
from pathlib import Path


time.sleep(2)

r = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)


out = Path('/data/hello.txt')

with out.open('a') as f:
    f.write(f"Hello docker volume : {r.get("current_time")}\n")