class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash = {}
        for i in nums:
            if i in hash.keys():
                return True
            else:
                hash[i] = 0
                
        return False


        

        

    