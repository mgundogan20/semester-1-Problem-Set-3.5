def print_paths(grid):
    '''
    Print all of the paths starting from the top-left cell and ending in the bottom-right cell such that the path is strictly increasing.

    grid (list of lists): The grid that we are moving on. It is a matrix in the form of list of lists. the element in the i'th row and j'th column is accesible by grid[i][j] (indexing is 0 based)

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Example:
    >>> print_paths([[1,4,3],[5,6,7]])
    [1, 4, 6, 7]
    [1, 5, 6, 7]

    Note: depending on your implementation, you may print the permutations in
    a different order than what is listed here.
    You must not return anything. You should only print the paths.
    '''
    current_paths = [[0,0,grid[0][0]]]
    for element in possible_steps(grid, current_paths):
        print(element[2:])
    
    pass #delete this line and replace with your code here

def possible_steps(grid, current_paths):
    '''
    input format:
    grid (list of lists): it is of the form grid[row][column].
    current_path (list of integers): first two elements are the coordinates of the last cell the rest is an ordered list of steps taken so far.
    Example:
    [i,j,1,2,3,4]

    output format:
    returns all possible paths, strictly increasing that is, as a list of lists; each sublist being a possible "path" starting from the initial cell of the grid. Notice it does not complete the route for the whole grid but merely increments one step at a time.
    Example:
    [[i+1,j,1,2,3,4,5],
     [i,j+1,1,2,3,4,6]
    ]
    '''
    possible_paths = []
    # find all possible steps for all current paths
    # update current paths accordingly and store them in possible_paths
    for current_path in current_paths:
        if current_path[-1] != grid[-1][-1]:
            steps = []
            directions = [[1,0],
                        [0,1],
                        [-1,0],
                        [0,-1]]

            "------determines the coordinates of the current cell --------"
            i = current_path[0]
            j = current_path[1]

            "------checks each direction for possible steps------"
            for element in directions:
                I = i + element[0]
                J = j + element[1]
                if I < 0 or I >= len(grid):
                    continue
                elif J < 0 or J >= len(grid[0]):
                    continue
                else:
                    target = grid[I][J]
                "----updates the final coordinates and adds the complete path to that location to possible_paths----"
                if target > grid[i][j]:
                    possible_path = [I,J] + current_path[2:] + [target]
                    steps.append(possible_path)
            # print("steps:",steps)
            possible_paths.extend(steps)
        else:
            possible_paths.append(current_path)

    #if none changed return current_paths
    if current_paths == possible_paths:
        # print("current_paths",current_paths)
        return current_paths
    #if not use recursion on the possible paths
    else:
        return possible_steps(grid, possible_paths)



myGrid = [[1,4,3],
        [5,6,7]]
# current_path = [1,3,6,8]

print_paths(myGrid)

