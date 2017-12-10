"""
This class contains a list of database constants to be used by the SQLite database.
"""


class DatabaseConstants:

    def __init__(self):
        print("Newed up an object!")
        self.databaseName = "payments.db"
        self.databaseFieldDict = {
            "account_id": "INTEGER",
            "account_name": "varchar(200)",
            "contact_id": "INTEGER",
            "contact_first_name": "varchar(200)",
            "contact_middle_name": "varchar(200)",
            "contact_last_name": "varchar(200)",
            "contact_address": "varchar(200)",
            "contact_city": "varchar(40)",
            "contact_state": "varchar(2)",
            "contact_zip": "varchar(10)",
            "contact_phone": "varchar(20)",
            "contact_email": "varchar(400)",
            "credit_card_id": "INTEGER",
            "credit_card": "char(16)",
            "credit_card_pin": "char(4)",
            "payment_id": "INTEGER",
            "payment_amount": "money",
            "invoice_id": "INTEGER",
            "invoice_number": "varchar(10)",
            "invoice_total_amount": "money",
            "invoice_current_amount": "money"
        }
        self.firstNames = ["John", "Bill", "Tim", "Susan", "Kaitlyn",
                           "Caitlyn", "Matt", "Josh", "Alex", "Alexis","Terrence","Billy","William","Josie","Dale","Jim","Jimmy"]
        self.lastNames = ["Smith", "Phillips", "Trembley",
                          "Elizabeth", "Johnson", "Jonson", "Johannson","Cooper","Gretzky","Patel","Robertson","Horne","Cyrus","Bellamy","Mozart","Chopin","Debussy"]
        self.cities = ["St. Paul", "Eagan", "Plano", "Nashville",
                       "Paris", "London", "Springfield", "New York City","Smyrna","Murfreesboro","Dallas","Fargo","Duluth","Bemidji","Somewhere","Chicago","Brunswick","Franklin","Shelbyville"]
        self.states = ["TX", "MN", "MO", "TN", "KY","AK","AL","NY","HI","ME","ND","SD","IL","OH","MA","MI","OR","MT"]
        self.accountNames = [
            "Big boy's trucking", "Cirque du Soleil", "Google", "Yahoo", "Apple", "Oracle", "Microsoft","Home Furniture","Penn and Teller","Gillette", "Something", "Something else", "Weird"]

    def getDatabaseFieldType(self, databaseFieldName):
        return self.databaseFieldDict[databaseFieldName]

    def getAccountsTableCreateQuery(self):
        accountsTableQuery = " ".join(["CREATE TABLE IF NOT EXISTS", "accounts (account_id", self.getDatabaseFieldType(
            "account_id"), "PRIMARY KEY, account_name", self.getDatabaseFieldType("account_name"), ")"])
        print(accountsTableQuery)
        return accountsTableQuery

    def getCreditCardsTableCreateQuery(self):
        creditCardsTableQuery = " ".join(["CREATE TABLE IF NOT EXISTS", "credit_cards (credit_card_id", self.getDatabaseFieldType(
            "credit_card_id"), "PRIMARY KEY, credit_card", self.getDatabaseFieldType("credit_card"), ", credit_card_pin", self.getDatabaseFieldType("credit_card_pin"),
            ", account_id", self.getDatabaseFieldType("account_id"), ")"])
        print(creditCardsTableQuery)
        return creditCardsTableQuery

    def getContactsTableCreateQuery(self):
        contactsTableQuery = " ".join(["CREATE TABLE IF NOT EXISTS",
                                       "contacts (contact_id", self.getDatabaseFieldType(
                                           "contact_id"), "PRIMARY KEY, contact_first_name ", self.getDatabaseFieldType("contact_first_name"),
                                       ", contact_middle_name", self.getDatabaseFieldType(
                                           "contact_middle_name"),
                                       ", contact_last_name", self.getDatabaseFieldType(
                                           "contact_last_name"),
                                       ", contact_address", self.getDatabaseFieldType(
                                           "contact_address"),
                                       ", contact_city", self.getDatabaseFieldType(
                                           "contact_city"),
                                       ", contact_state", self.getDatabaseFieldType(
                                           "contact_state"),
                                       ", contact_zip", self.getDatabaseFieldType(
                                           "contact_zip"),
                                       ", contact_phone", self.getDatabaseFieldType(
                                           "contact_phone"),
                                       ", contact_email", self.getDatabaseFieldType(
                                           "contact_email"),
                                       ", account_id", self.getDatabaseFieldType(
                                           "account_id"),
                                       ")"
                                       ])
        print(contactsTableQuery)
        return contactsTableQuery

    def getInvoicesTableCreateQuery(self):
        invoicesTableQuery = " ".join(["CREATE TABLE IF NOT EXISTS", "invoices (invoice_id", self.getDatabaseFieldType(
            "invoice_id"), "PRIMARY KEY, invoice_number", self.getDatabaseFieldType("invoice_number"), ", invoice_total_amount", self.getDatabaseFieldType("invoice_total_amount"),
            ", invoice_current_amount", self.getDatabaseFieldType("invoice_current_amount"), ", account_id", self.getDatabaseFieldType("account_id"), ")"])
        print(invoicesTableQuery)
        return invoicesTableQuery

    def getPaymentsTableCreateQuery(self):
        paymentsTableQuery = " ".join(["CREATE TABLE IF NOT EXISTS", "payments (payment_id", self.getDatabaseFieldType(
            "payment_id"), "PRIMARY KEY, payment_amount", self.getDatabaseFieldType("payment_amount"),
            ", invoice_number", self.getDatabaseFieldType("invoice_number"),
            ", account_id", self.getDatabaseFieldType("account_id"), ")"])
        print(paymentsTableQuery)
        return paymentsTableQuery
