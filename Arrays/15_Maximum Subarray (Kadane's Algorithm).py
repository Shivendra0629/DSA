'''
53. Maximum Subarray
Medium
Topics
premium lock icon
Companies
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

'''

class Solution:
    def Maxsub(self,nums):
        max_sum= float('-inf') #=0 doesnt work if only one element is present in array with -ve sign its gives wrog ouput so we use -inf
        for i in range(len(nums)):
            curr_sum=0
            for j in range(i,len(nums)):
                curr_sum+=nums[j]
                max_sum=max(max_sum,curr_sum)
            
        return max_sum

obj=Solution()
print(obj.Maxsub([0,1,-2,3,4]))
print(obj.Maxsub([-2,1,-3,4,-1,2,1,-5,4]))
print(obj.Maxsub([5,4,-1,7,8]))
print(obj.Maxsub([1]))


class Solution:
    def MaxsubArray(self,nums):
        curr_sum=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
            curr_sum=max(nums[i],curr_sum+nums[i])
            max_sum=max(curr_sum,max_sum)

        return max_sum


obj=Solution()
print(obj.MaxsubArray([0,1,-2,3,4]))