"""
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined
"""


""" my answer: """

def count_sheeps(sheep):
    count = 0
    
    for s in sheep:
        if s == True:
            count +=1
    
    return count

""" another answer: """
def count_sheeps_(sheep):
   return sheep.count(True)  # True is treated as 1 and False as 0 in Python
