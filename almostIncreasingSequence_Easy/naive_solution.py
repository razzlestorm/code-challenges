def almostIncreasingSequence(sequence):
    # iterate over sequence
    # check if each item is bigger than previous and smaller than next, if it isn't, remove it.
    ## keep track of previous and next
    ## keep track of how many times we remove an item from sequence (more than 1 and the next time it happens, we break and return false)
    delete_counter = 0
    ii = 1
    while delete_counter < 2 and ii < len(sequence):
        # Sequence length guaranteed to be at least 2
        curr = sequence[ii]
        # We've run through the entire thing
        if ii == len(sequence):
            return True

        # Edge case of 2
        if len(sequence) == 2:
            if sequence[0] <= sequence[ii]:
                return True
            return False
        try:
            '''
            # These are essentially our possible conditions
            prev < curr < next = Fine!  ~
            10, 20, 30
            prev < curr > next = remove curr ~
            10, 30, 20
            prev > curr < next = remove curr ~
            20, 10, 30
            prev < curr > next = remove next ~
            20, 30, 10
            prev > cur > next = False ~
            30, 20, 10
            prev > cur < next = remove prev
            30, 10, 20
            '''
            prev = sequence[ii-1]
            next = sequence[ii+1]
            # Any time we pop, we should re-check (so don't increment ii)
            if prev > curr > next:
                return False
            if prev == curr == next:
                return False
            # We also need to do a few checks between prev and next
            if (prev <= curr >= next) and (prev < next):
                sequence.pop(ii)
                delete_counter += 1
                continue
            if (prev <= curr >= next) and (prev >= next):
                sequence.pop(ii+1)
                delete_counter += 1
                continue
            if prev >= curr < next:
                sequence.pop(ii-1)
                delete_counter += 1
                continue
            if prev < curr >= next:
                sequence.pop(ii+1)
                delete_counter += 1
                continue
            if prev < curr < next:
                ii += 1


        # have also reached end of list without error
        except IndexError:
            # since we've reached the end, we don't need to actually pop anything
            prev = sequence[ii-1]
            if prev < curr:
                return True
            # We increase counter for deleting, and if it goes above 1, it will return false
            delete_counter += 1
            ii += 1

    return False
