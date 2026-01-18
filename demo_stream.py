%%writefile sliding_window.py
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
        return (self.sq_sum / self.count) - m * m
