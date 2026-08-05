class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            num = n
            sum = 0
            while(num) :
                rem = num%10
                sum = sum + rem*rem
                num = num//10
            n = sum
        return True if n == 1 else False