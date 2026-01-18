import math
import asyncio
import random
import time

class SlidingWindow:
    def __init__(self, size):
        self.size = size
        self.buffer = [0.0] * size
        self.index = 0
        self.count = 0
        self.sum = 0.0
        self.sq_sum = 0.0

    def append(self, value):
        if self.count == self.size:
            old = self.buffer[self.index]
            self.sum -= old
            self.sq_sum -= old * old
        else:
            self.count += 1

        self.buffer[self.index] = value
        self.sum += value
        self.sq_sum += value * value
        self.index = (self.index + 1) % self.size

    def mean(self):
        return self.sum / self.count if self.count else 0.0

    def variance(self):
        if self.count == 0:
            return 0.0
        m = self.mean()
        return (self.sq_sum / self.count) - m * m

async def stream():
    window = SlidingWindow(50)
    for _ in range(50):
        x = random.uniform(0, 100)
        start = time.perf_counter()
        window.append(x)
        latency = (time.perf_counter() - start) * 1e6
        print(f"x={x:.2f}, mean={window.mean():.2f}, latency={latency:.2f} µs")
        await asyncio.sleep(0.01)

await stream()
