class Solution:
    def isValid(self):
        s = "([])"

        closeToOpen = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        charStack = []
        
        for char in s:
            if char in closeToOpen:
                if charStack and charStack[-1] == closeToOpen[char]:
                    charStack.pop()
                else:
                    return False 
            else:
                charStack.append(char) 

        if not charStack:
            return True
        else:
            return False

solution = Solution()
print(solution.isValid())