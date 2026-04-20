class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        # Find leftmost position
        def findLeft(l, r):
            if l > r:
                return -1
            
            mid = (l + r) // 2
            
            if nums[mid] < target:
                return findLeft(mid + 1, r)
            elif nums[mid] > target:
                return findLeft(l, mid - 1)
            else:
                # Found target, but search left for leftmost
                result = findLeft(l, mid - 1)
                return result if result != -1 else mid
        
        # Find rightmost position
        def findRight(l, r):
            if l > r:
                return -1
            
            mid = (l + r) // 2
            
            if nums[mid] < target:
                return findRight(mid + 1, r)
            elif nums[mid] > target:
                return findRight(l, mid - 1)
            else:
                # Found target, but search right for rightmost
                result = findRight(mid + 1, r)
                return result if result != -1 else mid
        
        leftptr = findLeft(0, len(nums) - 1)
        
        if leftptr == -1:
            return [-1, -1]
        
        rightptr = findRight(0, len(nums) - 1)
        
        return [leftptr, rightptr]