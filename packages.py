import requests

#
# print(web_page.headers)
#
# print(web_page.cookies)
path = requests.get('http://api.postcodes.io/postcodes/E146GT')
my_dictionary = path.json()
print(my_dictionary, '\n')
print(f"Nuts: {my_dictionary['result']['codes']['nuts']}")
print(f"Parish: {my_dictionary['result']['codes']['parish']}")
print(f"Longitude and Latitude: {my_dictionary['result']['longitude']}, {my_dictionary['result']['latitude']}")