import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton
)
from random import choice

app = QApplication([])
window = QWidget()
window.setWindowTitle("Random text")

title = QLabel("Random Keywords")
text1 = QLabel("dgs")
text2 = QLabel("dgas")
text3 = QLabel("asdf")

button1 = QPushButton("Click me")
button2 = QPushButton("Click me")
button3 = QPushButton("Click me")

words = ['hello', 'app', 'pyqt', 'asia']

# Layout
layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)

row2.addWidget(text1, alignment= Qt.AlignmentFlag.AlignCenter)
row2.addWidget(text2, alignment= Qt.AlignmentFlag.AlignCenter)
row2.addWidget(text3, alignment= Qt.AlignmentFlag.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

layout.addLayout(row1)
layout.addLayout(row2)
layout.addLayout(row3)
window.setLayout(layout)

#Create function
def random_word1():
    word = choice(words)
    text1.setText(word)
def random_word2():
    word = choice(words)
    text2.setText(word)
def random_word3():
    word = choice(words)
    text3.setText(word)

#Events
button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)

window.show()
sys.exit(app.exec())