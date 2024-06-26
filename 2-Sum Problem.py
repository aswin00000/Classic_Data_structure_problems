# Input: nums = [8, 7, 2, 5, 3, 1]
# target = 10 
# Output: Pair found (8, 2)orPair found (7, 3)  
# Input: nums = [5, 2, 6, 8, 1, 9]
# target = 12 
# Output: Pair not found


# 1. Using Brute-Force

# Naive method to find a pair in a list with the given sum
def findPair(nums, target):
 
    # consider each element except the last
    for i in range(len(nums) - 1):
 
        # start from the i'th element until the last element
        for j in range(i + 1, len(nums)):
 
            # if the desired sum is found, print it
            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return
 
    # No pair with the given sum exists in the list
    print('Pair not found')
 
 
if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)

# 2. Using Sorting

# Function to find a pair in an array with a given sum using sorting
def findPair(nums, target):
 
    # sort the list in ascending order
    nums.sort()
 
    # maintain two indices pointing to endpoints of the list
    (low, high) = (0, len(nums) - 1)
 
    # reduce the search space `nums[low…high]` at each iteration of the loop
 
    # loop till the search space is exhausted
    while low < high:
 
        if nums[low] + nums[high] == target:        # target found
            print('Pair found', (nums[low], nums[high]))
            return
 
        # increment `low` index if the total is less than the desired sum;
        # decrement `high` index if the total is more than the desired sum
        if nums[low] + nums[high] < target:
            low = low + 1
        else:
            high = high - 1
 
    # No pair with the given sum exists
    print('Pair not found')
 
 
if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)

# 3. Using Hashing

# Function to find a pair in an array with a given sum using hashing
def findPair(nums, target):
 
    # create an empty dictionary
    d = {}
 
    # do for each element
    for i, e in enumerate(nums):
 
        # check if pair (e, target - e) exists
 
        # if the difference is seen before, print the pair
        if target - e in d:
            print('Pair found', (nums[d.get(target - e)], nums[i]))
            return
 
        # store index of the current element in the dictionary
        d[e] = i
 
    # No pair with the given sum exists in the list
    print('Pair not found')
 
 
if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)
