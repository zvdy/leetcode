class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(s1, s2):
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        def dfs(s, visited):
            visited.add(s)
            for nei in graph[s]:
                if nei not in visited:
                    dfs(nei, visited)

        graph = defaultdict(list)
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if is_similar(strs[i], strs[j]):
                    graph[strs[i]].append(strs[j])
                    graph[strs[j]].append(strs[i])

        visited = set()
        ans = 0
        for s in strs:
            if s not in visited:
                dfs(s, visited)
                ans += 1
        return ans