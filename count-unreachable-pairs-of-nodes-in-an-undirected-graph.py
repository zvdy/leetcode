class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = {}

        for f, t in edges:
            if f in g:
                g[f].add(t)
            else:
                g[f] = {t}
            
            if t in g:
                g[t].add(f)
            else:
                g[t] = {f}

        ans = 0
    
        visited = [0] * n

        def dfs(g, visited, now, comp):
            visited[now] = comp
            if now in g:
                for neig in g[now]:
                    if not visited[neig]:
                        dfs(g, visited, neig, comp)

        comp = 1
        for i in range(n):
            if not visited[i]:
                dfs(g, visited, i, comp)
                comp += 1

        comps = {}

        
        for i in range(n):
            comps[visited[i]] = comps.get(visited[i], 0) + 1
        
        def findProductSum(a):
            n = len(a)
            array_sum = 0
            for i in range(n):
                array_sum += a[i]

            array_sum_square = array_sum * array_sum
            individual_square_sum = 0
            for i in range(n):
                individual_square_sum += a[i] * a[i]

            return (array_sum_square -
                    individual_square_sum) // 2
        
        return findProductSum(list(comps.values()))
