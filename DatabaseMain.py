"""
This is the main database script used to communicate with the SQLite database.
This contains all necessary methods to create the schema for this database.
"""
import sqlite3 as sql
from DatabaseConstants import DatabaseConstants
import DatabaseTestingUtils as dtu

dc = DatabaseConstants()
con = sql.connect(dc.databaseName)


# This function creates all necessary tables needed in the SQLite database.
def createTables():
    cur = con.cursor()
    cur.execute(dc.getAccountsTableCreateQuery())
    cur.execute(dc.getContactsTableCreateQuery())
    cur.execute(dc.getCreditCardsTableCreateQuery())
    cur.execute(dc.getPaymentsTableCreateQuery())
    cur.execute(dc.getInvoicesTableCreateQuery())
    con.commit()

# This function drops all non-system tables in the SQLite database. BE CAREFUL USING THIS FUNCTION!!!


def dropAllTables():
    cur = con.cursor()
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite%'")
    for row in cur.fetchall():
        query = "DROP TABLE IF EXISTS " + row[0]
        print(query)
        cur.execute(query)
        con.commit()


#dropAllTables()
createTables()
dtu.dummyAccountsData(10)
dtu.dummyContactsData(20)
dtu.dummyCreditCardData(10)
dtu.dummyInvoiceData(10)
dtu.dummyPaymentsData(10)
