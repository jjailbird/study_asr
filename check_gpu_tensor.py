import tensorflow as tf
import time
from tensorflow.python.client import device_lib

print(device_lib.list_local_devices())

print("Available GPUs:", tf.config.list_physical_devices('GPU'))

num_runs = 10

# Approach 1: Generate on CPU and move to GPU
execution_times1 = []
for _ in range(num_runs):
    start_time = time.time()
    with tf.device('/CPU:0'):
        tensor1 = tf.random.uniform([10000, 10000])
    with tf.device('/GPU:0'):
        tensor1 = tf.identity(tensor1)
    end_time = time.time()
    execution_time1 = end_time - start_time
    execution_times1.append(execution_time1)

average_time1 = sum(execution_times1) / num_runs

# Approach 2: Allocate directly on GPU
execution_times2 = []
for _ in range(num_runs):
    start_time = time.time()
    with tf.device('/GPU:0'):
        tensor2 = tf.random.uniform([10000, 10000])
    end_time = time.time()
    execution_time2 = end_time - start_time
    execution_times2.append(execution_time2)

average_time2 = sum(execution_times2) / num_runs

print("Approach 1 average execution time:", average_time1)
print("Approach 2 average execution time:", average_time2)