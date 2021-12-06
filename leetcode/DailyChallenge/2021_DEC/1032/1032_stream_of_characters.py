from collections import deque

class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = {}
        self.queue = deque()
        
        for word in words:
            current = self.trie
            for letter in word[::-1]:
                if letter not in current:
                    current[letter] = dict()
                current = current[letter]
            current[0] = 0
    
    def query(self, letter: str) -> bool:
        self.queue.appendleft(letter)
        current = self.trie

        for query in self.queue:
            if query not in current:
                return False
            
            if 0 in current[query]:
                return True
            
            current = current[query]