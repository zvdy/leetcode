class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) < 3:
            return len(fruits)
        max_fruits = 0
        start = 0
        end = 0
        fruit_count = {}
        while end < len(fruits):
            fruit_count[fruits[end]] = fruit_count.get(fruits[end], 0) + 1
            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]
                start += 1
            max_fruits = max(max_fruits, end - start + 1)
            end += 1
        return max_fruits