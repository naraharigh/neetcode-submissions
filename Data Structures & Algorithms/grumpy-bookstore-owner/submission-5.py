class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        count = 0
        for i  in range(len(customers)):
            
            if grumpy[i] == 0:
                count += customers[i]

        custcount = 0
        total = 0
        for i in range(len(customers)):
            if grumpy[i] == 1:
                total += customers[i]
            
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    total -= customers[i - minutes]
            
            custcount = max(total, custcount)


        return  count+custcount