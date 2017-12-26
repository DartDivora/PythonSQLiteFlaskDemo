"""
This is meant to be a simple web demo using the Flask python library.
"""

from flask import Flask, request
import DatabaseUtils as du
import Config
import sqlite3 as sql
app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return Config.HTML["header"] + Config.HTML["index"]


@app.route("/query", methods=['GET'])
def getQueryForm():
    formHTML = Config.HTML["header"] + \
        Config.HTML["insertForm"].format("query")
    formHTML += """<label for="{0}">{0}:</label><input type="text" class="form-control" id="{0}" name="{0}">""".format(
        "SQLQuery")
    formHTML += """<input type="submit" name="form" value="Submit"></form></div></body></html>"""
    return formHTML


@app.route("/query", methods=['POST'])
def getQueryResults():
    SQLquery = request.form['SQLQuery']
    try:
        result = du.queryToHTML(SQLquery, None)
    except sql.Error as er:
        result = "SQL ERROR: " + str(er)
    return result


@app.route("/<tableName>/<methodName>", methods=['GET'])
def getForm(tableName, methodName):
    if(methodName.upper() == "ADD"):
        return du.getHTMLForm(tableName, methodName)
    else:
        return "Did not recognize method: " + str(methodName)


@app.route("/<tableName>/<methodName>", methods=['POST'])
def insertNewRow(tableName, methodName):
    columnNames = []
    columnParameters = []
    columnValues = []
    for k, v in request.form.items():
        if k.upper() != "FORM":
            columnNames.append(k)
            columnParameters.append("?")
            columnValues.append(v)
    query = """INSERT INTO {0} ({1}) VALUES ({2})""".format(
        tableName, ",".join(columnNames), ",".join(columnParameters))
    try:
        du.executeQuery(query, tuple(columnValues))
        result = "Successfully inserted row!"
    except sql.Error as er:
        result = "SQL ERROR: " + str(er)
    return result


@app.route("/<tableName>")
def getSQLTable(tableName):
    if(du.tableExists(tableName)):
        result = du.selectAllFromTableHTML("SELECT * FROM " + str(tableName))
        return result
    return "No table found with the name: " + tableName


if __name__ == "__main__":
    app.run()
