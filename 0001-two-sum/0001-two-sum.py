class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        x = 0
        n = len(nums)

        while x < n:
            for i in range(x+1,n):
                if nums[x] + nums[i] == target:
                    return [x,i]
            
            x += 1



         
                


        