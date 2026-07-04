class Solution:
    def reverse(self, x: int) -> int:
        reminder = x
        rev = ''

        # Define the 32-bit signed integer boundaries
        MIN_INT = -(1 << 31)       # -2147483648
        MAX_INT = (1 << 31) - 1    #  2147483647

        # The Range Check
        if MIN_INT <= x <= MAX_INT:
            if x == 0: return 0
            while(reminder != 0):
                div =  abs(reminder)%10
                print('div=',div)
                rev = rev + str(div)
                reminder = abs(reminder)//10

            rev = -int(rev) if x < 0 else int(rev )
            if not (MIN_INT <= rev <= MAX_INT):
                return 0
        else:
            return 0    
        return rev