n, s = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
maxSum = 0
count = 0

for end in range(n):
    maxSum += nums[end]

    while maxSum > s and start <= end:
        maxSum -= nums[start]
        start += 1

    count = max(count, end - start + 1)

print(count)
