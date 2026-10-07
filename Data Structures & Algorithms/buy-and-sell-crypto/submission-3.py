class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #i have to find the best diference from the start
        # 1- first solution would beto iterate and get every diference and get the maximum
        # 2- i would check from left, using two pointers 

        lower = 0
        higher = 1
        max_profit = 0
        while higher < len(prices):
            if prices[lower] < prices[higher]:
                current_profit = prices[higher] - prices[lower]
                if current_profit > max_profit:
                    max_profit = current_profit
            else:
                lower = higher
            higher += 1
        return max_profit
