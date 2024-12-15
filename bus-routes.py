from typing import *
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        # if source and target are the same, we don't need to take any buses
        if source == target:
            return 0

        # find the maximum stop number in all the routes
        max_stop = max(max(route) for route in routes)
        # if the target is greater than the maximum stop number, it is not reachable
        if max_stop < target:
            return -1

        # initialize an array to keep track of the minimum number of buses to reach each stop
        n = len(routes)
        min_buses_to_reach = [float('inf')] * (max_stop + 1)
        min_buses_to_reach[source] = 0

        # iterate until we have found the minimum number of buses to reach all stops
        flag = True
        while flag:
            flag = False
            for route in routes:
                # find the minimum number of buses to reach any stop on the current route
                mini = float('inf')
                for stop in route:
                    mini = min(mini, min_buses_to_reach[stop])
                # add 1 to the minimum number of buses to reach any stop on the current route
                mini += 1
                # update the minimum number of buses to reach each stop on the current route
                for stop in route:
                    if min_buses_to_reach[stop] > mini:
                        min_buses_to_reach[stop] = mini
                        flag = True

        # return the minimum number of buses to reach the target stop
        return min_buses_to_reach[target] if min_buses_to_reach[target] < float('inf') else -1