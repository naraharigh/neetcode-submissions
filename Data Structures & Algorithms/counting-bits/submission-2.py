class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        def dfs(i,count) :
            if i == 0:
                result.append(count)
                count = 0
                return
            if i%2 == 1 :
                count += 1
            dfs(i//2,count)   

        i = 0      
        for i in range(n+1) :
            dfs(i,0) 
            # result.append(count)
        return result            
