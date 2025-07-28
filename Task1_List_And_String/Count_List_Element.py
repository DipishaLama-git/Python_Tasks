#count how many times each element appear in the list
fruits=["apple","starfruit","papaya","watermelon","apricot","apple","papaya","papaya"]
unique_fruit=[]
for fruit in fruits:
    if fruit not in unique_fruit:
        unique_fruit.append(fruit)
        print(f"{fruit}:{fruits.count(fruit)}")