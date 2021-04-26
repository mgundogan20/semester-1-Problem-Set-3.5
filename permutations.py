def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # print("-----------start--------------------------")
    # print(sequence)
    
    
    mylist = []
    if len(sequence) == 1:
        mylist = [sequence]
    else:
        for element in get_permutations(sequence[1:]):
            # print("func " + str(sequence[1:]))
            for position in range(len(element)+1):
                # print(element, position, sequence)
                newPerm = element[:position] + sequence[0] + element[position:]
                mylist.append(newPerm)
    
    # print("-----------stop--------------------------")
    return mylist



