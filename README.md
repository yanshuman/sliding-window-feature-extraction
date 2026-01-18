# Custom Sliding Window Data Structure for Feature Extraction

## Overview
A high-performance circular buffer for streaming data that supports
O(1) append operations and rolling mean/variance computation.

## Features
- Fixed-size circular buffer
- O(1) updates
- Rolling mean and variance
- Async streaming simulation
- NumPy validation
- Microsecond-level latency

## Tech Stack
- Python 3.x
- asyncio
- NumPy

## Run Streaming Demo
```bash
python demo_stream.py
