class Solution(object):

    def getSubsets(self,nums,ans,i, allSubsets):

        if i == len(nums):
           
            return allSubsets.append(ans)

        ans.append(nums[i])
        self.getSubsets(nums,ans,i+1,allSubsets)

        ans.pop()
        self.getSubsets(nums,ans,i+1,allSubsets)        

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        allSubsets = []
        self.getSubsets(nums,ans,0,allSubsets)
        return allSubsets

        
