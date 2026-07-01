class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for id,v in enumerate(arr):
            l = id
            max_elem = -1
            while(True):
                if (l + 1 >= len(arr)):
                    break
                max_elem = max(arr[l+1], max_elem)
                l = l + 1
               
            
            arr[id] = max_elem
        return arr