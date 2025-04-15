from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitBasket = {}
        i, j = 0,1
        fruitBasket[fruits[i]] = 1
        count = 1
        maxCount = 1
        while j < len(fruits):
            if fruits[j] in fruitBasket:
                fruitBasket[fruits[j]] += 1
                count += 1
            else:
                if len(fruitBasket) < 2:
                    fruitBasket[fruits[j]] = 1
                    count += 1
                else:
                    maxCount = max(count, maxCount)
                    count -= fruitBasket[fruits[i]]
                    del fruitBasket[fruits[i]]
                    while fruits[i] not in fruitBasket:
                        i += 1
                    fruitBasket[fruits[j]] = 1
                    count += 1
            maxCount = max(count, maxCount)
            j += 1
                    
        return maxCount