import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Grid layout")

layout = QGridLayout()
layout.addWidget(QPushButton("(0,0)"),0,0)
layout.addWidget(QPushButton("(0,1)"),0,1)
layout.addWidget(QPushButton("(0,2)"),0,2)
layout.addWidget(QPushButton("(1,0)"),1,0)
layout.addWidget(QPushButton("(1,1)"),1,1)
layout.addWidget(QPushButton("(1,2)"),1,2)
layout.addWidget(QPushButton("(2,0)"),2,0)
layout.addWidget(QPushButton("(2,1) + (2,2)"),2,1,1,2)
window.setLayout(layout)

window.show()
sys.exit(app.exec())
