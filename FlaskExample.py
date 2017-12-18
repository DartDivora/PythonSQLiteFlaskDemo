"""
This is meant to be a simple web demo using the Flask python library.
"""

from flask import Flask, request
import DatabaseUtils as du
app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/<tableName>")
def getSQLTable(tableName):
    if(du.tableExists(tableName)):
        result = du.selectAllFromTableHTML(tableName)
        return result
    return "No table found with the name: " + tableName

if __name__ == "__main__":
    app.run()
