import json
from random import choice


def gen_person():
    name = ''
    tel = ''
    iden = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'm', 'n', 'k']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    while len(iden) != 5:
        iden += choice(nums)

    person = {
        'name': name,
        'tel': tel
    }
    p = {iden: person}
    return p


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = {}
    data.update(person_dict)
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
