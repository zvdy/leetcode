class Solution:
    def totalMoney(self, n: int) -> int:
        # The number of weeks
        weeks = n//7
        # The number of days after the last week
        days = n%7
        # The total amount of money
        return 28*weeks + 7*weeks*(weeks-1)//2 + weeks*days + days*(days+1)//2
