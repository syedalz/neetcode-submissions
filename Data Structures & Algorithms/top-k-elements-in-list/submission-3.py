class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        countList = [[] for i in range(len(nums) + 1)]

        ans = []

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        for key in count:
            countList[count[key]].append(key)

        for i in range(len(countList) - 1, 0, -1):
            for n in countList[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
