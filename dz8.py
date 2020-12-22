from os import path
from random import randint, choice
from string import ascii_lowercase
import random



def read_domains(domains_file: str):
    with open("domains.txt", "r") as file:
        lines = file.readlines()
    domain_list = [value_line.strip()[1:] for value_line in lines]
    return domain_list

print(read_domains("domains.txt"))


##############################################


def read_name(name_file: str):
    with open("names.txt", "r") as name1:
        surnames = '\n'.join([line.split()[1] for line in name1.readlines()])
        return surnames

print(read_name("name.txt"))


##############################################


with open("domains.txt", "r") as name:
    text = name.read()
    domen_name = text.replace(".", "")


with open("D:/work/gitTest/dz5/names.txt", "r") as name1:
    surnames = '\n'.join([line.split()[1] for line in name1.readlines()])


random_number = random.randint(100, 1000)
random_word = ''.join(chr(randint(ord('a'), ord('z'))) for j in range(randint(5, 7)))

emeil = surnames + "." + str(random_number) + "@" + str(random_word) + "." + domen_name
print(emeil)