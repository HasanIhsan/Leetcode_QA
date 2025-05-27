#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# #The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

#Increment the large integer by one and return the resulting array of digits.

 

#Example 1:

#Input: digits = [1,2,3]
#Output: [1,2,4]
#Explanation: The array represents the integer 123.
#Incrementing by one gives 123 + 1 = 124.
#Thus, the result should be [1,2,4].

#from my understanding we just have to find the last int in the array and add plus 1

 
def plusOne(arr):
    # Start from the last digit
    for i in range(len(arr) - 1, -1, -1):
        # If the current digit is less than 9, simply increment and return
        if arr[i] < 9:
            arr[i] += 1
            return arr
        # If it's 9, turn it into 0 (carry over will go to the next left digit)
        arr[i] = 0
    
    # If all digits were 9, we will end up here. Add 1 at the beginning
    return [1] + arr
            
            
 


 

if __name__ == "__main__":
    print("Plus one")
    ex1 = [1, 2, 3] # => 1, 2, 4
    ex2 = [4, 3, 2, 1] # => 4, 3, 2, 2
    ex3 = [9] # => 1, 0
    print(plusOne(ex3))