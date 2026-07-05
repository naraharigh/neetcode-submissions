class Solution:
    def isPalindrome(self, x: int) -> bool:
        number =abs(x)
        i = 0
        result = 0
        if  x < 0:
            return False
        if x < 10 :
            return True
        while(number!= 0):
            digit = number%10
            print('digit=', digit)
            result = result * 10 + digit
            number = number//10
            i += 1

        print (result)    
        if result == x :
            return True
        return False