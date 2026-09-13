class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = {}

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1

        frequency = (sorted(freq.items(), key=lambda x: (-x[1], x[0])))
        
        max = []
        for i in range(0,k):
            max.append(frequency[i][0])
        
        return max


        
