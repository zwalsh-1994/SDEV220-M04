import sqlite3
import csv

conn = sqlite3.connect('books.db')
curs = conn.cursor()
create_table_query = '''
    CREATE TABLE IF NOT EXISTS  books (
        title TEXT,
        author TEXT,
        year INT
    )
'''
curs.execute(create_table_query)

with open('books2.csv', 'r') as books:
    csv_data = csv.reader(books)
    next(csv_data)
    for row in csv_data:
        curs.execute('INSERT INTO books VALUES (?, ?, ?)', row)
conn.commit()
conn.close()