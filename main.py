# secret_word = "ANFIEAA"
# code_word = "EFEAA"
# list1 = [[chr(65 + (i + j) % 26)for i in range(26)]for j in range(26)]
# print(list1)
#
#
# def vijener(list1):
#     collumn = []
#     row = []
#     a = ""
#     for i in range(len(secret_word)):
#         for j in range(26):
#             if secret_word[i] == list1[0][j]:
#                 collumn.append(j)
#     print(collumn)
#
#     for i in range(len(code_word)):
#         for j in range(26):
#             if code_word[i] == list1[j][0]:
#                 row.append(j)
#     print(row)
#
#     for i in range(len(row)):
#         for j in range(len(collumn)):
#             a += list1[row[j % len(row)]][collumn[j]]
#         return a
#
#
# print(vijener(list1))
# b = vijener(list1)
#
#
# def lalala(list1):
#     row = []
#     aa = []
#     a = ""
#     for i in range(len(code_word)):
#         for j in range(26):
#             if code_word[i] == list1[j][0]:
#                 row.append(j)
#     print(row)
#
#     for i in row:
#         for j in range(26):
#             for k in range(len(b)):
#                 if b[k] == list1[k % len(row)][j]:
#                     aa.append(j)
#     print(aa)
#
#
# lalala(list1)

list_a = [1, 2, 3, 5, 5]
list_b = [6, 7, 8, 9, 5, 5]
list_c = []
list_a.extend(list_b)
print(len(list_a))
print(list_a)
for i in range(len(list_a)):
    for j in range(len(list_a)):
        if i == j:
            continue
        elif list_a[i] == list_a[j]:
            list_a.remove(list_a[i])
print(list_a)
