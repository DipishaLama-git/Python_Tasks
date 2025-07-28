#Remove duplicate from list
list_of_alphabets=['a','b','h','k','w','t','c','a','t','w']
duplicate_removed=[]
for alphabet in list_of_alphabets:
    if alphabet not in duplicate_removed:
        duplicate_removed.append(alphabet)
print(duplicate_removed)                        