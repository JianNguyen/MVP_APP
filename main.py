from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
from ui import Ui_MainWindow


class Ui(QtWidgets.QMainWindow):
    def __init__(self):

        # init params
        super(Ui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stacked.setCurrentIndex(0)
        self.ui.homebtn.setFocus()

        # function buttons
        self.ui.slide_menu_btn.clicked.connect(self.slide_menu)
        self.ui.homebtn.clicked.connect(self.home_page)
        self.ui.trainingbtn.clicked.connect(self.train_page)
        self.ui.testingbtn.clicked.connect(self.test_page)
        self.ui.aboutbtn.clicked.connect(self.about_page)
        self.ui.collection_image_btn.clicked.connect(self.collection_image_page)

        self.ui.browse_btn.clicked.connect(self.browse_file)
        self.ui.choose_file.clicked.connect(self.choose_file)
        self.show_menu = 1

    def slide_menu(self):
        if self.show_menu == 1:
            self.show_menu = 0
            self.ui.leftMenu.hide()

        else:
            self.show_menu = 1
            self.ui.leftMenu.show()

    def home_page(self):
        self.ui.stacked.setCurrentIndex(0)

    def train_page(self):
        self.ui.stacked.setCurrentIndex(1)

    def test_page(self):
        self.ui.stacked.setCurrentIndex(2)

    def collection_image_page(self):
        self.ui.stacked.setCurrentIndex(3)

    def about_page(self):
        self.ui.stacked.setCurrentIndex(4)

    def browse_file(self):
        fname = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.ui.file_name.setText(fname)

    def choose_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Select Model')
        self.ui.choose_file_name.setText(fname[0])


app = QtWidgets.QApplication(sys.argv)
application = Ui()
application.show()
app.exec_()
