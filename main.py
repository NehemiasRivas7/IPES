import sys
from PyQt6.QtWidgets import QApplication
from View.main_view import MainWindow

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    # Set application-wide stylesheet if needed
    # app.setStyleSheet(open("View/styles/stylesheet.css").read())
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())