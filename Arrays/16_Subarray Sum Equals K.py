'''

560. Subarray Sum Equals K
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

'''

class Solution:
    def Subarray(self,nums,k):
        count=0
        for i in range(len(nums)):
            sum_arr=0
            for j in range(i,len(nums)):
                sum_arr+=nums[j]

                if sum_arr==k:
                    count+=1
        return count
object=Solution()
print(object.Subarray([1,1,1],2))

