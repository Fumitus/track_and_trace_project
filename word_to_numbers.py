import string


list1 = list('Panangin')
list2 = list(string.ascii_letters[:])
result=[(j) for i in range(len(list1)) for j in range(len(list2)) if list1[i] == list2[j]]
print(result)