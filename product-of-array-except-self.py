class Solution:
    def productExceptSelf(self):
        nums = [-1,1,0,-3,3]
        productList = {}
        preFix = 1
        for index,value in enumerate(nums):
            productList[index] = preFix
            preFix = preFix * value 
        
        postFix = 1
        for index in range(len(nums) - 1, -1, -1):
            productList[index] *= postFix
            postFix = postFix * nums[index]

        return list(productList.values())

solution = Solution()
print(solution.productExceptSelf())
        