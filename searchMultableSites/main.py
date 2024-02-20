import sys
from custome_errors import *
sys.excepthook = my_excepthook
import Wikipedia
import update
import guiTools
from settings import *
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        layout=qt.QVBoxLayout()
        self.search=qt.QLineEdit()
        self.search.setAccessibleName("input")
        self.l1=qt.QComboBox()
        self.l1.addItems([_("Search Engines"),_("Wikipedia"),_("Social media"),_("share text on"),_("Other")])
        self.l1.setAccessibleName(_("section"))
        self.l2=qt.QComboBox()
        self.l2.setAccessibleName(_("Search Engines"))
        self.l2.addItems(["google","bing","yahoo","duckduckgo","ecosia","you"])
        self.start=qt.QPushButton(_("start search"))
        self.start.clicked.connect(self.fstart)
        self.start.setDefault(True)
        self.l1.currentIndexChanged.connect(self.f2)
        layout.addWidget(self.search)
        layout.addWidget(self.l1)
        layout.addWidget(self.l2)
        layout.addWidget(self.start)

        self.setting=qt.QPushButton(_("settings"))
        self.setting.setDefault(True)
        self.setting.clicked.connect(lambda: settings(self).exec())
        layout.addWidget(self.setting)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:guiTools.OpenLink(self,"https://t.me/tprogrammers"))
        githup=qt1.QAction(_("Github"),self)
        cus.addAction(githup)
        githup.triggered.connect(lambda: guiTools.OpenLink(self,"https://Github.com/mesteranas"))
        X=qt1.QAction(_("x"),self)
        cus.addAction(X)
        X.triggered.connect(lambda:guiTools.OpenLink(self,"https://x.com/mesteranasm"))
        email=qt1.QAction(_("email"),self)
        cus.addAction(email)
        email.triggered.connect(lambda: guiTools.sendEmail("anasformohammed@gmail.com","project_type=GUI app={} version={}".format(app.name,app.version),""))
        Github_project=qt1.QAction(_("visite project on Github"),self)
        help.addAction(Github_project)
        Github_project.triggered.connect(lambda:guiTools.OpenLink(self,"https://Github.com/mesteranas/{}_GUI".format(settings_handler.appName)))
        Checkupdate=qt1.QAction(_("check for update"),self)
        help.addAction(Checkupdate)
        Checkupdate.triggered.connect(lambda:update.check(self))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:guiTools.OpenLink(self,"https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
        if settings_handler.get("update","autoCheck")=="True":
            update.check(self,message=False)
    def closeEvent(self, event):
        if settings_handler.get("g","exitDialog")=="True":
            m=guiTools.ExitApp(self)
            m.exec()
            if m:
                event.ignore()
        else:
            self.close()
    def fstart(self):
        i1=self.l1.currentIndex()
        i2=self.l2.currentIndex()
        t=self.search.text()
        link=guiTools.OpenLink
        if i1==0:
            if i2==0:
                link(self,"https://www.google.com/search?q=" + t)
            elif i2==1:
                link(self,"https://www.bing.com/search?q=" + t)
            elif i2==2:
                link(self,"https://www.yahoo.com/search?q=" + t)
            elif i2==3:
                link(self,"https://www.duckduckgo.com/?q=" + t)
            elif i2==4:
                link(self,"https://www.ecosia.org/search?q=" + t)
            elif i2==5:
                link(self,"https://www.you.com/search?q=" + t)
        elif i1==1:
            langa=Wikipedia.dictionary.lang[self.l2.currentText()]
            Wikipedia.res.o(self,langa,t)
        elif i1==2:
            if i2==0:
                link(self,"https://t.me/" + t)
            elif i2==1:
                link(self,"https://wa.me/" + t)
            elif i2==2:
                link(self,"https://twitter.com/" + t)
            elif i2==3:
                link(self,"https://facebook.com/" + t)
            elif i2==4:
                link(self,"https://m.me/" + t)
            elif i2==5:
                link(self,"https://instgram.com/" + t)
            elif i2==6:
                link(self,"https://threads.net/" + t)
        elif i1==3:
            if i2==0:
                link(self,"https://t.me/share/url?url=" + t)
            elif i2==1:
                link(self,"https://wa.me/?text=" + t)
            elif i2==2:
                link(self,"https://twitter.com/intent/tweet?text=" + t)
            elif i2==3:
                link(self,"https://www.facebook.com/sharer/sharer.php?" + t)
        elif i1==4:
            if i2==0:
                link(self,"https://www.youtube.com/results?search_query=" + t)
            elif i2==1:
                link(self,t)
    def f2(self):
        i=self.l1.currentIndex()
        if i==0:
            self.l2.setAccessibleName(_("Search Engines"))
            self.l2.clear()
            self.l2.addItems(["google","bing","yahoo","duckduckgo","ecosia","you"])
        elif i==1:
            self.l2.clear()
            self.l2.setAccessibleName(_("select search language"))
            self.l2.addItems(Wikipedia.dictionary.lang.keys())
        elif i==2:
            self.l2.clear()
            self.l2.setAccessibleName(_("open accounds on Social media by user name or phone number"))
            self.l2.addItems(["telegram","whatsapp","twitter","facebook","Messenger","instgram","threads"])
        elif i==3:
            self.l2.clear()
            self.l2.setAccessibleName(_("share text on"))
            self.l2.addItems(["telegram","whatsapp","twitter","facebook"])
        elif i==4:
            self.l2.clear()
            self.l2.setAccessibleName(_("Other"))
            self.l2.addItems(["youtube",_("open link")])

App=qt.QApplication([])
w=main()
w.show()
App.exec()