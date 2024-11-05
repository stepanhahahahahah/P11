from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow 
import sys
from main_win import MainWindow
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()