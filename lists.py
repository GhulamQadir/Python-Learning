# LISTS

cities = ["Karachi","Peshawar","Lahore","Quetta","Multan","Islamabad"]
# print(cities[1])
# for i in range(len(cities)):
#     print("Welcome to " + cities[i] +" " + str(i+1))

# for i in cities:
#         if i=="Karachi":
#             print("Welcome to the city of lights,",i)
            

"'ADDING ELEMENTS IN LIST'"
# cities.append("Kashmir")  #for one argument or element
# print(cities)


"'for more than one element'"
# cities = cities+["Hyderabad","Lahore",1,2]  
# print(cities)


"'to insert element at specific index'"
# cities.insert(2,"Gujranwala")
# print(cities)


"'to update element at specific index'"
# cities[4]= "Rawalpindi"
# print(cities)


"'copy elements from list'"
# cities = ["Karachi","Peshawar","Lahore","Quetta","Multan","Islamabad"]
# copiedElements= cities[1:3]
# print(copiedElements)


"'delete element from list'"
# del cities[2]
# print(cities)


"'remove element from list'"
# cities.remove("Quetta")
# print(cities)


"'reverse list'"
# cities = cities[::-1]
# print(cities)


"'stepping'"
# cities =cities[1:6:2]
# print(cities)


# count=10
# while(count>0):
#     print(count)
#     count=count-1
   

"'reverse list using for loop'"
# for i in range(len(cities)-1,-1,-1):
#  print(cities[-i])


"'palindrome checker'"
# palin = input("Enter any word to check if its palidrome or not: ")
# if palin==palin[::-1]:
#    print("It is a palindrome word")
# else: print("It is not a palindrome word")   



"'POPPING ELEMENTS'"
# newList = []
# getElement = cities.pop(3)
# newList.append(getElement)
# print(newList)




# LIST COMPREHENSION
"'if we want to insert the table of 5 in list'"
# tableList = [i*5 for i in range(1,11)]
# print(tableList)


"'if we want to insert the any word in list'"
# wordList = [letter for letter in "Elephant"]
# print(wordList)


"'if we want to to print even number only'"
# evenList = [e for e in range(1,51) if e%2==0]
# print(evenList)


"'inputting number from user'"
# e= int(input("Enter number: "))
# table = [x*e for x in range(1,11)]
# print(table)


"'NESTED FOR LOOP'"
# matrix = [ [1,2,3,4],[5,6,7,8] ]
# transpose=[]

# for i in range(len(matrix[0])):
#     row = []
#     for j in matrix:
#         row.append(j[i])
#     transpose.append(row)
# print(transpose)


"'NESTED FOR LOOP in LIST COMPREHENSION'"
# matrix = [ [1,2,3,4],[5,6,7,8] ]
# transpose=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(transpose)


"'DICTIONARY'"
# dictionary = {"name":"abc","age":12,"rollNO":1234}
# print(dictionary["age"])
# print(dictionary)


"'CONSTRUCTOR'"
construct = dict([("name","abc"),("age",20,),("education","intermediate")])
# print(construct["name"])

"'show error if key not found'"
# print(construct.get("address","key not found"))


"'to print the keys of dictionary'"
# for i in construct.keys():
#     print(i)


"'to get both, the keys and the values'"
# for keys,values in construct.items():
#     print(f'{keys}: {values}')


"'convert list into dictionary'"
list1=[1,2,3,4,5]
list2=["Apple","Mango","Banana","Orange","Pomegranate"]
# result = {}
# for key in list1:
#     for value in list2:
#         result[key] = value
#         list2.remove(value)
#         break
# print(result)        


"'convert list into dictionary'"  # SHORT METHOD
# result =dict(zip(list1,list2))
# print(result)


# lengthofNums = int(input("Enter how many numbers you want to add: "))
# numbersDirect = {}
# for i in range(1,lengthofNums+1):
#     name = input(f"Enter the name of person {i}: ")
#     number = int(input(f"Enter the number of person {i}: "))
    
#     numbersDirect[name] = number

# print(numbersDirect)


# newDict = {1:"name"}
# newDict["age"] = "dasda"
# print(newDict)


#pop #delete #clear in dictionary
animals = {1:"cat",2: "dog",3:"goat"}
# print(animals.pop(2))
# print(animals)


# animals.clear()
# print(animals)


del animals[3]
print(animals)