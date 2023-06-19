lang = ['python','C#','PHP','Java','TypeScript']
# print(len(lang))

# lang[4]="C++"
# print(lang)

fruits = ('Apple','Banana','Cherry')
# print(f"Type: {type(fruits)}\nLength: {len(fruits)}")
# print("Banana" in fruits)

fruits = {'Apple','Banana','Cherry'}
# fruits.add("Lemon")
# print(f"Type: {type(fruits)}\nLength: {len(fruits)}\nData: {fruits}")

# fruits.remove('Apple')

# print(f"Type: {type(fruits)}\nLength: {len(fruits)}\nData: {fruits}")

# text = ("Balalalala")
# Notext = list(reversed(text))

# print (Notext)

# text=("Kdjslkgj2pw35iulksdjfklauw3o8uqfljqoi3u57")

# temp=0

# for i in text:
#     if i =="u":
#         temp+=1

# print("Cal: ",temp)

# text1 = (f"a,b,c,")
# text2 = (f"d,e,f.")

# text3= (text1+text2)

# print(f"Type: {type(text3)} {text3}")

# import random
# listing = []
# new_list = {0}


# for i in range(12):
#     listing.append(random.randint(1,10))

# print("First list: ",listing)

# new_list.clear
# for i in range(12):
#     new_list.add(listing[i])

# print("Second list: ",new_list)

# first = {23,45,657,67,5}
# second = {23,45,15,654,65}
# result = []

# for element in first:
#     if element in second:
#         result.append(element)

# print(result)

list = [12,32,523,34,78,56,3,5,8,123]
result = []

for element in list:
    if element<list[0]:
        result.append(element)
    else:
        result.append(element)

print(result)