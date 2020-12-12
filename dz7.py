import  random as rnd

my_list = [rnd.randint(1, 100) for value in range(20)]
print(my_list)

###########################################################

my_key = ["A", "B", "C"]
my_list = [rnd.randint(-10, 10) for value in range(2)]
triangel = {key: tuple(my_list) for key in my_key}
print(triangel)

#############################################################

my_str = " i'm the string "

def my_print(my_str: str):
    print(f"***{my_str}***")

my_print(my_str=my_str)

#################################44444444##############################

persons = [
    {"name": "Taras", "age": 35},
    {"name": "Ira", "age": 23},
    {"name": "Diana", "age": 19},
    {"name": "Pavel", "age": 45},
    {"name": "Danil", "age": 25},
    {"name": "Ivan", "age": 15}
    ]
############aaaaaaaaaaa###############

min_age = min(person["age"] for person in persons)
print(min_age)

############bbbbbbbbbbb###############

longest_name = max(len(person["name"]) for person in persons)
[print(person["name"]) for person in persons if len(person["name"]) == longest_name]

############vvvvvvvvvvvv###############

avr = sum(person["age"] for person in persons) / len(persons)
print(avr)

###################################################################################

my_dict_1 = {"a": 1, "b": 2, "c": 3}
my_dict_2 = {"q": 1, "w": 2, "e": 3, "a": 1}

######################aaaaaaaaaaaaaaaaaaaa####################

intersection_keys = list(set(my_dict_1.keys()).intersection(my_dict_2.keys()))
print(intersection_keys)


#######################bbbbbbbbbbbbbbbbbb#########################

difference_keys = list(set(my_dict_1.keys()).difference(my_dict_2.keys()))
print(difference_keys)

###################VVVVVVVVVVVV#############################

difference_keys = list(set(my_dict_1.keys()).difference(my_dict_2.keys()))
new_dict = {key: my_dict_1[key] for key in difference_keys}
print(new_dict)

##################ggggggggggggggggg###################

intersection_keys = list(my_dict_2.keys() & my_dict_1.keys())
unique_keys_in_dicts = list(my_dict_1.keys() ^ my_dict_2.keys())
print("unique_keys_in_dicts", unique_keys_in_dicts)

unique_dict1 = {key:  value for key, value in my_dict_1.items() if key in unique_keys_in_dicts}
print("unique_dict1", unique_dict1)
unique_dict2 = {key:  value for key, value in my_dict_2.items() if key in unique_keys_in_dicts}
print("unique_dict1", unique_dict2)
common_keys_dict ={kay: [my_dict_1[kay], my_dict_2[kay]] for kay in intersection_keys}
print("common_keys_dict", common_keys_dict)
merge_dict = {**unique_dict1, **unique_dict2, **common_keys_dict}
print("merge_dict", merge_dict)


