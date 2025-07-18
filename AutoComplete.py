# Time Complexity: O(N + mlogm) where N is the total number of sentences and m is the number of sentences that match the input prefix.
# Space Complexity: O(N) where N is the total number of sentences.
# Brute Force Approach (HashMap + PriorityQueue Equivalent)
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.map = defaultdict(int)
        self.input_str = ""
        for i in range(len(sentences)):
            self.map[sentences[i]] += times[i]
        

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.map[self.input_str] += 1
            self.input_str = ""
            return []

        self.input_str += c
        heap = []
        for s in self.map:
            if s.startswith(self.input_str):
                heapq.heappush(heap, (-self.map[s], s))
        res = []
        for _ in range(min(3, len(heap))):
            res.append(heapq.heappop(heap)[1])
        return res


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)


# Time Complexity: O(N + m) where N is the total number of sentences and m is the number of sentences that match the input prefix.
# Space Complexity: O(N) where N is the total number of sentences.
# Trie Approach
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = defaultdict(int)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s: str, count: int):
        node = self.root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.count[s] += count
    
    def search(self, prefix: str):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node.count

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.input_str = ""
        for i in range(len(sentences)):
            self.trie.insert(sentences[i], times[i])
        

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.insert(self.input_str, 1)
            self.input_str = ""
            return []

        self.input_str += c
        freq_map = self.trie.search(self.input_str)
        if not freq_map:
            return []

        heap = [(-freq, word) for word, freq in freq_map.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(min(3, len(heap)))]
    

# Time Complexity: O(1) 
# Space Complexity: O(N * L) where N is the total number of sentences and L is the average length of the sentences.
# Trie Approach - Optimized solution

class TrieNode:
    def __init__(self):
        self.children = {}
        self.li = []

class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]):
        self.root = TrieNode()
        self.map = defaultdict(int)
        self.inp = ""
        for i in range(len(sentences)):
            self.map[sentences[i]] += times[i]
            self._insert(sentences[i])

    def _insert(self, sentence: str):
        node = self.root
        for ch in sentence:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if sentence not in node.li:
                node.li.append(sentence)
            node.li.sort(key=lambda x: (-self.map[x], x))
            if len(node.li) > 3:
                node.li.pop()

    def _search(self, prefix: str) -> list[str]:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        return node.li

    def input(self, c: str) -> list[str]:
        if c == '#':
            self.map[self.inp] += 1
            self._insert(self.inp)
            self.inp = ""
            return []
        self.inp += c
        return self._search(self.inp)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)