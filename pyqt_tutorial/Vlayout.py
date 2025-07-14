import sys
from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Vertical Layout")

layout = QVBoxLayout()
layout.addWidget(QPushButton("Top"))
layout.addWidget(QPushButton("Center"))
layout.addWidget(QPushButton("Bottom"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())