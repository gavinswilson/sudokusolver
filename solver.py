import sys, random
from sudoku2 import sudoku
from sudElement import sudElement
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QTableWidget,
                               QTableWidgetItem)

#puzzle = sudoku(9,"111111110222222222333333333444444444555555555666666666777777777888888888999999999", "std")
puzzle = sudoku(9,"012340000050006041700000005000030000037684510000020000900000006380100050000058390", "std")
puzzle.sud_print("opts")
puzzle.sud_print("soln")


app = QApplication()

table = QTableWidget()
table.setRowCount(9)
table.setColumnCount(9)

item_name = QTableWidgetItem("4")
table.setItem(4, 4, item_name)
table.resize(930,310)
table.show()

sys.exit(app.exec())

# bob = sudElement(1,1,1,9,0,0)
# print(bob.value)
# bob.removeOpt(2)
# bob.removeOpt(3)
# bob.removeOpt(4)
# bob.removeOpt(9)
# bob.removeOpt(6)
# bob.removeOpt(7)
# bob.removeOpt(8)
# bob.removeOpt(1)
# bob.setValue()