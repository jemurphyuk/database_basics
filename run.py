from module_example import *

encoded = encode_path_file('README.md')
decoded = decode_path_file(encoded)

print(encoded)
print(decoded)