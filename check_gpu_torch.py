import torch
import time

print(f"CUDA 사용 가능: {torch.cuda.is_available()}")
print(f"현재 디바이스: {torch.cuda.current_device()}")
print(f"디바이스 이름: {torch.cuda.get_device_name(0)}")

num_runs = 10

# Approach 1: Generate on CPU and move to GPU
execution_times1 = []
for _ in range(num_runs):
    start_time = time.time()
    tensor1 = torch.rand(10000, 10000).cuda()
    end_time = time.time()
    execution_time1 = end_time - start_time
    execution_times1.append(execution_time1)

average_time1 = sum(execution_times1) / num_runs

# Approach 2: Allocate directly on GPU
execution_times2 = []
for _ in range(num_runs):
    start_time = time.time()
    tensor2 = torch.rand(10000, 10000, device=torch.device("cuda"))
    end_time = time.time()
    execution_time2 = end_time - start_time
    execution_times2.append(execution_time2)

average_time2 = sum(execution_times2) / num_runs

print("Approach 1 average execution time:", average_time1)
print("Approach 2 average execution time:", average_time2)
