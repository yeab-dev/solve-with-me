from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        my_idx = 1
        bobs_idx = len(piles) - 1
        my_coins = 0
        while my_idx < bobs_idx:
            my_coins += piles[my_idx]
            my_idx += 2
            bobs_idx -= 1
        return my_coins
