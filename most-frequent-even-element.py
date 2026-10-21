class Solution:
    def mostFrequentEven(self):
        nums = [8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]
        mostFreq = {}
        for num in nums:
            if not mostFreq.get(num,'') and (num % 2 == 0):
                mostFreq[num] = 0
            if num % 2 == 0:
                mostFreq[num] += 1
        sortedList = sorted(mostFreq.items(),key=lambda item: item[1],reverse=True)
        max_frequency = 0
        answer = -1
        for num,count in sortedList:
            if count > max_frequency:
                max_frequency = count
                answer = num
            elif count == max_frequency:
                answer = min(answer,num)

        print(answer)

solution = Solution()
solution.mostFrequentEven()