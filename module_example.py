import os

working_dir = os.getcwd()

print(working_dir)

# def return_current_user():
#     print(os.getuid()) # doesn't work with windows

def encode_path_file(file):
    return os.fsencode(file) # these are the methods to encode and decode data

def decode_path_file(file):
    return os.fsdecode(file)