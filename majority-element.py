class Solution:
    def majorityElement(self):
        nums = [3,3,4]
        majorityEle = {}
        for num in nums:
            if not majorityEle.get(num,''):
                majorityEle[num] = 0
            
            majorityEle[num] += 1
        print(majorityEle)
        return sorted(majorityEle, key=majorityEle.get,reverse=True)[0]

obj = Solution()
print(obj.majorityElement())