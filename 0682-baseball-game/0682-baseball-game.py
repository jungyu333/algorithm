class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        records = []

        operator = ["D", "C", "+"]

        for oper in operations:

            if oper not in operator:
                records.append(int(oper))
            
            else:
                if oper == 'C':
                    records.pop()
                
                elif oper == 'D':
                    top = records[-1]
                    records.append(top * 2)
                
                elif oper == '+':
                    previous_sum = sum(records[-2:])
                    records.append(previous_sum)
        
        return sum(records)