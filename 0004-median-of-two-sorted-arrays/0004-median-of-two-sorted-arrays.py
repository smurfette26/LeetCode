class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = nums1 + nums2

        # sorting the arrey

        # sorting arrey
        x.sort()
        n = len(x)
        value = 0
        
        if n % 2 == 0:
            numEven = (n/2) + ((n/2)+1)
            numEven = numEven/2
            firstInd = int(numEven-1.5)
            secondInd = int(numEven-0.5)
            value1 = x[firstInd]
            value2 = x[secondInd]
            value = (value1+value2)
            value = value/2
        else:
            numOdd = (n-1)
            numOdd = numOdd//2
            value = x[numOdd]

        return value