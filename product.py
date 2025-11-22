nums = [1,2,4,6]
pd1 = []
j,k = 0,0
product = 1
l = 0
while j<len(nums):
    nums1 = nums.copy() # nums1 = [1,2,4,6]
    j=k   # j=k=0
    while j==k: # 0==0
        nums1.pop(j)            # nums1 = [2,4,6]
        product = 1             
        for l in range(len(nums1)):  # 
            product *= nums1[l]      # product = 1*2 , product = 2*4 ,product *= 8*6=48
        pd1.append(product)
        k+=1
    j+=1
print(pd1)



# while j<len(nums):
#     nums1 = nums.copy()
#     # nums1.pop(j)
#     j=k
#     while j==k:
#         nums1.pop(j)
#         product *= nums1[k]
#         k+=1
#     pd1.append(product)
# print(pd1)
