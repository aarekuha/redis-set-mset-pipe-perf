from rediscluster import RedisCluster
from typing import Mapping
from time import monotonic
from random import randint

COUNT: int = 50000
startup_nodes = [
        {"host": "173.18.0.2", "port": "6379"},
        {"host": "173.18.0.3", "port": "6379"},
        {"host": "173.18.0.4", "port": "6379"},
        {"host": "173.18.0.5", "port": "6379"},
        {"host": "173.18.0.6", "port": "6379"},
        {"host": "173.18.0.7", "port": "6379"},
]
r = RedisCluster(startup_nodes=startup_nodes)

start_time: float
total_time: float

# SET testing
start_time = monotonic()

for i in range(COUNT):
    r.set(str(randint(0, 10**6)), randint(0, 10**6))

total_time = monotonic() - start_time
print(f"SET: {total_time=}")

# MSET testing
start_time = monotonic()

keys: list[str] = [str(randint(0, 10**6)) for _ in range(COUNT)]
values: list[int] = [randint(0, 10**6) for _ in range(COUNT)]
r.mset({k: v for k, v in zip(keys, values)})

total_time = monotonic() - start_time
print(f"MSET: {total_time=}")

# PIPE testing
start_time = monotonic()
pipe = r.pipeline()

for i in range(COUNT):
    pipe.set(str(randint(0, 10**6)), randint(0, 10**6))

pipe.execute()
total_time = monotonic() - start_time
print(f"PIPE: {total_time=}")
