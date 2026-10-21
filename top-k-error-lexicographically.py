from collections import Counter

class Solution:
	def topKError(self):
		logs = [
			"2026-03-20 10:00:00 ERROR Database connection failed",
			"2026-03-20 10:01:00 INFO User logged in",
			"2026-03-20 10:02:00 ERROR Database connection failed",
			"2026-03-20 10:03:00 ERROR Timeout while calling API",
			"2026-03-20 10:04:00 ERROR Database connection failed",
		]
		errors = []
		for log in logs:
			parts = log.split(" ", 3)
			if len(parts) == 4 and parts[2] == 'ERROR':
				errors.append(parts[3])
		frequency = Counter(errors)
		result = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
		print(result)
			

obj = Solution()
obj.topKError()




# Write Python code to return the top K most frequent ERROR messages, sorted by:
# Frequency (descending)
# Lexicographically (for tie-breaking)