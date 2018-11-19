from os import stat

#Creates a big file and apppends to it if already there
def fill(path, file_name, text):
    big_file = open(path + file_name +'.txt', '+a')
    while True:
        big_file.write(text + '\n')

# Returns size of file in bytes
def size(path):
    return stat(path).st_size

