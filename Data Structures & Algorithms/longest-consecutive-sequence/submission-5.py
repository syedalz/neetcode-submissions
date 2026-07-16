class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        print(nums)
        seq = 1
        longest = 1

        if len(nums) == 1:
            return 1
        
        elif not nums:
            return 0


        for i in range(1, len(nums)):
            

            if nums[i] == nums[i-1]:
                continue
            
            elif nums[i] == nums[i-1] + 1:
                    seq += 1


            else:
               longest = max(longest, seq)
               seq = 1




            
        longest = max(longest, seq)
        return longest


