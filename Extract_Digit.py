#Extarct the digit from string
sentence="There are 365 days in a year but leap year has 366 days"
digit=[]
for word in sentence.split():
    if word.isdigit():
        digit.append(int(word))
print(digit)        