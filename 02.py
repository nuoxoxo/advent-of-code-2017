res = 0
res2 = 0
for nums in [list(map(int,_.split()))for _ in open(0).read().splitlines()]:
    l,s = max(nums),min(nums)
    res += abs(l-s)
    N = len(nums)
    nums.sort(reverse=True)
    for i in range(N - 1):
        l = nums[i]
        for j in range(i + 1, N):
            if nums[i] % nums[j] == 0:
                res2 += nums[i] // nums[j]
print(res,res2)
