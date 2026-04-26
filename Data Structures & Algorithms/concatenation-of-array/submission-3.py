class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(2):
            for i in range(len(nums)):
                arr.append(nums[i])

        return arr