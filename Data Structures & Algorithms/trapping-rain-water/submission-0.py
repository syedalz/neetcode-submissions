class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r = 0, len(height) - 1
        maxL= -1
        maxR = -1

        maxW  = 0


        while l < r:

            maxL = max(height[l], maxL)
            maxR = max(height[r], maxR)


            if maxL <= maxR:
                    
                maxW += min(maxL,maxR) - height[l]
                l+=1

            else:
                maxW += min(maxL,maxR) - height[r]
                r -= 1


        return maxW




            
