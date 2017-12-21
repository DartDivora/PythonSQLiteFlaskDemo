"""
This contains all functions related to testing and "dummy" data to populate the tables.
"""
import sqlite3 as sql
from random import *
import Config

con = sql.connect(Config.Database["databaseName"])

firstNames = ["John", "Bill", "Tim", "Susan", "Kaitlyn",
              "Caitlyn", "Matt", "Josh", "Alex", "Alexis", "Terrence", "Billy", "William", "Josie", "Dale", "Jim", "Jimmy"]
lastNames = ["Smith", "Phillips", "Trembley",
             "Elizabeth", "Johnson", "Jonson", "Johannson", "Cooper", "Gretzky", "Patel", "Robertson", "Horne", "Cyrus", "Bellamy", "Mozart", "Chopin", "Debussy"]
cities = ["St. Paul", "Eagan", "Plano", "Nashville",
          "Paris", "London", "Springfield", "New York City", "Smyrna", "Murfreesboro", "Dallas", "Fargo", "Duluth", "Bemidji", "Somewhere", "Chicago", "Brunswick", "Franklin", "Shelbyville"]
states = ["TX", "MN", "MO", "TN", "KY", "AK", "AL", "NY",
          "HI", "ME", "ND", "SD", "IL", "OH", "MA", "MI", "OR", "MT"]
accountNames = [
    "Big boy's trucking", "Cirque du Soleil", "Google", "Yahoo", "Apple", "Oracle", "Microsoft", "Home Furniture", "Penn and Teller", "Gillette", "Something", "Something else", "Weird"]

# This function gets a random account ID from the accounts table.


def getRandomAccountID():
    cur = con.cursor()
    cur.execute(
        "SELECT account_id from accounts WHERE account_id IN(SELECT account_id FROM accounts ORDER BY RANDOM() LIMIT 1)")
    account_id = cur.fetchone()[0]
    return account_id

# This function gets a random unpaid invoice from the invoice table.


def getRandomUnpaidInvoice():
    cur = con.cursor()
    cur.execute(
        "SELECT invoice_number, invoice_current_amount, account_id from invoices WHERE invoice_number IN(SELECT invoice_number FROM invoices WHERE invoice_current_amount > 0 ORDER BY RANDOM() LIMIT 1)")
    return cur.fetchone()


def dummyAccountsData(count):
    cur = con.cursor()
    for i in range(1, count):
        cur.execute("REPLACE INTO accounts VALUES (?,?)",
                    (randint(111111, 999999), choice(accountNames)))
    con.commit()


def dummyContactsData(count):
    cur = con.cursor()
    for i in range(1, count):
        randFirstName = choice(firstNames)
        randLastName = choice(lastNames)
        email = randFirstName + "@" + randLastName + ".com"
        cur.execute("REPLACE INTO contacts VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (randint(111111, 999999), randFirstName, "", randLastName, "123 Test Street", choice(cities), choice(states), str(randint(11111, 99999)), "6151234567", email, getRandomAccountID()))
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


def insertIntoAccounts(account_id, account_name):
    cur = con.cursor()
    cur.execute("INSERT INTO accounts VALUES (?,?)",
                (account_id, account_name))
    con.commit()

dummyAccountsData(10)
dummyContactsData(20)
dummyCreditCardData(10)
dummyInvoiceData(10)
dummyPaymentsData(10)
