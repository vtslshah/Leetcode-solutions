class Solution:
	def lengthOfLongestSubstring(self):
		s = "abcbcabb"
		
		seen = {}
		left = 0
		maxLenght = 0

		for right in range(len(s)):
			if s[right] in seen:
				left = max(left, seen[right] + 1)
			seen[s[right]] = right
			maxLenght = max(maxLenght, right - left + 1)

		print(maxLenght)



	
obj = Solution()
obj.lengthOfLongestSubstring()