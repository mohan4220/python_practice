"""
Dictionary:
"""

person = {"name": "seethamma", "age": 67, "pension_received": False}

personal_details = {
    "name": "seethamma",
    "aadhar": "123412341234",
    "mobile": "0123456789",
}

# persons = [
#     {"name": "seethamma", "age": 67, "pension_received": False},
#     {"name": "radhamma", "age": 50, "pension_received": False},
#     {"name": "janaki", "age": 200, "pension_received": False},
# ]

# adding new key-value pair to a dictionary

person["height"] = 5.6
del person["age"]

details = [("name", "hari"), ("age", 34)]  # creating dictionary from a list of tuples

# details = dict(details)
# # clubbing two dictionaries
# person.update(personal_details)
# print(details)

"""
empty dict
dictionary with some data
dictionary from list of tuples

value updates
clubbing two dicts
reading data from a dictionary

deleting data from a dictionary using del and pop
"""
# details.pop("name")
# print(details)

# person2 = details
# print(id(person2), id(details))

persons = [
    {"name": "seethamma", "age": 67, "pension_received": False},
    {"name": "radhamma", "age": 50, "pension_received": False},
    {"name": "janaki", "age": 80, "pension_received": False},
    {"name": "ramanamma", "age": 52, "pension_received": False},
    {"name": "vijayamma", "age": 20, "pension_received": False},
]

attendance = ["seethamma", "radhamma", "ramanamma"]

# whoever attended, they took pension, received_pension should be true, and for others it is false
for person in persons:
    if person["name"] in attendance:
        person["pension_received"] = True

sentence = (
    "the big brown fox ate chocolate icecream"  # how many times a , b , c are repeated
)

letters = {"vowels": 0, "consonants": 0}

vowels = ["a", "e", "i", "o", "u"]

for letter in sentence:
    # print(letter)
    if letter in vowels:
        letters["vowels"] += 1
    else:
        letters["consonants"] += 1

print()
