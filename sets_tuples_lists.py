# collection = single "variable" used to store multiple values
# list = [] ordered and changeable. Duplicates with no issue
# set = {} unordered and immutable, but Add/Removes fine, can't duplicate
# tuple = () ordered and unchangeable/ Duplicates fine and faster than a list

fruits = ["apple", "orange", "banana", "coconut", "kiwi", "pineapple", "tomato", "pomegranate", "mango", "melon", "papaya"]
# print(dir(fruits))
#^^ shows every attribute for a list

# print(help(fruits))
# ^^ gives you help for documentation

# rint(fruits[::-1])

#^^ [::2]gives every fruit but skips every second element

#[::-1] reverses the entire list

# for fruit in fruits:
   # print(fruit)
# print(len(fruits))

# print("apple" in fruits)
# print("cookies" in fruits)
## ^^ basic boolean statement

# fruits[0] = "pineapple"
# fruits[1] = "orange"
# fruits[2] = "banana"
# fruits[-1] = "papaya"
## ^^ changes values of these elements using indexing
# fruits.append("pineapple")
# fruits.append("apples")
# fruits.append("kiwi")
# ##^^appending adds to the end of the list
# fruits.remove("apple")
# ##removes specific items
# fruits.sort()
# ^ sorts the items alphabetically
# fruits.reverse()
#reverses list ^
# fruits.clear
#^ removes everything
print(fruits.index("apple"))
print(fruits)
# fruits.insert(0, "pineapple")
# #adding something into a spot and moving the rest over

# ##^puts everything in alphgabetical order
