my_list = ['aaabbb', 'bbbccc', 'cccddd', 'dddfff']
my_list_2 = []

for index, item in enumerate(my_list):
  if index % 2 != 0:
     my_list_2.append(item[::-1])
  else:
    my_list_2.append(item)

print(my_list_2)


###########################################################

my_list = ["car", "cat", "dog", "red", "apple"]
new_list =[]

for value in my_list:
    if value[0] == "a":
        new_list.append(value)

print(new_list)




###########################################################

my_list = ["car", "cat", "dog", "red", "apple"]

new_list = [new_list for new_list in my_list if "a" in new_list]
print(new_list)

###########################################################

my_list = ["one", "two", "list", "dict", 100, 1, 50]
new_list = []

for value in my_list:
    if isinstance(value, str):
        new_list.append(value)

print(new_list)

################################################################

my_str = 'aa', 'bb', 'cc', 'dd', 'bb', 'dd'
my_list = []

result = set([symbol for symbol in my_str if my_str.count(symbol) == 1])

for value in result:
    if value not in my_list:
        my_list.append(value)

print(my_list)


####################################################################


my_list = "a", "b", "f", "h", "g", "k", "s"
my_list_2 = "a", "b", "f", "h", "t", "n", "l"


result = [elem for elem in my_list if elem in my_list_2]
print(result)


##################################################################

str_1 = "one", "two", "list", "car", "car"
str_2 = "one", "list", "two", "car", "car"

my_1 = set([symbol for symbol in str_1 if str_1.count(symbol) == 1])
my_2 = set([symbol for symbol in str_2 if str_2.count(symbol) == 1])
result = list(my_1.intersection(my_2))

print(result)



