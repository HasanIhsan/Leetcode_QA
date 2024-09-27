#Given an interger x, return rtuen if x is a palindome, and false otherwuse

#* Example 1

#* input = 121
#* output: true


def isPalindrome(num):
    ONum = num
    Rnum = 0
    
    #* return false immeadly for negativs, cause a negaive number will never be a plindrome on the account of the face
    #* that if the number is reverces aka say user enter -121 the output if accounting for plaindrome would be 121-
    if num < 0:
        return False
        
    #* reverse the number
    while num != 0:
        digit = num % 10
        Rnum = Rnum * 10 + digit
        num //= 10
    
    print("Original Number: ", ONum)
    print("Reverce Number: ", Rnum)
    

    
    #* check if reversed number is the same as original number
    if ONum == Rnum:
        return True
    else:
        return False
    
    
if __name__ == "__main__":
    print("is number a palindrome")
    num = input("Enter a number: ")
    print(isPalindrome(int(num)))