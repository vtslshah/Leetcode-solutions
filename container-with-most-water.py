class Solution:
	def maxArea(self):
		height = [1,8,6,2,5,4,8,3,7]
		
		maxWater = 0
		leftP = 0
		rightP = len(height) - 1

		while (leftP < rightP):
			w = rightP - leftP
			hw = min(height[leftP], height[rightP])
			current_capacity = hw * w
			maxWater = max(maxWater, current_capacity)

			if (height[leftP] < height[rightP]):
				leftP += 1
			else: 
				rightP -= 1

		return maxWater
			
obj = Solution()
print(obj.maxArea())