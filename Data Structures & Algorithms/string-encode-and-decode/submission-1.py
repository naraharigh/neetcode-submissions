class Solution:

    def encode(self, strs: List[str]) -> str:
        ens = ''
        for s in strs:
            s =  "1@"+ s
            ens = ens + s

        return ens    

    def decode(self, s: str) -> List[str]:
        s1 = []
        s1  = s.split('1@')

        if s1 is None:
            return []
        return s1[1:]