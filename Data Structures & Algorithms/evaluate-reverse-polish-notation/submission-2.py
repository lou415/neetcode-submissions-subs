class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for item in tokens:
            if item not in ['+', '-', '*', '/']:
                result.append(int(item))
            else:
                item1 = result.pop()
                item2 = result.pop()
                
                if item == '+':
                    result.append(item2 + item1)
                elif item == '-':
                    result.append(item2 - item1)
                elif item == '*':
                    result.append(item2 * item1)
                else:
                    result.append(int(item2 / item1))
        return sum(result)

            