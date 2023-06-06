mylist = [8,5,12,19,22,24,9]
evenlist = []
oddlist = []
for i in mylist:
    if i % 2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print(evenlist)
print(oddlist)
