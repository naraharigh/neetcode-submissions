class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b  = a[::-1], b[::-1]
        carry = 0
        res = ""

        for i in range(max(len(a), len(b))):
            print("in")
            digitA = ord(a[i]) - ord("0") if i < len(a)  else 0
            digitB = ord(b[i])- ord("0")  if i < len(b)  else 0
        
            total = digitA + digitB + carry
            print('total=',total)
            char =  str(total % 2)
            print('char=',char)
            res = char + res
            carry  = total // 2

        if carry :
            res = "1" + res
        return res    