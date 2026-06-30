class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        def dfs(n,count) :
            if n == 0:
                result.append(count)
                count = 0
                return
            if (n%2) == 1 :
                count = count +1
            dfs(n//2,count)

        for num in range(0,n+1):
            dfs(num,0)    

        return result