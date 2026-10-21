class Solution:
    def isPalindrome(self):
        s = "A man, a plan, a canal: Panama"
        leftP = 0
        rightP = len(s) - 1

        while leftP < rightP:
            while not self.isAlnum(s[leftP]):
                leftP += 1

            while not self.isAlnum(s[rightP]):
                rightP -= 1

            if s[leftP].lower() != s[rightP].lower():
                return False
    
            leftP += 1
            rightP -= 1
        return True

        

    def isAlnum(self,s):
        return ( ord('A') <= ord(s) <= ord('Z') or ord('a') <= ord(s) <= ord('z') or ord('0') <= ord(s) <= ord('9'))
solution = Solution()
print(solution.isPalindrome())