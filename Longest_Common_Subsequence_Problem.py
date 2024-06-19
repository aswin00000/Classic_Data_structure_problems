# X: ABCBDAB
# Y: BDCABA 
# The length of the LCS is 4
# LCS are BDAB, BCAB, and BCBA


# Function to find the length of the longest common subsequence of substring
# `X[0…m-1]` and `Y[0…n-1]`
def LCSLength(X, Y, m, n, lookup):
 
    # return if the end of either string is reached
    if m == 0 or n == 0:
        return 0
 
    # construct a unique key from dynamic elements of the input
    key = (m, n)
 
    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:
 
        # if the last character of `X` and `Y` matches
        if X[m - 1] == Y[n - 1]:
            lookup[key] = LCSLength(X, Y, m - 1, n - 1, lookup) + 1
 
        else:
            # otherwise, if the last character of `X` and `Y` don't match
            lookup[key] = max(LCSLength(X, Y, m, n - 1, lookup),
                            LCSLength(X, Y, m - 1, n, lookup))
 
    # return the subproblem solution from the dictionary
    return lookup[key]
 
 
if __name__ == '__main__':
 
    X = 'ABCBDAB'
    Y = 'BDCABA'
 
    # create a dictionary to store solutions to subproblems
    lookup = {}
 
    print('The length of the LCS is', LCSLength(X, Y, len(X), len(Y), lookup))
 
