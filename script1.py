import psycopg2
#1. Connect to a database
#2. Create a cursor object
#3. Write an SQL query
#4. Commit changes
#5. Close database connection

#Creating a table with no entries. It will be created with the Item, Quantity, and Price column.
def create_table():
    conn = psycopg2.connect("dbname='database 1' user='postgres' password='scorpion1234' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

#insert entries into table. Call this function everytime you want to insert an entry.
#Include the item name as a string, the quantity as a integer, and the price as a double.
def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database 1' user='postgres' password='scorpion1234' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

#View the table. The table prints out as a list. 
def view():
    conn = psycopg2.connect("dbname='database 1' user='postgres' password='scorpion1234' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

#Delete an entry in the table based on the item name. All items with that name will be deleted. 
def delete(item):
    conn = psycopg2.connect("dbname='database 1' user='postgres' password='scorpion1234' host='localhost' port='5432' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM store where item= %s", (item,))
    conn.commit()
    conn.close()

#Update the quantity and price of a specific item. Items with the same 
def update(quantity, price, item):
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store set quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()



