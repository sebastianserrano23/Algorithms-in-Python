# we are using kadane's algorithm to solve leetcode 53 
# maximum subarray
# kadane's algorithm utilizes a 2 pointer approach
# The idea of Kadane’s algorithm is to maintain a variable max_ending_here that 
# stores the maximum sum contiguous subarray ending at current index and a 
# variable max_so_far stores the maximum sum of contiguous subarray found so far, 
# Everytime there is a positive-sum value in max_ending_here compare it with max_so_far 
# and update max_so_far if it is greater than max_so_far.
# So the main Intuition behind Kadane’s algorithm is, 
# - the subarray with a negative sum is discarded (by assigning max_ending_here = 0)
# - we carry the subarray till it gives positive sum

# code below will be kadane's algorithm

from typing import List


def maxSubArray(nums: List[int]) -> int:
        maxSum = nums[0] # set the maxSum to the value of the first index since the subarray is non 0
        curSum = 0 # set the value of current sum = 0
        
        for i in range(len(nums)): # loop through the values of the array
            if curSum < 0: # if curSum ever becomes negative, we reset it equal to 0
                curSum = 0 
            curSum += nums[i] # we add the current value of i to our current sum
            maxSum = max(maxSum, curSum) # we set maxSum to whiever is greater between maxSum or curSum
        return maxSum # we return maxSum
