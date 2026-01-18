"""
sliding_window.py

High-performance sliding window (circular buffer) for streaming feature extraction.
Supports O(1) append, rolling mean, and variance.
"""

import math


class SlidingWindow:
    """
    Fixed-size circular buffer supporting O(1) updates
    and rolling statistics.
    """

    def __init__(self, size: int):
        self.size = size
        self.buffer = [0.0] * size
        self.index = 0
        self.count = 0
        self.sum = 0.0
        self.sq_sum = 0.0

    def append(self, value: float) -> None:
        """
        Append a new value to the sliding window.
        """
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

    def mean(self) -> float:
        """
        Return rolling mean.
        """
        return self.sum / self.count if self.count else 0.0

    def variance(self) -> float:
        """
        Return rolling variance.
        """
        if self.count == 0:
            return 0.0
        m = self.mean()
        return (self.sq_sum / self.count) - (m * m)

    def std(self) -> float:
        """
        Return rolling standard deviation.
        """
        return math.sqrt(self.variance())
