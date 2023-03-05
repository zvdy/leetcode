class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        pos = collections.defaultdict(list)
        for i, a in enumerate(arr):
            pos[a].append(i)
        visited = [False] * n
        visited[0] = True
        q = collections.deque([0])
        step = 0
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if i == n - 1:
                    return step
                for j in (i - 1, i + 1):
                    if 0 <= j < n and not visited[j]:
                        visited[j] = True
                        q.append(j)
                for j in pos[arr[i]]:
                    if not visited[j]:
                        visited[j] = True
                        q.append(j)
                pos[arr[i]] = []
            step += 1
        return -1