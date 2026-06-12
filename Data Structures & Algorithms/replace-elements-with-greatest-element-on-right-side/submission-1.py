class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
       # initial max=1

        rMax=-1

        for i in range(len(arr)-1,-1,-1 ):
            nMax = max(arr[i], rMax)
            arr[i] = rMax
            rMax=nMax

        return arr 


      
