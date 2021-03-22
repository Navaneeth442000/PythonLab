#Sort in dictionary

dict={
    "Anu":123,
    "Manu":234,
    "Sanu":345,
    "Siva":555,
    "Banu":654,
    "Jack":231
}
print("Ascending order")
for i in sorted(dict.keys()):
    print(i,dict[i])
print("Descending order")
for i in sorted(dict.keys(),reverse=-1):
    print(i,dict[i])