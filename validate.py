"""
validate.py

Validates SlidingWindow statistics against NumPy.
"""

import numpy as np
from sliding_window import SlidingWindow

WINDOW_SIZE = 20
data = np.random.randn(1000)

window = SlidingWindow(WINDOW_SIZE)

for i, x in enumerate(data):
    window.append(x)
    expected = data[max(0, i - WINDOW_SIZE + 1): i + 1]

    assert abs(window.mean() - np.mean(expected)) < 1e-9
    assert abs(window.variance() - np.var(expected)) < 1e-9

print("✅ Validation passed: SlidingWindow matches NumPy")
