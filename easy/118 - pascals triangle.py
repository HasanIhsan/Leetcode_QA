#Given an integer numRows, return the first numRows of Pascal's triangle.

#In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


def generate(numsRows):
    # initialaze the triagina
    triangle = []
    
    for i in range(numRows):
        #start each row with 1
        row = [1] * (i + 1)
        
        
        # compute the values between the 1's (if any)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
        # add the row to the triagnle
        triangle.append(row)
        
    return triangle
    

    
if __name__ == "__main__":
    print("remove duplicates!")
    numRows = 5
    print(generate(numRows))
    
    