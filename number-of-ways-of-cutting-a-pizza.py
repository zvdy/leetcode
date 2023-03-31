class Solution:
    def isValid(self,pizza,startRow,endRow,startCol,endCol):
        for i in range(startRow,endRow+1):
            for j in range(startCol,endCol+1):
                if pizza[i][j]=='A':
                    return True
        return False
    
    def solve(self,pizza,startRow,startCol,cutsLeft,dp):
        if cutsLeft==0:
            return 1
        ans =0
        m=len(pizza)
        n=len(pizza[0])
        if dp[startRow][startCol][cutsLeft]!=-1:
            return dp[startRow][startCol][cutsLeft]

        for row in range(startRow,m):
            upperHalf=self.isValid(pizza,startRow,row,startCol,n-1)
            lowerHalf=self.isValid(pizza,row+1,m-1,startCol,n-1)
            if upperHalf and lowerHalf:
                ans+=self.solve(pizza,row+1,startCol,cutsLeft-1,dp)
        
        for col in range(startCol,n):
            leftHalf=self.isValid(pizza,startRow,m-1,startCol,col)
            rightHalf=self.isValid(pizza,startRow,m-1,col+1,n-1)
            if leftHalf and rightHalf:
                ans+=self.solve(pizza,startRow,col+1,cutsLeft-1,dp)
        dp[startRow][startCol][cutsLeft] = ans
        return dp[startRow][startCol][cutsLeft]
    def ways(self, pizza: List[str], k: int) -> int:
        dp=[[[-1 for i in range(k+1)]for j in range(len(pizza[0])+1)]for x in range(len(pizza)+1)]
        return self.solve(pizza,0,0,k-1,dp)  % (10**9+7)