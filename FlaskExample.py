"""
This is meant to be a simple web demo using the Flask python library.
"""

from flask import Flask, request
import DatabaseTestingUtils as dtu
app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/accounts")
def getAccounts():
    result = dtu.selectAllFromTableHTML("accounts")
    return result

@app.route("/accounts/add")
def getAddAccount():
    return app.send_static_file('form.html')

@app.route('/accounts/add', methods=['POST'])
def addAccount():
    account_id = request.form['id']
    account_name = request.form['name']
    dtu.insertIntoAccounts(account_id,account_name.upper())
    result = "Successfully inserted account_id: " + str(account_id) + " and account_name: " + account_name + "!"
    return result

@app.route("/contacts")
def getContacts():
    result = dtu.selectAllFromTableHTML("contacts")
    return result


@app.route("/credit_cards")
def getCreditCards():
    result = dtu.selectAllFromTableHTML("credit_cards")
    return result


@app.route("/invoices")
def getInvoices():
    result = dtu.selectAllFromTableHTML("invoices")
    return result


@app.route("/payments")
def getPayments():
    result = dtu.selectAllFromTableHTML("payments")
    return result


if __name__ == "__main__":
    app.run()
