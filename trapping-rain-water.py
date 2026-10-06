class Solution:
	def trap(self):
		height = [0,1,0,2,1,0,1,3,2,1,2,1]

		leftP = 0
		rightP = len(height) -1

		maxLeft = 0
		maxRight = 0
		totalTrapWater = 0

		while(leftP < rightP):
			maxLeft = max(maxLeft,height[leftP])
			maxRight = max(maxRight, height[rightP])

			if(maxLeft < maxRight):
				totalTrapWater += (maxLeft - height[leftP])
				leftP += 1
			else:
				totalTrapWater += (maxRight - height[rightP])
				rightP -= 1

		return totalTrapWater

obj = Solution()
print(obj.trap())