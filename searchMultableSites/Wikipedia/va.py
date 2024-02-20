import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
from settings import language
language.init_translation()
class main (qt.QDialog):
    def __init__(self,p,url:str,text:str,title:str):
        super().__init__(p)
        self.setWindowTitle(title)
        self.text=qt.QTextEdit()
        self.text.setReadOnly(True)
        self.text.setText(text)
        self.text.setAccessibleName(_("contant"))
        layout=qt.QVBoxLayout()
        layout.addWidget(self.text)
        self.setLayout(layout)


