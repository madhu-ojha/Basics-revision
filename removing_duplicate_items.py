# Display all duplicate items from a list
sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
duplicates = []
aset = {}

for i in sample_list:
    if i not in aset:
        aset[i] = 1
    else:
        duplicates.append(i)

print(duplicates)
