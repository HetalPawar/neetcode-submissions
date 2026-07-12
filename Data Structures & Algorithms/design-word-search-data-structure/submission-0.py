class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(index, root):
            curr = root

            for c in range(index, len(word)):
                if word[c] == '.':
                    for child in curr.children.values():
                        if dfs( c + 1, child):
                            return True
                    return False

                else:
                    if word[c] not in curr.children:
                        curr.children[word[c]] = TrieNode()
                    curr = curr.children[word[c]]

            return curr.endOfWord
        
        return dfs(0, self.root)