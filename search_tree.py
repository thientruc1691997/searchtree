class TSTNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.eq = None
        self.right = None
        self.is_end = False
        self.index = -1  # Assigned when word ends


class TernarySearchTree:
    def __init__(self):
        self.root = None
        self.word_index = 0
        self.word_map = {}

    def insert(self, word):
        if word in self.word_map:
            return self.word_map[word]
        self.root = self._insert(self.root, word, 0)
        self.word_map[word] = self.word_index
        self.word_index += 1
        return self.word_map[word]

    def _insert(self, node, word, idx):
        char = word[idx]
        if node is None:
            node = TSTNode(char)
        if char < node.char:
            node.left = self._insert(node.left, word, idx)
        elif char > node.char:
            node.right = self._insert(node.right, word, idx)
        else:
            if idx + 1 < len(word):
                node.eq = self._insert(node.eq, word, idx + 1)
            else:
                node.is_end = True
                node.index = self.word_index
        return node

    def search(self, word):
        return self._search(self.root, word, 0)

    def _search(self, node, word, idx):
        if node is None:
            return False
        char = word[idx]
        if char < node.char:
            return self._search(node.left, word, idx)
        elif char > node.char:
            return self._search(node.right, word, idx)
        else:
            if idx + 1 == len(word):
                return node.is_end
            return self._search(node.eq, word, idx + 1)
    
    def count_nodes(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0
        return (1 +
                self._count_nodes(node.left) +
                self._count_nodes(node.eq) +
                self._count_nodes(node.right))
    def trace_word(self, word):
        print(f"\nTracing path for word: '{word}'")
        node = self.root
        idx = 0
        while node is not None:
            char = word[idx]
            print(f"At node {id(node)}: char='{node.char}' (target='{char}')")
            if char < node.char:
                node = node.left
            elif char > node.char:
                node = node.right
            else:
                idx += 1
                if idx == len(word):
                    print(f"Reached node {id(node)} for word end. is_end={node.is_end}, index={node.index}")
                    return
                node = node.eq
        print("Word not found.")


def load_words_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def main():
    base_dict_file = 'corncob_lowercase.txt'
    insert_file = 'insert_words.txt'
    search_file = 'not_insert_words.txt'

    tst = TernarySearchTree()

    # Load and insert base dictionary
    base_words = load_words_from_file(base_dict_file)
    for word in base_words:
        tst.insert(word)

    # Insert additional words and print index
    print("Inserting words from insert_words.txt:")
    insert_words = load_words_from_file(insert_file)
    for word in insert_words:
        index = tst.insert(word)
        print(f"Inserted '{word}' at index {index}")

    # Search words in not_insert_words.txt
    print("\nSearching words from not_insert_words.txt:")
    search_words = load_words_from_file(search_file)
    for word in search_words:
        found = tst.search(word)
        print(f"'{word}': {'Found' if found else 'Not Found'}")
    total_nodes = tst.count_nodes()
    print(f"\nTotal nodes in TST: {total_nodes}")

    tst.trace_word('a')


if __name__ == '__main__':
    main()

def export_to_dot(self, filename='tst_tree.dot'):
    with open(filename, 'w') as f:
        f.write('digraph TST {\n')
        self._export_node(self.root, f, "root")
        f.write('}\n')

def _export_node(self, node, f, nodename):
    if not node:
        return
    label = f"{node.char}\\n{'[END]' if node.is_end else ''}"
    f.write(f'"{id(node)}" [label="{label}", shape=circle];\n')

    for child, name in [(node.left, 'L'), (node.eq, 'E'), (node.right, 'R')]:
        if child:
            f.write(f'"{id(node)}" -> "{id(child)}" [label="{name}"];\n')
            self._export_node(child, f, name)


