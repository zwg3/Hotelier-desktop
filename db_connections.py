import psycopg2
from PyQt6.QtCore import QDate

CON_STRING = "dbname=hotel_db user=hotel_admin password=hotel"
conn = psycopg2.connect(CON_STRING)
cursor = conn.cursor()


res_id = 54
usr_id = 3
cursor.execute("""UPDATE reservations SET

                last_update_by = %s
                WHERE id = %s;""", [usr_id, res_id])


conn.commit()

