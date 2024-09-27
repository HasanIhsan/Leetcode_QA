#Given an interger x, return rtuen if x is a palindome, and false otherwuse

#* Example 1

#* input = 121
#* output: true


def isPalindrome(num):
    ONum = num
    Rnum = 0
    
    while num != 0:
        digit = num % 10
        Rnum = Rnum * 10 + digit
        num //= 10
    
    print("Original Number: ", ONum)
    print("Reverce Number: ", Rnum)
    if ONum == Rnum:
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    print("is number a palindrome")
    num = input("Enter a number: ")
    print(isPalindrome(int(num)))