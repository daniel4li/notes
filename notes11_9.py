# quick sort

# can sort a list by subdividing it based on a PIVOT value 
    # place elements < pivot to the left side
    # place elements > pivot to the right side
    # recurse for each left/ right portion
    # when sub list sizes == 1, the entire list is sorted 
# how do we partition the list into left/ right sub lists?
    # choose pivot (since elements are random, choose 1st element [0])
    # find an element in the left side (using leftmark index starting at the beginning of the list just past pivot moving right)
    # find element on right thats out of place
    # swap out of place elemnt with each other
        # put them in correct side throughout the entire thing 