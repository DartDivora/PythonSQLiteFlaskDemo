from xlsxwriter.workbook import Workbook
import sqlite3 as sql
import Config

con = sql.connect(Config.Database["databaseName"])


# This function creates all necessary tables needed in the SQLite database.
def createTables():
    cur = con.cursor()
    cur.executescript(Config.Database["createTablesQuery"])
    print("Created all tables!")
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

# USE AT YOUR OWN RISK, DELETES ALL ROWS FROM ALL TABLES


def cleanTables():
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    for row in cur:
        con.cursor().execute("DELETE FROM " + row[0])
        con.commit()


def tableExists(tableName):
    cur = con.cursor()
    cur.execute(
        "SELECT COUNT(1) FROM sqlite_master WHERE type='table' AND name=?;", (tableName,))
    if(cur.fetchone()[0] < 1):
        return False
    return True


def selectAllFromTable(tableName):
    cur = con.cursor()
    cur.execute("SELECT * FROM " + tableName)
    return cur


def selectAllFromTableHTML(query):
    return queryToHTML(query,None)


def queryToHTML(query,tupleValues):
    cur = executeQuery(query, tupleValues)
    resultHTML = Config.HTML["header"]
    resultHTML += Config.HTML["selectTable"]
    columnNames = []
    for column in cur.description:
        resultHTML += "<th>" + column[0] + " </th> \n"
    resultHTML += "</tr></thead><tbody> \n"
    for row in cur:
        resultHTML += "<tr> \n"
        for column in row:
            resultHTML += "<td>" + str(column) + " </td> \n"
        resultHTML += "</tr> \n"
    resultHTML += "</tbody></table></div></body></html>"
    return resultHTML

def executeQuery(query, tupleValues):
    cur = con.cursor()
    if tupleValues is None:
        cur.execute(query)
    else:
        cur.execute(query, tupleValues)
    con.commit()
    return cur


def getHTMLForm(tableName, methodName):
    cur = con.cursor()
    query = """PRAGMA table_info('{0}')""".format(tableName,)
    cur.execute(query)
    formHTML = Config.HTML["header"]
    formHTML += Config.HTML["insertForm"].format(
        str(tableName) + "/" + str(methodName))
    for row in cur:
        formHTML += """<label for="{0}">{0}({1}):</label><input type="text" class="form-control" id="{0}" name="{0}">""".format(
            str(row[1]), str(row[2]))
    formHTML += """<input type="submit" name="form" value="Submit"></form></div></body></html>"""
    return formHTML


"""
This function takes in a filepath and select SQL query and outputs the result (with columns) to the filepath specified.
"""


def generateExcelFile(path, selectQuery):
    cur = con.cursor()
    cur.execute(selectQuery)
    workbook = Workbook(path)
    sheet = workbook.add_worksheet()
    columnNames = []
    for column in cur.description:
        columnNames.append(column[0])
    listToWrite = cur.fetchall()
    listToWrite.insert(0, tuple(columnNames))
    print(listToWrite)
    for r, row in enumerate(listToWrite):
        for c, col in enumerate(row):
            sheet.write(r, c, col)
    workbook.close()


"""
This is the main database script used to communicate with the SQLite database.
This contains all necessary methods to create the schema for this database.
"""


def main():
    createTables()
    # dropAllTables()
    #generateExcelFile("test.xlsx","SELECT * FROM accounts")


if __name__ == "__main__":
    main()
