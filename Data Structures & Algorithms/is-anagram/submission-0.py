class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = sorted(list(s))
        str2 = sorted(list(t))
        if str2 == str1:
            return True
        else:
            return False

        
        