def rotate_matrix(matrix):
    """
    Rotates the given square matrix 90 degrees clockwise in place.

    Args:
        matrix: the 2D square matrix to rotate
    """
    n = len(matrix)
    #first we transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # then we reverse each row 
    for i in range(n):
        left, right = 0, n - 1
        while left < right:
            matrix[i][left],matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
    
    return matrix
   


def print_matrix(matrix):
    """
    Helper function to print a 2D matrix.

    Args:
        matrix: the matrix to print
    """
    for row in matrix:
        print(' '.join(str(value) for value in row))


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    print_matrix(matrix)
    rotate_matrix(matrix)
    print("Matrix after 90-degree clockwise rotation:")
    print_matrix(matrix)

    # Expected output:
    # Original Matrix:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # Matrix after 90-degree clockwise rotation:
    # 7 4 1
    # 8 5 2
    # 9 6 3
    
    
    #[0,0] -> [0,2]
    #[0,1] -> [1,2]
    #[0,2] -> [2,2]
    #[1,0] -> [0,1]
    #[1,1] -> [1,1]
    #[1,2] -> [2,1]
    #[2,0] -> [0,0]
    #[2,1] -> [1,0]
    #[2,2] -> [2,0]