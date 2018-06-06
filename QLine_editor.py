from PyQt5.QtWidgets import *
import sys
class lineEditor(QWidget):
    def __init__(self,parent=None):
        super(lineEditor,self).__init__()
        # set window title
        self.setWindowTitle("QLineEditor")
        # window QFormLayout way
        flo  = QFormLayout()
        # window line editor object definition
        Qnormaleditor = QLineEdit()
        QNoEchoEditor = QLineEdit()
        QPassEditor = QLineEdit()
        QPassEchoEditor = QLineEdit()
        # let we have definite line editor to window QFormLayout with 4 Row
        flo.addRow("Normal",Qnormaleditor)
        flo.addRow("NoEcho",QNoEchoEditor)
        flo.addRow("Password",QPassEditor)
        flo.addRow("PasswordEchoEditor",QPassEchoEditor)

        # set text to lin editor
        Qnormaleditor.setPlaceholderText("Normal")
        QNoEchoEditor.setPlaceholderText("NoEcho")
        QPassEditor.setPlaceholderText("Password")
        QPassEchoEditor.setPlaceholderText("PasswordEchoEditor")

        # set show mode
        Qnormaleditor.setEchoMode(QLineEdit.Normal)
        QNoEchoEditor.setEchoMode(QLineEdit.NoEcho)
        QPassEditor.setEchoMode(QLineEdit.Password)
        QPassEchoEditor.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        # layout
        self.setLayout(flo)

# main
if __name__ =="__main__":
    app =QApplication(sys.argv)
    win = lineEditor()
    win.show()
    sys.exit(app.exec_())




