class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:

        closest = nums[0]

        for i in nums:
            if i == 0:
                return 0
            
            if i>0:
                if i < abs(closest):
                    closest = i
            
            if i < 0:

                if abs(closest)>= abs(i):
                    closest = i
                
                if abs(closest) >= abs(i) and abs(i) in nums :
                    closest = abs(i)
        return closest
                










        