class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        reshape = []

        m = len(mat)
        n = len(mat[0])

        if m * n != r * c :
            return mat

        arr = []

        for mat_item in mat:
            arr.extend(mat_item)

        for i in range(0, len(arr), c):
            reshape.append(arr[i:i + c])
        
        return reshape