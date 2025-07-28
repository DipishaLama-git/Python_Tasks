stationery1=["book","pen","highlighter","Eraser","Pencil","Sharpner"]
stationery2=["book","highlighter","spiral_note_book","color","Sharpner"]
common_item=[]
for i in range(len(stationery1)):
    for j in range(len(stationery2)):
        if stationery1[i]==stationery2[j]:
            common_item.append(stationery1[i])
print(common_item)            