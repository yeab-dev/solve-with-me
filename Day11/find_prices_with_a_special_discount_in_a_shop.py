from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = [0] * len(prices)

        for i, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                priceV, priceIdx = stack.pop()
                res[priceIdx] = priceV - price
            stack.append([price, i])
        if stack:
            for num, idx in stack:
                res[idx] = num
        return res

print(Solution().finalPrices([10,1,1,6]))