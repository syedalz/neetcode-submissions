class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        count = [[] for i in range(len(nums) + 1)]

        cmap = {}

        ans=[]

        for n in nums:

            cmap[n] = 1 + cmap.get(n, 0)


        for key in cmap:
            count[cmap[key]].append(key)

        
        for i in range(len(count) -1, 0, -1):

            for n in count[i]:
                ans.append(n)

            if len(ans) == k:
                return ans