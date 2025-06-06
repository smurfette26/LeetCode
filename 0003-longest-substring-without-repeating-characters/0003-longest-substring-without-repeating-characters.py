class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        
        l = 0
        longest = 0
        h = set()
        n = len(s)

        for r in range(n):
            while s[r] in h:
                h.remove(s[l])
                l += 1
            w = (r-l)+1
            longest = max(longest,w)

            h.add(s[r])
        return longest



            

        



        
        