class Solution:
    def reverseWords(self, s: str) -> str:

        out = s.split()
        res = out[::-1]
        return ' '.join(res)

        