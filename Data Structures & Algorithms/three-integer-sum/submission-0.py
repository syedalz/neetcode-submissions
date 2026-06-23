class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        nums = sorted(nums)
        ans = []

        # [-4,-1,-1,0,1,2]


        # 1. target = 4
        # j = 0, k = 1
        




        for i in range(len(nums)):

            target = -1 * nums[i]

            j = i + 1
            k = len(nums) - 1

            while j < k:

                if nums[j] + nums[k] < target:
                    j +=1

                elif nums[j] + nums[k] > target:
                    k -= 1

                else:
                    
                    if [nums[i],nums[j],nums[k]] not in ans:
                        ans.append([nums[i],nums[j],nums[k]])
                        
                    j +=1
                    k -=1


        
        return ans


