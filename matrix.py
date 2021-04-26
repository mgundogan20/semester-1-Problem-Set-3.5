def determinant(matrix):
    '''
    Calculate the determinant of a given matrix

    matrix (list of lists): a matrix in the form of a list of lists. the element in the i'th row and j'th column is accesible by matrix[i][j] (indexing is 0 based)  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: determinant of the matrix

    Example:
    >>> determinant([[2,3,1],[-4,5,2], [2,1,-4]])
    -94

    '''
    # print("--------------start--------------")
    
    # print(matrix)
    
    determ = 0
    
    if len(matrix) == 1:
        determ = matrix[0][0]
        # print(determ)
    else:
        for index, row in enumerate(matrix):
            # print("(index,row) = " + str((index,row,)))
            submat = [rowSlice[1:] for rowSlice in matrix if matrix.index(rowSlice) != index]
            
            # print("\nsubmat:")
            # for rows in submat:
            #     print("[" + ",".join(map(str, rows)) + "]")

            increment = row[0]*determinant(submat)*pow(-1,index)
            # print(increment)
            determ += increment
    # print("**************stop**************")
    return determ