class Solution:
    def isValid(self, s: str) -> bool:
        # initialize the stack
        stack = []
        # initialize our dict of characters.  
        char_dict = {')':'(', '}':'{', ']':'['}

        # iterate through the string
        for char in s:
            # if the closing tag is not in the hashmap, then 
            # its an open bracket. 
            if char not in char_dict:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != char_dict[char]:
                        return False

        return not stack
    

        