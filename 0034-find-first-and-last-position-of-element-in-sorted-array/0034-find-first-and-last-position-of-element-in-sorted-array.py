class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        tar = []
        n = len(nums)
        l = 0
        r = n-1

        if n==0:
            return [-1,-1]
        if n == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]

        for i in range(n):
            if nums[i] == target:
                tar.append(i)
        
        if len(tar)==0:
            return [-1,-1]
        if len(tar) == 1:
            return [tar[0],tar[0]]
        if len(tar) > 2:
            tar = [tar[0],tar[(len(tar)-1)]]
            # return ([range(tar[0],tar[len(tar)-1])])
        
        return tar