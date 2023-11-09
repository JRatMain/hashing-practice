'''
Hashing Lab 5
Matthew Vrbka
'''


# Reads data from the file, trimming the \n before adding it to the table.
def import_data(file):
    table = {}
    for line in file.readlines():
        line.strip('\n')
        table[line] = True
    return table


# verifies hashes and checks to see if they are all completed.
# it also displays collisions that are detected from each table.
# hash2 and hash3 are false by default.
def verify(table, hash1, hash2=False, hash3=False):
    if hash1 and not hash2 and not hash3:
        print('Displaying results for hash 1:')
        print()
    elif hash2 and not hash3:
        print('Displaying results for hash 2:')
        print()
    elif hash3:
        print('Displaying results for hash 3:')
        print()
    print('Collision Count              ' + 'Hash Number')
    for count, hash in table.items():
        print(str(count) + '                            '
              + str(hash))


# Multiplication hash concept from geeksforgeeks
# https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/
# Caclulates a hash value using multiplication. The hash value starts at 1 to prevent a zero collision.
# If it were zero, every value would be zero as a result.
def hash_1(data, new):
    print('Hashing dataset with first function... ')
    hash = 1
    hashvals = {}
    for line in data:
        hashv = 0
        for char in line:
            if char.isalpha():
                hashv = ord(char)
            elif char.isdigit():
                hashv = int(char)
        hash *= hashv
        new.write(str(hash))
        if hash not in hashvals:
            key = 1
            hashvals[key] = hash
        else:
            key = hashvals.get(hash) + 1
            hashvals[key] = hash
        new.write('\n')
        hash = 1
    print("DONE")
    return True, hashvals


# Uses an addition-based hash to hash each password, returning true once it is finished
def hash_2(data, new):
    print('Hashing dataset with second function... ')
    hash = 0
    hashvals = {}
    for line in data:
        for char in line:
            if char.isalpha():
                hashval = ord(char)
                hash += hashval
            if char.isdigit():
                hash += int(char)
        new.write(str(hash))
        if hash not in hashvals:
            key = 1
            hashvals[key] = hash
        else:
            key = hashvals.get(hash) + 1
            hashvals[key] = hash
        new.write('\n')
        hash = 0
    print('DONE')
    return True, hashvals


# It uses the absolute value of the hash value generated to place it into the table,
# as without it, it wouldn't be in the table.
def hash_3(data, new):
    hashvals = {}
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
        new.write('\n')
        if hash not in hashvals:
            key = 1
            hashvals[key] = abs(hash)
        else:
            key = hashvals.get(hash) + 1
            hashvals[key] = abs(hash)
        hash = 0

    print('DONE')
    return True, hashvals


# Main function. It opens two files, only reading from passwords but freely writing
# to hashpasswords - passwords that have been hashed. The first thing it does is truncate
# hashpassowords to the first line, deleting every value in it.
with (open('hashpasswords.txt', 'r+') as new,
      open('passwords.txt') as file):
    if __name__ == '__main__':
        new.truncate(0)
        data = import_data(file)
        hash_done, table = hash_1(data, new)
        reader = new.readline(10000)
        verify(table, hash_done, False, False)
        hash2_done, table = hash_2(data, new)
        verify(table, hash_done, hash2_done, False)
        hash3_done, table = hash_3(data, new)
        verify(table, hash_done, hash2_done, hash3_done)
