# Given an array of integers sorted in ascending order aAd a target value, return the index~s 
# of any pair of numbers in the array that sum to the tar-get. The order of the indexes In the 
# result doesn't matter. If no pair is found, return an empty array. 
# E>cample 1: 
# I 
# ! Input nums e ( -5, -2, 3, 4, 6]., target = 7 
# Output t2, 3) 
# Explanation: nums[2] + nums[3] = 3 + 4 = 7 
# Example 2: 
# Input nums = [1, 1, 1], target = 2 
# Output: (0, 1J 
# Explanation: c:>ther valid outputs could be [ 1, 0] • [ e., 2] , [ 2, 0] , [ 1, 2] or 
# I [2, 11 ]. 


def pair_sum_sorted(nums : list[int], target : int) -> list[int] :
    first, last = 0 , len(nums)-1
    
    while last > first:
        sum = nums[first] + nums[last]
        if sum > target :
            last -=1
        elif sum < target:
            first +=1
        else :
            return [first,last]
    return []


print(pair_sum_sorted([ -5, -2, 3, 4, 6] , 7))