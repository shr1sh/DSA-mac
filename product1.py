nums = [1,2,4,6]
n = len(nums)
prefix = [1]*n

for i in range(1,len(nums)):
    prefix[i] = prefix[i-1] * nums[i-1]
print(prefix)

suffix = [1]*n
for i in range(len(nums)-2,-1,-1):
    suffix[i] = suffix[i+1]*nums[i+1]
print(suffix)

ans = []
for j in range(len(nums)):
    ans.append(prefix[j] * suffix[j])
print(ans)


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)

#         prefix = [1] * n
#         for i in range(1, n):
#             prefix[i] = prefix[i-1] * nums[i-1]

#         suffix = [1] * n
#         for i in range(n-2, -1, -1):
#             suffix[i] = suffix[i+1] * nums[i+1]

#         ans = [prefix[i] * suffix[i] for i in range(n)]
#         return ans