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
def hash_1(data):
    hash = 0
    for line in data:
        for char in line:
            print(char)
            if char.isalpha():
                hashv = ord(char)
                hashv = hashv * hash
            elif char.isdigit():
                hashv = int(char)
            else:
                raise Exception("Invalid data type.")
        hashv = hashv * hash
        new.write(str(hash))
        print(hash)
        new.write('\n')
        hash = 0

    return


# Addition hash from geeksforgeeks.
# https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/
def hash_2(data):
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


def hash_3(data):
    pass


with open('hashpasswords.txt', 'w') as new:
    with open('passwords.txt') as file:
        if __name__ == '__main__':
            counter = 0
            data = import_data(file)
            hash_1(data)
            hash_2(data)
            hash_3(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
