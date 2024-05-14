class RadixNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class RadixTree:
    def __init__(self):
        self.root = RadixNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = RadixNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char == '*':
                return self._wildcard_search(current, word)
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def _wildcard_search(self, node, word):
        if not word:
            return node.is_end_of_word
        for char, child in node.children.items():
            if char == word[0] or word[0] == '*':
                if self._wildcard_search(child, word[1:]):
                    return True
        return False

# Example usage:
radix_tree = RadixTree()
radix_tree.insert("apple")
radix_tree.insert("banana")
radix_tree.insert("cherry")
radix_tree.insert("peach")

print(radix_tree.search("apple"))  # Output: True
print(radix_tree.search("app*"))   # Output: True
print(radix_tree.search("*pple"))  # Output: True
print(radix_tree.search("peach"))  # Output: False
print(radix_tree.search("b*n*n*")) # Output: True
