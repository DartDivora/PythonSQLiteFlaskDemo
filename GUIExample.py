"""
This is meant to be a simple UI demo to show the display of tables using PyQt5.
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import DatabaseTestingUtils as dtu


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'GUI Demo'
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 1000
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable("contacts")
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self, name):
        cur = dtu.selectAllFromTable(name)
        columnNames = []
        for column in cur.description:
            columnNames.append(column[0])
        listToWrite = cur.fetchall()
        listToWrite.insert(0, tuple(columnNames))
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(listToWrite))
        self.tableWidget.setColumnCount(len(columnNames))
        for r, row in enumerate(listToWrite):
            for c, col in enumerate(row):
                print(str(r) + " " + str(c) + " " + str(col))
                self.tableWidget.setItem(r, c, QTableWidgetItem(str(col)))
        self.tableWidget.move(0, 0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(
            ), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
