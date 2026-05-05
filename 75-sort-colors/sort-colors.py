class Solution:
    def sortColors(self, nums: List[int]) -> None:

        size = len(nums)
        zero,one,two = 0,0,0
        

        for i in nums:
            if i == 0:
                zero = zero +1
            elif i == 1:
                one = one + 1
            else:
                two = two + 1
        i = 0

        while i < size:
            if zero > 0:
                nums[i] = 0
                zero = zero-1
                i = i+1
                continue
            elif one > 0:
                nums[i] = 1
                one = one - 1
                i = i+1
                continue
            elif two > 0:
                nums[i] = 2
                two = two + 1
                i = i+1
                continue
            





        """
        Do not return anything, modify nums in-place instead.
        """
        