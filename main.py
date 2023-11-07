'''
Hashing Lab 5

'''


def import_data(file):
    table = {}
    for line in file.readlines():
        table[line] = True
    results = table
    return results


# Multiplication hash from geeksforgeeks
# https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/
# Caclulates a hash value using multiplication. The hash value starts at 1 to prevent a zero collision.
def hash_1(data, new):
    hash = 1
    for line in data:
        hashv = 0
        for char in line:
            print(char)
            if char.isalpha():
                hashv = ord(char)

            elif char.isdigit():
                hashv = int(char)
        hash *= hashv
        new.write(str(hash))
        print(hash)
        new.write('\n')
        hash = 1


# Addition hash from geeksforgeeks.
# https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/
def hash_2(data, new):
    hash = 0
    for line in data:
        for char in line:
            if char.isalpha():
                hashval = ord(char)
                hash += hashval
            if char.isdigit():
                hash += int(char)
        new.write(str(hash))
        print(hash)
        new.write('\n')
        hash = 0
    pass


def hash_3(data, new):
    pass


with open('hashpasswords.txt', 'w') as new:
    with open('passwords.txt') as file:
        if __name__ == '__main__':
            counter = 0
            data = import_data(file)
            hash_1(data, new)
            hash_2(data, new)
            hash_3(data, new)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
