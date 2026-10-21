class Solution:
	def min_stops(self):
		capacity = 100 
		initial_fuel_percent= 50 
		destination= 200
		pumps = [50,80,100,130,140]
		current = 0
		stops = 0
		i = 0

		# Convert initial fuel % into initial range
		current_range = capacity * initial_fuel_percent / 100
		print(current_range)

		while current + current_range < destination:
			# print(current)
			farthest = current

			# Find the farthest pump we can currently reach
			while i < len(pumps) and pumps[i] <= current + current_range:
				# print(pumps[i])
				farthest = pumps[i]
				i += 1

			print(farthest, current)
			# Cannot reach another pump
			if farthest == current:
				return -1

			current = farthest
			current_range = capacity
			stops += 1

		print(stops)


obj = Solution()
obj.min_stops()