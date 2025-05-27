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
     
    
    """ method 1
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
    """
    # Method 2  O(log n)
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2 # Find the Middle index
        if nums[mid] == target: #Target Found
            return mid
        elif nums[mid] < target: # Target is on the right side
            left = mid + 1
        else: # Target is on the left side
            right = mid - 1
        
    #if the target is not found, left is the correct insertion index
    return left
  
            
    

    
    
     


if __name__ == "__main__":
    print("Search Insert Position")
    nums = [1, 3, 5, 6]
    target = 2
    print(searchInsert(nums, target))