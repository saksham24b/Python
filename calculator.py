import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import(
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout
)

#App Settings
app = QApplication([])
window = QWidget()
window.setWindowTitle("Calcy")
window.resize(250,300)

#Objects
text_box = QLineEdit()
grid = QGridLayout()

buttons = ["1", "2", "3", "/",
           "4", "5", "6", "*",
           "7", "8", "9", "-",
           "0", ".", "=", "+"]

clear = QPushButton("Clear")
delete = QPushButton("<")

def button_click():
    button = app.sender()
    text = button.text()

    if text == "=":
        symbol = text_box.text()
        try:
            res = eval(symbol)
            text_box.setText(str(res))
        except Exception as e:
            print("Error: ", e)
    
    elif text == "Clear":
        text_box.clear()

    elif text == "<":
        current_text = text_box.text()
        text_box.setText(current_text[:-1])

    else:
        current_value = text_box.text()
        text_box.setText(current_value + text)

row = 0
col = 0
for text in buttons:
    button = QPushButton(text)
    button.clicked.connect(button_click)
    grid.addWidget(button, row, col)
    col+=1
    if col>3:
        col=0
        row+=1

#Design
layout = QVBoxLayout()
layout.addWidget(text_box)
layout.addLayout(grid)

erase_buttons = QHBoxLayout()

erase_buttons.addWidget(clear)
clear.clicked.connect(button_click)

erase_buttons.addWidget(delete)
delete.clicked.connect(button_click)

layout.addLayout(erase_buttons)
window.setLayout(layout)

#Show
window.show()
sys.exit(app.exec())