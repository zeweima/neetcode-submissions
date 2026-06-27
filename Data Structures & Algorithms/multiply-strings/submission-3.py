class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        res = []
        numer_res = 0
        tens = 1
        for digit1 in num1[::-1]:
            tmp_res = 0
            
            for digit2 in num2:
                tmp_res = tmp_res * 10 + int(digit1)*int(digit2)
            
            numer_res += tmp_res*tens
            tens = tens*10
        if numer_res ==0:
            return '0'
        while numer_res:
            res.append(str(numer_res%10))
            numer_res = numer_res//10
        return ''.join(res[::-1])