class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        t = -1
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                t = i
        
        return t
        