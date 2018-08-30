import sys

# 1 Byte == 8 Bit
# 1 bit == 0.125 byte

empty_list = []
print(f"\nSize of empty list: {sys.getsizeof(empty_list)} bytes\n")  # 64 bytes

one_itm_ls = [1]
print(f"\nSize of list with one item: {sys.getsizeof(one_itm_ls)} bytes\n")  # 72 bytes

# list > tuple

empty_tuple = ()
print(f"\nSize of empty tuple: {sys.getsizeof(empty_tuple)} bytes\n")  # 48 bytes

one_itm_tuple = (1,)
print(f"\nSize of tuple with one item: {sys.getsizeof(one_itm_tuple)} bytes\n")  # 56 bytes

items_list = [i for i in range(100)]
print(f"\nSize of list with 100 items: {sys.getsizeof(items_list)} bytes\n")  # 912 bytes

items_tuple = tuple([i for i in range(100)])
print(f"\nSize of tuple with 100 items: {sys.getsizeof(items_tuple)} bytes\n")  # 848 bytes

empty_dict = {}
print(f"\nSize of empty dict: {sys.getsizeof(empty_dict)} bytes\n")  # all is 240 bytes

one_itm_dict = {1: "a"}
print(f"\nSize of dict with one item: {sys.getsizeof(one_itm_dict)} bytes\n")  # all is 240 bytes

two_itms_dict = {1: "a", 2: "b"}
print(f"\nSize of dict with two items: {sys.getsizeof(two_itms_dict)} bytes\n")  # all is 240 bytes

keys_ls = [i for i in range(100)]
values_ls = [i for i in range(101, 201)]
full_dict = dict(zip(keys_ls, values_ls))
print(len(full_dict))
print(f"\nSize of full dict: {sys.getsizeof(full_dict)} bytes\n")  # 4,704 kb

empty_str = ""
print(f"\nSize of empty string: {sys.getsizeof(empty_str)} bytes\n")  # 49 bytes

one_l_str = "a"
print(f"\nSize of not empty string: {sys.getsizeof(one_l_str)} bytes\n")  # 50 bytes

hund_str = "".join([str(i) for i in range(100)])
print(f"\nSize of hund. items string: {sys.getsizeof(hund_str)} bytes\n")  # 239 bytes

small_int = 1
print(f"\nSize of small int: {sys.getsizeof(small_int)} bytes\n")  # 28 bytes

big_int = int("".join([str(i) for i in range(100)]))
print(f"\nSize of big int: {sys.getsizeof(big_int)} bytes\n")  # 108 bytes

empty_set = set()
print(f"\nSize of empty set: {sys.getsizeof(empty_set)} bytes\n")  # 224 bytes

one_itm_set = {1}
print(f"\nSize of set with one item: {sys.getsizeof(one_itm_set)} bytes\n")  # 224 bytes

items_set = {i for i in range(100)}
print(len(items_set))
print(f"\nSize of set with 100 items: {sys.getsizeof(items_set)} bytes\n")  # 8,416 kb

empty_frozen_set = frozenset()
print(f"\nSize of empty frozenset: {sys.getsizeof(empty_frozen_set)} bytes\n")  # 224 bytes

one_itm_frozenset = frozenset({1})
print(f"\nSize of frozenset with one item: {sys.getsizeof(one_itm_frozenset)} bytes\n")  # 224 bytes

items_frozenset = frozenset({i for i in range(100)})
print(f"\nSize of frozenset with 100 items: {sys.getsizeof(items_frozenset)} bytes\n")  # 4,320 kb
