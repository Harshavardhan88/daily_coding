# trie (prefix tree) - store words and search by prefix

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._find_node(prefix) is not None

    def _find_node(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def words_with_prefix(self, prefix):
        node = self._find_node(prefix)
        if node is None:
            return []
        words = []
        self._collect(node, prefix, words)
        return words

    def _collect(self, node, current, words):
        if node.is_end:
            words.append(current)
        for ch, child in node.children.items():
            self._collect(child, current + ch, words)


trie = Trie()
for word in ["apple", "app", "apply", "banana", "band", "bandana"]:
    trie.insert(word)

print(trie.search("apple"))    # True
print(trie.search("app"))      # True
print(trie.search("apples"))   # False
print(trie.starts_with("ban")) # True
print(trie.starts_with("cat")) # False
print(trie.words_with_prefix("app"))  # ['app', 'apple', 'apply']
print(trie.words_with_prefix("band")) # ['band', 'bandana']
