# Sliding Window with 5 Different Inputs
# Screenshot-friendly output

import math

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
        return (self.sq_sum / self.count) - (m * m)


# -------------------------------
# TESTING WITH 5 DIFFERENT INPUTS
# -------------------------------

WINDOW_SIZE = 5

test_inputs = [
    ("Increasing",   [1, 2, 3, 4, 5, 6, 7]),
    ("Decreasing",   [7, 6, 5, 4, 3, 2, 1]),
    ("Constant",     [3, 3, 3, 3, 3, 3, 3]),
    ("Random",       [2.5, 7.1, 1.8, 9.0, 4.2, 6.6, 3.3]),
    ("Alternating",  [1, -1, 1, -1, 1, -1, 1]),
]

for name, data in test_inputs:
    print("=" * 45)
    print(f"Input Type : {name}")
    print(f"Input Data : {data}")
    print("-" * 45)

    window = SlidingWindow(WINDOW_SIZE)

    for x in data:
        window.append(x)
        print(
            f"Added: {x:>5} | "
            f"Mean: {window.mean():>6.2f} | "
            f"Variance: {window.variance():>6.2f}"
        )

    print()
