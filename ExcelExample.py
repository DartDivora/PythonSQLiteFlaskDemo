"""
This contains a list of functions used for generating/reading a file in Excel format.
"""
from xlsxwriter.workbook import Workbook
import DatabaseMain


"""
This function takes in a filepath and select SQL query and outputs the result (with columns) to the filepath specified.
"""


def generateExcelFile(path, selectQuery):
    cur = DatabaseMain.con.cursor()
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


