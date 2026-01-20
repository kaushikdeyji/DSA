class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            False
        temp=x
        reversed=0

        while temp > 0:
            reversed = reversed*10 + temp%10
            temp //= 10
        return x==reversed


        