class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for k in range(min(len(mat), len(mat[0]))-1):
            for i in range(len(mat)-1):
                for j in range(len(mat[0])-1):
                    if mat[i][j] > mat[i+1][j+1]:
                        temp = mat[i][j]
                        mat[i][j] = mat[i+1][j+1]
                        mat[i+1][j+1] = temp
        return mat