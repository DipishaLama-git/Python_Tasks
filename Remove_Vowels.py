#To remove vowels
str="vowel word coUnt"
vowels="aeiouAEIOU"
output=""
#for i in range(len(str)):
    #if str[i]!='a'and str[i]!='A' and str[i]!='e' and str[i]!='E' and str[i]!='i' and str[i]!='I' and str[i]!='o' and str[i]!='O' and str[i]!='u'and str[i]!='U' in str:
for char in str: 
    if char not in vowels:
        output=output+char
print(output)