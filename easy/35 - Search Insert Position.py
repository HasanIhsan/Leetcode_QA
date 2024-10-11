#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#NOTE: You must write an algorithm with O(log n) runtime complexity. (......... no)

 

#Example 1:
#Input: nums = [1,3,5,6], target = 5
#Output: 2

#Example 2:
#Input: nums = [1,3,5,6], target = 2
#Output: 1

#Example 3:
#Input: nums = [1,3,5,6], target = 7
#Output: 4

def searchInsert(nums, target):
    index = 0
    
    # Method 1: (this is complicated and what i first thought of) O(n + n + n log n + n) = O(n log n)
    temp = nums
    # Iterate through the array
    for i in range(len(nums)):
        # If the target exits in the array
        if nums[i] == target:
            # Set index to the i and return it
            index = i
            return index
        else:
            # If target is not in array add it to a temp array
            temp.append(target)
            #print(temp)
            
            # Sort that temp array
            temp.sort()
            
            #search that array and return the index
            for x in range(len(temp)):
                if temp[x] == target:
                    index = x
                    return index
            
    
            
    
    return index


if __name__ == "__main__":
    print("Search Insert Position")
    nums = [1, 3, 5, 6]
    target = 2
    print(searchInsert(nums, target))