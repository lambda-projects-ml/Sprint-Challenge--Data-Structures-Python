import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []
# ===================================================
# ================ Dictionary Option ================
# ===================================================
dictionary = {}
for i in names_1:
    dictionary[i] = i

for i in names_2:
    if dictionary.get(i):
        duplicates.append(i)


# ===================================================
# ======================= BST =======================
# ===================================================
# class BinarySearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     def insert(self, value):

#         if value >= self.value:
#             if self.right == None:
#                 self.right = BinarySearchTree(value)
#             else:
#                 self.right.insert(value)

#         if value < self.value:
#             if self.left == None:
#                 self.left = BinarySearchTree(value)
#             else:
#                 self.left.insert(value)

#     def contains(self, target):
#         if target == self.value:
#             return True
#         elif target < self.value and self.left:
#             return self.left.contains(target)
#         elif target > self.value and self.right:
#             return self.right.contains(target)


# BST = BinarySearchTree(names_1[0])
# for i in names_1:
#     BST.insert(i)
# for j in names_2:
#     if BST.contains(j):
#         duplicates.append(j)


# ===================================================
# ================== Another Option =================
# ===================================================
# index = 0
# while index < len(names_1)-1:
#     sub_index = 0
#     for x in names_2:
#         if x == names_1[index]:
#             duplicates.append(x)
#             sub_index += 1
#         else:
#             sub_index += 1
#     index += 1

# ====================================================
# ===================== Original =====================
# ====================================================
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
