class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == '+':
                record.append(record[-1] + record[-2])
            elif op == 'D':
                record.append(2 * record[-1])
            elif op == 'C':
                record.pop()
            else:
                record.append(int(op))
        return sum(record)

        # operations_types = ['+', 'D', 'C']
        # for operation in operations:
        #     if operation not in operations_types:
        #         record.append(operation)
        #     else:
        #         if operation == '+':
        #             record.append(record[-1] + record[-2])
        #         elif operation == 'D':
        #             record.append(record[-1] * 2)
        #         elif operation == 'C':
        #             record.remove(record[-1])
    
        # counter = 0
        # for i in record:
        #     i = int(i)
        #     counter += i
        # return counter


