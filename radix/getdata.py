from pypruningradixtrie.input.csv_input_provider import *
from pypruningradixtrie.insert import *
from pypruningradixtrie.trie import *
trie = PruningRadixTrie()


def load_data(filepath, n, name_value):
    trie = PruningRadixTrie(filepath, CSVInputProvider(',', lambda x: float(x[1])))
    fill_trie_from_file(trie, filepath, CSVInputProvider(',', lambda x: float(x[1]), 0))

    found_name = []
    found_name_score = []
    for i in trie.get_top_k_for_prefix(name_value, n):
        found_name.append(i.term)
        found_name_score.append(i.score)

    print(found_name)
    print(found_name_score)