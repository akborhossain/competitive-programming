class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        self.dfs(image,sr,sc,color,image[sr][sc])
        return image
        

    def dfs(self, image: List[List[int]], r: int, c: int, color: int, oldcolor: int):
        if r<0 or c<0 or r>=len(image) or c>=len(image[0]) or image[r][c]!=oldcolor:
            return
        image[r][c]=color
        self.dfs(image,r+1,c,color,oldcolor)
        self.dfs(image,r-1,c,color,oldcolor)
        self.dfs(image,r,c+1,color,oldcolor)
        self.dfs( image,r,c-1,color,oldcolor)