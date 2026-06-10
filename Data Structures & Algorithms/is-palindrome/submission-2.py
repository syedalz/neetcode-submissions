class Solution:
    def isPalindrome(self, s: str) -> bool:

        import string;
        
        clean_s = "".join(char for char in s if char.isalnum())

        for i in range(len(clean_s)):

            if clean_s[i].lower() == clean_s[len(clean_s)-i-1].lower():

                continue
            else:
                return False
        
        return True

        

        