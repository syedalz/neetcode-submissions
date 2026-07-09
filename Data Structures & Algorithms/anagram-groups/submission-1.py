class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        count = defaultdict(list)

        for i in range(len(strs)):

            countList = [0] * 26

            for c in strs[i]:

                countList[ord(c.lower()) - ord('a')] +=1
            
            count[tuple(countList)].append(strs[i])


        
        return list(count.values())



        