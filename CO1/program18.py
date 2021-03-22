#Merge two dictionaries

dict1={
    "Name":"Anu",
    "Age":18,
    "Class":"Plus Two"
}
dict2={
    "Mark1":45,
    "Mark2":48,
    "Mark3":50
}
dict1.update(dict2)

print(dict1)