from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur_node = self.root
        for ch in word:
            cur_node = cur_node.children[ch]
        cur_node.is_word = True

    def search(self, word):
        return self.search_node(self.root, word)

    def search_node(self, node, word):
        if not word:
            return node.is_word
        for ch in word:
            if ch == '.':
                return any(self.search_node(n, word[1:]) for n in node.children.values())
            if ch in node.children:
                return self.search_node(node.children[ch], word[1:])
            else:
                return False


dic = WordDictionary()
dic.add_word('bad')
dic.add_word('good')
dic.add_word('dad')

print(dic.search('.ad'))
