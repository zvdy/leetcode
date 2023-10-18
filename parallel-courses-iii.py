from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # create a graph using a list of lists
        graph = [[] for _ in range(n)]
        # populate the graph with the given relations
        for prev, next in relations:
            graph[prev - 1].append(next - 1)
        # create a memoization list to store the minimum time to complete each course
        memo = [-1] * n
        # define a recursive function to calculate the minimum time to complete a course
        def calculateTime(course):
            # if the minimum time for this course has already been calculated, return it
            if memo[course] != -1:
                return memo[course]
            # if this course has no prerequisites, the minimum time is the time to complete this course
            if not graph[course]:
                memo[course] = time[course]
                return memo[course]
            # otherwise, calculate the minimum time to complete all prerequisites
            max_prerequisite_time = 0
            for prereq in graph[course]:
                max_prerequisite_time = max(max_prerequisite_time, calculateTime(prereq))
            # the minimum time to complete this course is the maximum time to complete all prerequisites plus the time to complete this course
            memo[course] = max_prerequisite_time + time[course]
            return memo[course]
        # calculate the minimum time to complete all courses
        overall_min_time = 0
        for course in range(n):
            overall_min_time = max(overall_min_time, calculateTime(course))
        # return the overall minimum time
        return overall_min_time