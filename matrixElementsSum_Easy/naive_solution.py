def matrixElementSum(matrix):
    # What do we need to do?
    # We can create a list of indices to check,
    # Then when an index is checked, if its value is 0,
    # that index is added to a blocked filter
    '''
    Example input:
    [[1,0,3],
     [0,2,1],
     [1,2,0]]
    '''
    # indices = list(range(0, len(matrix[0])))  <- this still works for 1-col matrices
    # then we check the indices are not blocked
    # if there is a 0, we add that index to the blocked list.
    rooms = []
    indices = list(range(0, len(matrix[0])))
    blocked = []
    for row in matrix:
        for ii in indices:
            if row[ii] == 0:
                blocked.append(ii)
            elif ii not in blocked:
                rooms.append(row[ii])
    return sum(rooms)
