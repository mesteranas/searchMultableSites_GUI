from . import va
import wikipedia
from guiTools import OpenLink
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
from settings import language
language.init_translation()
class main (qt.QDialog):
    def __init__(self,p,languageCode:str,text:str):
        super().__init__(p)
        self.setWindowTitle(_("wikipedia search results"))
        self.lang1=languageCode
        wikipedia.set_lang(languageCode)
        self.re=qt.QListWidget()
        self.re.setAccessibleName(_("result"))
        try:
            self.re.addItems(wikipedia.search(text))
        except:
            qt.QMessageBox.information(self,"error","no internet")
        self.opage=qt.QPushButton(_("open article"))
        self.opage.clicked.connect(self.fop)
        self.link=qt.QPushButton("open or copy link")
        self.link.clicked.connect(lambda:OpenLink(self,self.getli()))
        layout=qt.QVBoxLayout()
        layout.addWidget(self.re)
        layout.addWidget(self.opage)
        layout.addWidget(self.link)
        self.setLayout(layout)
    def getli(self):
        q=f"https://{self.lang1}.wikipedia.org/wiki/{self.re.currentItem().text()}"
        return q
    def fop(self):
        page=wikipedia.page(self.re.currentItem().text())
        va.main(self,self.getli(),page.content,page.title).exec()
def o(dc,languageCode:str,text:str):
    if text.startswith("https://"):
        from urllib.parse import urlparse
        parsed_url = urlparse(text)
        wikipedia.set_lang(parsed_url.netloc.split(".")[0])
        page=wikipedia.page(parsed_url.path.split("/")[-1].replace("_", " "))
        va.main(dc,f'https://{parsed_url.netloc.split(".")[0]}.wikipedia.org/wiki/{parsed_url.path.split("/")[-1].replace("_", " ")}',page.content,page.title).exec()
    else:
        main(dc,languageCode,text).exec()
