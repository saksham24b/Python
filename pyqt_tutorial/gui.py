import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

#Create an instance of QApplication
app = QApplication([])
#window is an instance of QWidget
window = QWidget()
# .setWindowTitle() sets the window's title in ur application
window.setWindowTitle("PyQt App") 
# Defines window's size (x,y,width,height)  x and y are screen coordinates where the window will be placed
window.setGeometry(100,100,280,80)
msg = QLabel("<h1>Hello world!</h1>", parent=window)
# .move to place msg at the coordinates
msg.move(60,15)
# show application's GUI
window.show()
# Run application's event loop
sys.exit(app.exec())
