import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class MainWindow(qtw.QWidget):

    def __init__(self):
        """MainWindow Constructor"""
        super().__init__()
        # Main UI code goes here

        # Create all of the required widgets
        self.setWindowTitle('4237 Time Clock')
        self.resize(1024, 600)
        self.checkin_button = qtw.QPushButton("Check In")
        self.checkin_button.setMinimumHeight(200)
        self.checkin_button.setIcon(qtg.QIcon('img/checkin.png'))
        self.checkout_button = qtw.QPushButton('Check Out')
        self.checkout_button.setMinimumHeight(200)
        self.checkout_button.setIcon(qtg.QIcon('img/checkout.png'))
        self.message_label = qtw.QLabel('This is my test label right here!')
        self.horizontal_spacer1 = qtw.QSpacerItem(40, 20, qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Minimum)
        self.horizontal_spacer2 = qtw.QSpacerItem(40, 20, qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Minimum)
        self.horizontal_spacer3 = qtw.QSpacerItem(40, 20, qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Minimum)
        self.vertical_spacer1 = qtw.QSpacerItem(20, 40, qtw.QSizePolicy.Minimum, qtw.QSizePolicy.Expanding)
        self.vertical_spacer2 = qtw.QSpacerItem(20, 40, qtw.QSizePolicy.Minimum, qtw.QSizePolicy.Expanding)
        self.vertical_spacer3 = qtw.QSpacerItem(20, 40, qtw.QSizePolicy.Minimum, qtw.QSizePolicy.Expanding)
        self.vertical_spacer4 = qtw.QSpacerItem(40, 20, qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Minimum)
        self.vertical_spacer5 = qtw.QSpacerItem(40, 20, qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Minimum)

        # Add the widgets to the layout(s)
        main_layout = qtw.QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.addItem(self.horizontal_spacer1)

        mid_layout1 = qtw.QHBoxLayout()
        main_layout.addLayout(mid_layout1)
        mid_layout1.addItem(self.vertical_spacer1)
        mid_layout1.addWidget(self.checkin_button)
        mid_layout1.addItem(self.vertical_spacer2)
        mid_layout1.addWidget(self.checkout_button)
        mid_layout1.addItem(self.vertical_spacer3)

        main_layout.addItem(self.horizontal_spacer2)

        #mid_layout2 = qtw.QHBoxLayout()
        #main_layout.addLayout(mid_layout2)
        #mid_layout2.addItem(self.vertical_spacer4)
        #mid_layout2.addWidget(self.message_label)
        #mid_layout2.addItem(self.vertical_spacer5)
        main_layout.addWidget(self.message_label)
        main_layout.addItem(self.horizontal_spacer3)
        
        # End main UI code
        self.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())