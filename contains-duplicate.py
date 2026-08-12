class Solution:
    def containsDuplicate(self) -> bool:
        nums = [1,2,3,1]
        duplicates = {}

        for num in nums:
            print(num)
            if not duplicates.get(num,''):
                duplicates[num] = 1
            else:
                return True
        return False


solution = Solution()
solution.containsDuplicate()