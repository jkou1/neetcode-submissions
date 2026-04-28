class WordDictionary:

    def __init__(self):
        self.wordDict = set()

    def addWord(self, word: str) -> None:
        self.wordDict.add(word)

    def search(self, word: str) -> bool:
        if word in self.wordDict:
            return True
        else:
            for w in self.wordDict:
                if len(w) == len(word):
                    tf = False
                    for i in range(len(word)):
                        if w[i] == word[i] or word[i] == '.':
                            tf = True
                        else:
                            print("Same len found, but char is diff")
                            tf = False
                            break
                    if tf:
                        print("Found a string of same length!")
                        return True
            return False
