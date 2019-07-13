import psycopg2
import time as t

con = psycopg2.connect(
    host='localhost',
    database='sample_db',
    user='postgres',
    password='121211',
    port=5432

)


s = t.time()


cur = con.cursor('sltk')
e = (t.time() - s) * 1000

print(f'Cursor established in {e}')

s = t.time()
cur.execute('SELECT * FROM employee')
e = (t.time() - s) * 1000
print(f'query all rows established in {e}')

s = t.time()
rows = cur.fetchmany(50)
e = (t.time() - s) * 1000
print(f'Fetching 50 rows {e}')


cur.close()
con.close()