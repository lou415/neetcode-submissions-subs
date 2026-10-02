class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # We can first transpose the matrix, so the rows become columns
        # and the columns become rows.

        # once we have this, we can use create a horizontal reflection to get the rotated matrix.

        # getting the length of the matrix
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # now the horizontal reflection
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]