#create dictionary with 3 key-value pairs of studnet names and marks
students={
    "name":"Ram",
    "section":"A",
    "marks":97
}

#add a new key-value pair to an existing dictionary
students["course"]="Engineering"
for i in students.keys():
    print(students[i])

#to update dictionaries
students.update({"marks":98})
print(students)
del students["section"]
print(students)

#to check if key exist in dictionary
for i in students.keys():
    if(i=="name"):
        print("Found name key")       

#loop through all key and values in dictionary

for i,j in students.items():
    print(f"{i}:{j}")

#merge two dictionary
first={
    'a':1,
    'b':2,
    'c':3
}
second={
    'd':4,
    'e':5,
    'f':6
}
merge={**first,**second}
#first.update(second)
#merge=first|second
print(merge)
#print(first)
#print(merge)

#get the key with highest value in a dictionary
maximum=max(merge,key=merge.get)
print(f"Key with maximum value \n{maximum}:{merge[maximum]}")

#sort dictionary by its value
