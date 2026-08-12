class Solution():
	def twoSum(self):
		nums = [2,7,11,15]
		target = 9
		hashList = {}

		for index, value in enumerate(nums):
			reminder = target - value
			if reminder in hashList:
				return [hashList[reminder],index]
			else:
				hashList[value] = index

obj = Solution()
print(obj.twoSum())