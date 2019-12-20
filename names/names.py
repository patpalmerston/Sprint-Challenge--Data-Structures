import time
#this seems like a great fit for a BST
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# original
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# pat version 1
# grab the beginning index of names_2 to iterate through for duplicates against names_1
bst = BinarySearchTree(names_2[0])
# for every name in names_1 insert name into tree
for name in names_1:
    bst.insert(name)
# for every name in names_2
for name in names_2:
    # if bst already contains the name
    if bst.contains(name):
        # append the duplicates to the duplicate array
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
