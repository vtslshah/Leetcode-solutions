# Travel Planning: You have to travel 200 KM starting from your home, initially you have 50 fuel in your tank, your vehicle fuel capacity is 100 litter, you need to find total minimum stop you need to take to reach the destination.

# when tank is full it running 100 km
# initial fuel 50%
# Destination i have to travel is 200 KM
class Solution:
	def min_stops(self):
		capacity = 100 
		initial_fuel_percent= 50 
		destination= 220
		pumps = [50, 90, 120, 145]

		stops = 0
		current_range = capacity * initial_fuel_percent / 100
		remaining_distance = destination

		for index, pump in enumerate(pumps):

			if (remaining_distance <= 0 or (remaining_distance - current_range) <= 0):
				return stops

			if(pump <= current_range):
				initial_distance_cover = 0
				remaining_distance -= current_range
				current_range = capacity
				stops += 1

obj = Solution()
print(obj.min_stops())