"""
This is meant to be a simple web demo using the Flask python library.
"""

from flask import Flask, request
import DatabaseUtils as du
app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return app.send_static_file("index.html")


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
    du.executeQuery(query, tuple(columnValues))
    result = "Successfully inserted row!"
    return result


@app.route("/<tableName>")
def getSQLTable(tableName):
    if(du.tableExists(tableName)):
        result = du.selectAllFromTableHTML(tableName)
        return result
    return "No table found with the name: " + tableName


if __name__ == "__main__":
    app.run()
