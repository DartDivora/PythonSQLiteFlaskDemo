"""
This is the main database script used to communicate with the SQLite database.
This contains all necessary methods to create the schema for this database.
"""
import sqlite3 as sql
from DatabaseConstants import DatabaseConstants
import DatabaseTestingUtils as dtu
import DatabaseUtils as du

dc = DatabaseConstants()
con = sql.connect(dc.databaseName)


#dropAllTables()
du.createTables()
dtu.dummyAccountsData(10)
dtu.dummyContactsData(20)
dtu.dummyCreditCardData(10)
dtu.dummyInvoiceData(10)
dtu.dummyPaymentsData(10)
