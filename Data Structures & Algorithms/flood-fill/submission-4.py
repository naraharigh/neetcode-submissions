class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        orig = image[sr][sc]
        if orig == color:
            return image
        r,c = len(image),len(image[0])


        def dfc(i,j):
           
            if  i >= r or i < 0 or j <0 or  j >= c or image[i][j] != orig:
                return
            print(i,j)
            image[i][j] = color
            dfc(i+1, j)
            dfc(i-1,j)  
            dfc(i,j+1)
            dfc(i, j-1) 
        dfc(sr,sc)
        return image


        