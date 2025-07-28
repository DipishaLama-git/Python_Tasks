#Check the palindrome string
word=""
word=input("Enter a string:")
palindrome=word[::-1]
if(word==palindrome):
    print("The string is palindrome")
else:
    print("The string is not palindrome")    