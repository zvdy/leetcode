class Solution:
    def minInsertions(self, s: str) -> int:

        rev_str=s[::-1]
        n=len(s)

        t=[[0]*(n+1) for i in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==rev_str[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
            

        # def dp(rev_str,s,i,j,n):
        #     if i>=n or j>=n:
        #         return 0
        #     if rev_str[i]==s[j]:
        #         return 1 + dp(rev_str,s,i+1,j+1,n) 
        #     return max( dp(rev_str,s,i+1,j,n) , dp(rev_str,s,i,j+1,n) )





        k=t[n][n]

        return len(s)-k