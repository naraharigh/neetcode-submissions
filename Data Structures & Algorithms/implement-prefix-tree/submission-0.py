class PrefixTree:

    def __init__(self):
        self.store = []
        

    def insert(self, word: str) -> None:
        if word not in self.store :
            self.store.append(word)


    def search(self, word: str) -> bool:
        if word in self.store :
            return True
        else:
            return False    
        

    def startsWith(self, prefix: str) -> bool:
        l = len(prefix)
        for word1 in self.store :
            if word1[0:l] == prefix:
                return True
        return False
        