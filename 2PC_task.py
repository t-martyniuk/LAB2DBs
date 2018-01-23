import psycopg2
from psycopg2._psycopg import DatabaseError

conn1 = psycopg2.connect(dbname="Fly Booking", user="postgres", host="localhost")
conn2 = psycopg2.connect(dbname="Hotel Booking", user="postgres", host="localhost")
conn3 = psycopg2.connect(dbname="Account", user="postgres", host="localhost")

conn1.tpc_begin(conn1.xid(42, 'flighthotel', 'conn1'))
conn2.tpc_begin(conn2.xid(42, 'flighthotel', 'conn2'))
conn3.tpc_begin(conn2.xid(42, 'flighthotel', 'conn3'))

cur1 = conn1.cursor()
cur2 = conn2.cursor()
cur3 = conn3.cursor()

cur1.execute("INSERT INTO flights VALUES ('42', 'Tanya', 'CAT 2017', 'AMS', 'JFK', '01/01/2018');")
cur2.execute("INSERT INTO hotels VALUES ('42', 'Tanya', 'Hilton', '01/01/2017', '10/01/2018');")
cur3.execute('UPDATE accounts SET "Ammount" = "Ammount" - 200 WHERE "Account ID"=\'42\'');

try:
    conn1.tpc_prepare()
    conn2.tpc_prepare()
    conn3.tpc_prepare()
except DatabaseError as e:
    print(e)
    conn1.tpc_rollback()
    conn2.tpc_rollback()
    conn3.tpc_rollback()
else:
    conn1.tpc_commit()
    conn2.tpc_commit()
    conn3.tpc_commit()

cur1.close()
conn1.close()
cur2.close()
conn2.close()
