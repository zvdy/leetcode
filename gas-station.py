from typing import *
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 1. If the sum of gas is less than the sum of cost, then there is no solution
        if sum(gas) < sum(cost):
            return -1
        # 2. If the sum of gas is greater than the sum of cost, then there is a solution
        # 2.1. Start from the first gas station
        start = 0
        # 2.2. Initialize the tank with the gas at the first gas station
        tank = gas[0]
        # 2.3. Initialize the cost to get to the next gas station
        cost_to_next = cost[0]
        # 2.4. Start from the second gas station
        i = 1
        # 2.5. While we have not visited all gas stations
        while i < len(gas):
            # 2.5.1. If the tank has enough gas to get to the next gas station
            if tank >= cost_to_next:
                tank = tank - cost_to_next + gas[i]
                cost_to_next = cost[i]
            # 2.5.2. If the tank does not have enough gas to get to the next gas station
            else:
                start = i
                tank = gas[i]
                cost_to_next = cost[i]
            # 2.5.3. Go to the next gas station
            i += 1
        # 3. Return the start
        return start
