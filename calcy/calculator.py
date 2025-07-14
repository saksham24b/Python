import sys
from PyQt6.QtWidgets import(
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout
)
from PyQt6.QtGui import QFont

class Calcy(QWidget):
    def __init__(self):
        super().__init__()
        # App Settings
        self.resize(280,280)
        self.setWindowTitle("Calcy")

        # Objects
        self.grid = QGridLayout()
        self.grid
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 30))
        self.text_box.setStyleSheet("QLineEdit {color: white;}")

        self.buttons = ["1", "2", "3", "/",
                        "4", "5", "6", "*",
                        "7", "8", "9", "-",
                        "0", ".", "=", "+"]

        row = 0
        col = 0
        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            button.setStyleSheet("""
                                 QPushButton {
                                 font: 20pt; 
                                 padding: 10px; 
                                 color: white;
                                 background: #353935;
                                 border-radius: 5px;
                                 }
                                 QPushButton:pressed{
                                 background: grey;
                                 }"""
                                 )
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton("Clear")
        self.delete = QPushButton("<")
        self.clear.setStyleSheet("""
                                 QPushButton {
                                 font: 20pt Comic Sans MS; 
                                 padding: 10px; 
                                 color: black;
                                 background: #FFC300;
                                 border-radius: 12px;
                                 }
                                 QPushButton:pressed{
                                 background: #FAFAD2}""")
        self.delete.setStyleSheet("""
                                  QPushButton {
                                  font: 20pt Comic Sans MS; 
                                  padding: 10px; 
                                  color: black;
                                  background: #FFC300;
                                  border-radius: 12px;
                                  }
                                  QPushButton:pressed{
                                  background: #FAFAD2;}"""
                                  )

        # Design
        layout = QVBoxLayout()
        layout.addWidget(self.text_box)
        layout.addLayout(self.grid)

        erase_buttons = QHBoxLayout()
        erase_buttons.addWidget(self.clear)
        self.clear.clicked.connect(self.button_click)

        erase_buttons.addWidget(self.delete)
        self.delete.clicked.connect(self.button_click)

        layout.addLayout(erase_buttons)
        layout.setContentsMargins(25,25,25,25)
        self.setLayout(layout)

    def button_click(self):
        button = app.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))
            except Exception as e:
                print("Error: ", e)

        elif text == "Clear":
            self.text_box.clear()

        elif text == "<":
            current_text = self.text_box.text()
            self.text_box.setText(current_text[:-1])

        else:
            current_value = self.text_box.text()
            self.text_box.setText(current_value + text)


if __name__ in "__main__":
    app = QApplication([])
    window = Calcy()
    window.setStyleSheet("QWidget {background: black;}")
    window.show()
    sys.exit(app.exec())
