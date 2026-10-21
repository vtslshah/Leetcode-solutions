# class Solution:
# 	def twoSum(self):
# 		numbers = [2,7,11,15]
# 		target = 9
# 		hashList = {}
# 		for index, value in enumerate(numbers):
# 			reminder = target - value
# 			if reminder in hashList:
# 				return [hashList[reminder],index + 1]
# 			else:
# 				hashList[value] = index + 1

# obj = Solution()
# print(obj.twoSum())

class Solution:
	def twoSum(self):
		numbers = [2,7,11,15]
		target = 9
		
		left = 0
		right = len(numbers) - 1
		while left < right:
			currentSum = numbers[left] + numbers[right]
			if currentSum > target:
				right -= 1
			elif currentSum < target:
				left += 1
			else:
				return [left + 1, right + 1]
		return []

obj = Solution()
print(obj.twoSum())