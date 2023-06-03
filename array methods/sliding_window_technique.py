# this is called the slding window technique
# not exactly an algorithm but more of a 2 pointer technique 
# that can be implemented many ways
# for example if we have an array and we are trying to find the total sum of every sub array length k
# instead of starting at the first index and adding every value until the subarray 
# reaches length of k and then having to move the pointer over 1 left and doing the same steps
# we can initialize with 2 pointers and and have them slide down the array while keeping that
# sub-array length of k

class Solution:
    def slide_window(self, nums, k):
        l, r = 0, k - 1
        total = 0
        res = []
        while r <= len(nums) - 1:
            for i in range(l, r):
                total += nums[i]
            res.append(total)
            l += 1
            r += 1
        return res