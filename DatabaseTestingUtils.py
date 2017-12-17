"""
This contains all functions related to testing and "dummy" data to populate the tables.
"""
import sqlite3 as sql
from DatabaseConstants import DatabaseConstants
from random import *

dc = DatabaseConstants()
con = sql.connect(dc.databaseName)

#This function gets a random account ID from the accounts table.
def getRandomAccountID():
    cur = con.cursor()
    cur.execute(
        "SELECT account_id from accounts WHERE account_id IN(SELECT account_id FROM accounts ORDER BY RANDOM() LIMIT 1)")
    account_id = cur.fetchone()[0]
    return account_id

#This function gets a random unpaid invoice from the invoice table.
def getRandomUnpaidInvoice():
    cur = con.cursor()
    cur.execute(
        "SELECT invoice_number, invoice_current_amount, account_id from invoices WHERE invoice_number IN(SELECT invoice_number FROM invoices WHERE invoice_current_amount > 0 ORDER BY RANDOM() LIMIT 1)")
    return cur.fetchone()


def dummyAccountsData(count):
    cur = con.cursor()
    for i in range(1, count):
        cur.execute("REPLACE INTO accounts VALUES (?,?)",
                    (randint(111111, 999999), choice(dc.accountNames)))
    con.commit()


def dummyContactsData(count):
    cur = con.cursor()
    for i in range(1, count):
        randFirstName = choice(dc.firstNames)
        randLastName = choice(dc.lastNames)
        email = randFirstName + "@" + randLastName + ".com"
        cur.execute("REPLACE INTO contacts VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (randint(111111, 999999), randFirstName, "", randLastName, "123 Test Street", choice(dc.cities), choice(dc.states), str(randint(11111, 99999)), "6151234567", email, getRandomAccountID()))
    con.commit()


def dummyCreditCardData(count):
    cur = con.cursor()
    for i in range(1, count):
        cur.execute("REPLACE INTO credit_cards VALUES (?,?,?,?)",
                    (randint(111111, 999999), randint(1111111111111111, 9999999999999999), randint(1111, 9999), getRandomAccountID()))
        con.commit()


def dummyInvoiceData(count):
    cur = con.cursor()
    for i in range(1, count):
        invoiceNumber = randint(111111, 999999)
        invoiceAmount = randint(1, 1000)
        cur.execute("REPLACE INTO invoices VALUES (?,?,?,?,?)",
                    (invoiceNumber, invoiceNumber, invoiceAmount, invoiceAmount, getRandomAccountID()))
        con.commit()


def dummyPaymentsData(count):
    cur = con.cursor()
    for i in range(1, count):
        invoice = getRandomUnpaidInvoice()
        invoice_number = invoice[0]
        invoice_current_amount = invoice[1]
        account_id = invoice[2]
        payment_amount = randint(1, invoice_current_amount)
        invoiceAmount = randint(1, 1000)
        cur.execute("REPLACE INTO payments VALUES (?,?,?,?)",
                    (randint(111111, 999999), payment_amount, invoice_number, account_id))
        cur.execute("UPDATE invoices SET invoice_current_amount = invoice_current_amount - ? WHERE invoice_number = ? AND account_id = ?",
                    (payment_amount, invoice_number, account_id))
        con.commit()

def insertIntoAccounts(account_id,account_name):
    cur = con.cursor()
    cur.execute("INSERT INTO accounts VALUES (?,?)",(account_id,account_name))
    con.commit()
