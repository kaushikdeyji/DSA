class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       charset = set()
       leftptr = 0
       result=0

       for rightptr in range(len(s)):
        while s[rightptr] in charset:
            charset.remove(s[leftptr])
            leftptr += 1
        charset.add(s[rightptr])
        result = max(result, rightptr - leftptr +1)
       return result


        