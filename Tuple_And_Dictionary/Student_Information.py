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

#count the frequency of each character in string using dictionary
input_str="paece"
freq={}
for char in input_str:
    if char in freq:
        freq[char]=freq[char]+1
    else:
        freq[char]=1

print(freq)        
#sort dictionary by its value

performance={
    "Singing":60,
    "Painting":30,
    "Study":80,
    "Speaking":70,
    "Writing":100
}
items=list(performance.items())

for i in range(len(items)):
    for j in range(i+1,len(items)):
        if items[i][1] > items[j][1]:
            items[i], items[j] = items[j], items[i]
    
sorted_dict=dict(items)

print(sorted_dict)