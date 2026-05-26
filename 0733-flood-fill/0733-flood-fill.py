class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        origin_color = image[sr][sc]

        def DFS(r, c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            
            if image[r][c] != origin_color or image[r][c] == color:
                return
            
            image[r][c] = color

            DFS(r+1, c)
            DFS(r-1, c)
            DFS(r, c+1)
            DFS(r, c-1)
        
        DFS(sr, sc)

        return image