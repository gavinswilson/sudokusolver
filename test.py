import sys
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QTableWidget,
                               QTableWidgetItem)
app = QApplication()

table = QTableWidget()
table.setRowCount(9)
table.setColumnCount(9)
#table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])

item_name = QTableWidgetItem("4")
table.setItem(4, 4, item_name)
table.show()
sys.exit(app.exec())