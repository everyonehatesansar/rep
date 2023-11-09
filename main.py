import psycopg2
conn = psycopg2.connect (host = 'localhost', 
                           database = 'assign9',
                           user = 'postgres',
                           port = '5432',
                           password = '1234')

cur = conn.cursor()
cur.execute('SELECT * from supermarket_products LIMIT 5;')
username = [r for r in cur.fetchall()]
username = input("Введите свой логин")
if username in username:
    print("You are in the list")
    Found=True
else:
    print("You are not in the list")

conn.commit()
cur.close()
conn.close()

    