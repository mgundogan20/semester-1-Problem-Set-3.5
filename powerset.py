def generate_powerset(input_set):
    '''
    Enumerate all subsets of a given string

    input_set (list): an arbitrary list. Assume that it does not contain any duplicate elements.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of lists containing all the subsets of input_set

    Example:
    >>> generate_powerset([1, 2, 3])
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

    Note: depending on your implementation, you may return the susbsets in
    a different order than what is listed here.
    '''
    # print("--------------start--------------")
    # print("input set:", input_set)
    powerset = []
    if len(input_set) == 0:
        powerset = [[]]
    else:
        extension = []
        for subset in generate_powerset(input_set[1:]):
            powerset.append(subset[:])
            subset.append(input_set[0])
            extension.append(subset[:])
        powerset.extend(extension)
    # print("-----------",powerset,"-----------")
    return powerset

# print(len(generate_powerset([1,2,3,4,5,6,7,8])))
