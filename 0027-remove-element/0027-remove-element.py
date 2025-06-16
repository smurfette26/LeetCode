class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        n = len(nums)
        i = 0
        j = n-1
        res = 0
        for i in range(n):
            if nums[i] == val:
                res += 1

        i = 0
        while i < j:
            while nums[i] != val and i < j:
                i += 1
            while nums[j] == val and j > i:
                j -= 1

            if i >= j:
                break
            nums[i],nums[j] = nums[j],nums[i]
            
            

        return n-res
    

        