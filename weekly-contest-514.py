class Solution:
    def minPrice(self) -> float:
        prices = [10,30,21]
        discounts = [50,60]

        sorted_prices = sorted(prices,reverse=True)
        sorted_discounts = sorted(discounts,reverse=True)

        for index,price in enumerate(sorted_prices):
            discount = sorted_discounts[index] if index < len(sorted_discounts) and sorted_discounts[index] is not None else 0
            if(discount > 0):
                sorted_prices[index] = price * ((100 - discount)) / 100
            else:
                sorted_prices[index] = price

        return sum(sorted_prices)
            


obj = Solution()
obj.minPrice()