'''
Hashing Lab 5

'''


def import_data(file):
    table = {}
    for line in file.readlines():
        table[line] = True
    results = table
    return results


# verifies hashes and checks to see if they are all completed.
# hash2 and hash3 are false by default.
def verify(hash1, hash2=False, hash3=False, read=None):
    if hash1 and not hash2 and not hash3:
        lines = read[0, 9999]
        for line in lines:
            print(line)
            pass
        pass
    elif hash1 and hash2 and not hash3:
        lines = read[10000, 19999]
        for line in lines:
            print(line)
            pass
        pass

    elif hash1 and hash2 and hash3:
        lines = read[20000, 29999]
        for line in lines:
            print(line)
        pass
    else:
        pass
        raise Exception("Looks like the program did an oopsie! Try running it again.")

    pass


# Multiplication hash from geeksforgeeks
# https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/
# Caclulates a hash value using multiplication. The hash value starts at 1 to prevent a zero collision.
def hash_1(data, new):
    print('Hashing dataset with first function... ')
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
        new.write('\n')
        hash = 1
    print("DONE")
    return True


# Addition hash from geeksforgeeks.
# https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/
def hash_2(data, new):
    print('Hashing dataset with second function... ')
    hash = 0
    for line in data:
        for char in line:
            if char.isalpha():
                hashval = ord(char)
                hash += hashval
            if char.isdigit():
                hash += int(char)
        new.write(str(hash))
        new.write('\n')
        hash = 0
    print('DONE')
    return True


# Subtraction hash from geeks for geeks
# https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/
def hash_3(data, new):
    print('Hashing dataset with third function...')
    hash = 0
    for line in data:
        for char in line:
            if char.isalpha():
                hashval = ord(char)
                hash -= hashval
            if char.isdigit():
                hashval = int(char)
            hash -= hashval
        new.write(str(hash))
        print(hash)
        new.write('\n')
        hash = 0
    print('DONE')
    return True


with open('hashpasswords.txt', 'r+') as new:
    with open('passwords.txt') as file:
        if __name__ == '__main__':
            counter = 0
            data = import_data(file)
            hash_done = hash_1(data, new)
            reader = new.readlines()
            verify(hash_done, False, False, reader)
            hash2_done = hash_2(data, new)
            verify(hash_done, hash2_done, False, reader)
            hash3_done = hash_3(data, new)
            verify(hash_done, hash2_done, hash3_done, reader)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
