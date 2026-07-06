class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        def IsprefixorSuffix(i,o):
            nonlocal count
            if o  > len(words) - 1 :
                return
            l1 = len(words[i])

            # print(i,o,words[i],words[o][:l1],words[o][-1:l1])
            if words[o].startswith(words[i]) and words[o].endswith(words[i]):
                count += 1
                # print('count=',count)

            IsprefixorSuffix(i,o+1)
           
               

        for i in range(0,len(words)-1,1):
            # print(i,'for')
            IsprefixorSuffix(i,i+1)

        return count      