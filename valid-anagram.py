class Solution(object):
    def isAnagram(self):
        s = "anagram"
        t = "nagaram"
        charCountS = {}
        
        if len(s) != len(t):
            return False
        
        for charS in s:
            charCountS[charS] = charCountS.get(charS, 0) + 1
            
        for charT in t:
            if not charCountS.get(charT, ''):
                return False
            charCountS[charT] = charCountS.get(charT, 0) - 1

        return True

solution = Solution()
print(solution.isAnagram())