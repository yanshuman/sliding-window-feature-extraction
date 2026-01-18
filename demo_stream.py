"""
demo_stream.py

Simulates a real-time data stream using asyncio and
computes rolling mean and variance.
"""

import asyncio
import random
import time
from sliding_window import SlidingWindow

WINDOW_SIZE = 50
STREAM_DELAY = 0.01  # seconds


async def stream():
    window = SlidingWindow(WINDOW_SIZE)
    latencies = []

    for _ in range(200):
        value = random.uniform(0, 100)

        start = time.perf_counter()
        window.append(value)
        mean = window.mean()
        var = window.variance()
        latency = (time.perf_counter() - start) * 1e6  # microseconds

        latencies.append(latency)

        print(
            f"value={value:.2f}, mean={mean:.2f}, "
            f"variance={var:.2f}, latency={latency:.2f} µs"
        )

        await asyncio.sleep(STREAM_DELAY)

    print("\n--- Latency Summary ---")
    print(f"Average: {sum(latencies)/len(latencies):.2f} µs")
    print(f"Max: {max(latencies):.2f} µs")
    print(f"Min: {min(latencies):.2f} µs")


if __name__ == "__main__":
    asyncio.run(stream())
