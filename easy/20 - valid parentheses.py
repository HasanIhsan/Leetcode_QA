#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#! An input string is valid if:

#! Open brackets must be closed by the same type of brackets.
#! Open brackets must be closed in the correct order.
#! Every close bracket has a corresponding open bracket of the same type.

# https://www.youtube.com/watch?v=WTzjTskDFMg
def isValid(s: str) -> bool:
    #* Stack to keep track of opening brackets
    stack = []
    
    #* Dictionary to hold the matching pairs of brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    #* Traverse each character in the string
    for char in s:
        #* If it's a closing bracket
        if char in bracket_map:
            #* Pop the top element from stack if it's not empty; otherwise, use a dummy value
            top_element = stack.pop() if stack else '#'
            
            #* Check if the popped element is the matching opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            #* If it's an opening bracket, push it to the stack
            stack.append(char)
    
    #* Return True if the brackets match 
    return True
    
    
if __name__ == "__main__":
    print("is valid parentheses")
    
    s = "())"
    print(isValid(s))