import pyodbc

# Look at our packages for the documentation to connect our SPECIFIC database
# get the parameters it's looking for
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Connection object of DB
docker_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + server +'; DATABASE='+ database +'; UID='+ username +'; PWD='+ password)

# Create cursor object
cursor = docker_conn.cursor() # converted to cursor object

# This is our connection object
# print(docker_conn)

# Get all the products out
# query = 'SELECT * FROM products;' # a query for all rows from Products table
# cursor.execute(query)
#
# row = cursor.fetchone()
# print(row)
# row = cursor.fetchone()
# print(row)                  # this will give us the second row as the cursor remembers the original position, it maintains state

# # Get all customers with fetchall()
# new_cursor = docker_conn.cursor()
# query2 = 'SELECT * FROM Customers'
# all_customers = new_cursor.execute(query2).fetchall()
# print(all_customers) # fetchall is generally bad practice because there could be millions of data information sets

# Better way of using fetchone instead
rows = cursor.execute('SELECT * FROM Products;')

while True:
    record = rows.fetchone()
    if record == None:
        break
    print(record)


# username, password, location to communicate

# use the pydbc to create an instance of the DB

# use their methods to send in requests and iterate of the data