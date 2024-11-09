import psycopg2
from PyQt6.QtCore import QDate

CON_STRING = "dbname=hotel_db user=hotel_admin password=hotel"
conn = psycopg2.connect(CON_STRING)
cursor = conn.cursor()

# cursor.execute("""DELETE from reservations where id in (64, 65);""")
# conn.commit()
# cursor.execute("""SELECT * from users;""")


# res = cursor.fetchall()
#
# print(res)

