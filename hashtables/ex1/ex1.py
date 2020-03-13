#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for index, value in enumerate(weights):
        hash_table_insert(ht, value, index)
    for i in range(length):
        weight = weights[i]
        if hash_table_retrieve(ht, limit - weight):
            pair = (i, hash_table_retrieve(ht, limit - weight))
            print(pair)
            return pair
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")