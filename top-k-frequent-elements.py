class Solution:
    def topKFrequent(self):
        nums = [1,2,1,2,1,2,3,1,3,2]
        k = 2
        freqencyList = {}

        for num in nums:
            if not freqencyList.get(num,''):
                freqencyList[num] = 0
            # freqencyList[num] = freqencyList.get(num,0) + 1
            freqencyList[num]+=1

        return sorted(freqencyList, key=freqencyList.get, reverse=True)[:k]


        print(result)
        # return list(sorted_by_keys_desc)[:k]

solution = Solution()
solution.topKFrequent()
        