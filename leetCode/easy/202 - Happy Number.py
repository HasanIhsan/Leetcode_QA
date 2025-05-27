#Write an algorithm to determine if a number n is happy.

#A happy number is a number defined by the following process:

#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.
#Return true if n is a happy number, and false if not.

#Input: n = 19
#Output: true
#Explanation:
#1^2 + 9^2 = 82
#8^2 + 2^2 = 68
#6^2 + 8^2 = 100
#1^2 + 0^2 + 0^2 = 1

def isHappy(n):
    
    #calculate the sum of the squares 
    def get_next(num):
        sum = 0
        while num > 0:
            digit = num % 10
            sum += digit ** 2
            num //= 10
        return sum
    
    # track numbers we encounterd if n appears again = num is not happy
    seen = set()
    
    # loop continues until n becomes 1 or n is found in seen
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
        
        if n in seen:
            return False
    
     
    
    # return true if happy
    return True

if __name__ == "__main__":
    print("Happy Number")
    n = 2
    print(isHappy(n))
