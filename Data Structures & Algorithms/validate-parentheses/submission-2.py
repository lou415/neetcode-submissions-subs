class Solution:
    def isValid(self, s: str) -> bool:
        # initialize our Python dynamic array that implements the 
        # Stack ADT. 
        stack = []
        # initialize our hashmap
        hashmap = {')':'(','}':'{',']':'['}

        # iterate through the string
        for char in s:
            # check to see if it's a closing string
            if char in hashmap:
                # if it is a closing string, see if it has its open string counterpart
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
    

        