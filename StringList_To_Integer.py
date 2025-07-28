#Convert list of string to integer

list1=['1','2','3']
list2=list(map(int,list1))
#map(int,list2) applies int() function to every element in list2
print(list2)