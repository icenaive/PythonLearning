import time
nums = list(range(1, 1000001))
print(min(nums))
print(max(nums))
start = time.time()
all = sum(nums)
end = time.time()
print(all)
print(str(end - start))