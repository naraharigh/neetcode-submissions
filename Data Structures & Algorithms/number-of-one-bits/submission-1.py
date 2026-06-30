class Solution:
    def hammingWeight(self, n: int) -> int:
        reminder  = n
        count = 0
        while (reminder > 0):
            divider  = reminder % 2
            if divider == 1 :
                count += 1
            reminder = reminder // 2 
            # divider = reminder
            # print(reminder)   
        return count