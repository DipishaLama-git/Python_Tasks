integers=[7,1,3,5,2,9,4,10,8]
even_integers=[]
odd_integers=[]
for i in range(len(integers)):
    if(integers[i]%2==0):
        even_integers.append(integers[i])
    else:
        odd_integers.append(integers[i])
print(f"Even:{even_integers}")
print(f"Odd:{odd_integers}")            