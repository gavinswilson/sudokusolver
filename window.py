from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QTableView, QMainWindow,QLabel, QLineEdit, QVBoxLayout, QWidget
import sys

from Ui_mainwindow import Ui_Sudoku

class Window(QMainWindow, Ui_Sudoku):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Sudoku()
        self.ui.setupUi(self)
        #self.connectSignalsSlots()

    def connectSignalsSlot(self):
        #     print("Hi")
        self.action_Close.triggered.connect(self.close)
        self.action_Open.triggered.connect(self.open)
        self.action_Solve.triggered.connect(self.solve)

    def open():
        print("does nothing right now")

    def solve():
        print("Also does nothing right now")




#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")

#         self.label = QLabel()

#         self.input = QLineEdit()
#         self.input.textChanged.connect(self.label.setText)

#         layout = QVBoxLayout()
#         layout.addWidget(self.input)
#         layout.addWidget(self.label)

#         container = QWidget()
#         container.setLayout(layout)

#         # Set the central widget of the Window.
#         self.setCentralWidget(container)

