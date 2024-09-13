class Solution:
    def removeElements(self, nums, value):
        unique_elements=0
        for index in range(len(nums)):
            if nums[index] != value:
                nums[unique_elements] = nums[index]
                unique_elements+=1
        for j in range(unique_elements,len(nums)):
            nums[j]='_'
        return unique_elements
nums = [0,1,2,2,3,0,4,2]
nums1=[3,2,2,3]
val = 2
val1=3
solution=Solution()
result=solution.removeElements(nums,val)
result1=solution.removeElements(nums1,val1)
print(result1)
print(nums1)
print('2nd input.')
print(result)
print(nums)
