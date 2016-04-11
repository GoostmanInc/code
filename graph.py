

class Graph:
    def __init__(self):
        self.structure={}
        self.threshold=0
    def set_structure(self,wordlist):
        for sentence in wordlist:
            for word in sentence:
                if unique(word,structure
