def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    length = 0
    lengths = []
    prev = 0
    for a in A:
        if a < prev:
            lengths.append(length)
            length = 1
        else:
            length += 1
        prev = a
    lengths.append(length)
    
    return lengths.count(max(lengths))
