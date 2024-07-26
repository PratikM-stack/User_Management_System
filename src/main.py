import sys
from PyQt5.QtWidgets import QApplication,QVBoxLayout
from login.UM_login import LoginWindow
from PyQt5 import QtGui

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=LoginWindow()
    ex.setWindowIcon(QtGui.QIcon('./assets/images/logo.png'))
    ex.setWindowTitle("User infp form application")
    ex.setGeometry(0,40,1200,600)
    #ex.setFixedSize(400,900)
    ex.show()
    
    sys.exit(app.exec_())