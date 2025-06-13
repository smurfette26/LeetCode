class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sorting the arrey
        def dis(a,b,c,d):
            return a != b and a != c and a != d and b != c and b != d and c !=d

        h = {}
        n = len(nums)
        for i in range(n):
            h[nums[i]]= i
        
        s = set()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    res = target - nums[i] - nums[j] - nums[k]
                    if res in h and dis(i,j,k,h[res]):
                        t = tuple(sorted([nums[i],nums[j],nums[k],res]))
                                           
                        s.add(t)
        l = []

        for i in s:
            l.append(list(i))
        
        return l








        