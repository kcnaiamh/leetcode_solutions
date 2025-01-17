from typing import List
from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = inf
        max_result = 0
        for price in prices:
            min_value = min(min_value, price)
            max_result = max(max_result, price - min_value)

        return max_result