class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
       
        def bs(i, j):
            # ✅ Add base case
            if i > j:
                return -1
            
            mid = (i + j) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bs(mid + 1, j)   # ✅ Add return
            else:
                return bs(i, mid - 1)   # ✅ Add return
        
        return bs(0, size - 1)          # ✅ Add return