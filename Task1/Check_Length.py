sentence="It started raining"
words=sentence.split()
output=""
for word in words:
    if len(word)>len(output):
        output=word
print(output)        