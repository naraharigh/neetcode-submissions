class WordDictionary:

    def __init__(self):
        self.wordstore = []
        

    def addWord(self, word: str) -> None:
        self.wordstore.append(word)
        

    def search(self, word: str) -> bool:
        import re
        pattern = "^" + word + "$"
        for str1 in self.wordstore:
            if re.match(pattern, str1):
                return True
        return False