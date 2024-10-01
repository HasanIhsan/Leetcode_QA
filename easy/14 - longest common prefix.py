# write a function to find the longest common prefix string amongst an array of strings

#* if there is no prefix return an empty string

#Example 1:
#Input: strs = ["flower","flow","flight"]
#Output: "fl"

#Example 2:
#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.


# NOTE: After a few hours i gave up and looked up a video
# this video really helped me out: https://www.youtube.com/watch?v=0sWShKIJoo4 (after watch through his video i basically understood the problem better but also just copied his code...)

def longestCommonPrefix(strs):
    #print(strs)
    prefix = ""
     
    
    #* iterate throught the first string
    for i in range(len(strs[0])):
        #* now we want to make sure all the string have the exact same character at index as i
        for s in strs:
            #* check the first string in the input and go to that string index of i
            if i == len(s) or s[i] != strs[0][i]:
                return prefix
        #* add the character that is common among those strings to the result
        prefix += strs[0][i]
 
        
    
    return prefix


if __name__ == "__main__":
    print("longest Common Prefix")
    strs = ["flower", "flow", "flight"]
    print(longestCommonPrefix(strs))