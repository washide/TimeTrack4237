import sys
import sqlite3
import datetime
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from MainWidget import Ui_MainWidget
from InOutWidget import Ui_InOutWidget

db_file='TimeTrack4237.db'

class InOutWidget(qtw.QWidget):

    buttonclicked = qtc.pyqtSignal(str)

    def __init__(self, studentName, *args, **kwargs):
        super(InOutWidget, self, *args, **kwargs).__init__()
        self.ui = Ui_InOutWidget()
        self.ui.setupUi(self)
        self.ui.studentLabel.setText(studentName)
        self.ui.studentLabel.setStyleSheet("QLabel { color : #cf2027;}")
        self.showFullScreen()

        self.ui.checkinButton.clicked.connect(lambda:self.whichbtnclicked(self.ui.checkinButton))
        self.ui.checkoutButton.clicked.connect(lambda:self.whichbtnclicked(self.ui.checkoutButton))
        self.ui.cancelButton.clicked.connect(lambda:self.whichbtnclicked(self.ui.cancelButton))

    @qtc.pyqtSlot(qtw.QPushButton)
    def whichbtnclicked(self, b):
        self.ui.checkinButton.setEnabled(False)
        self.ui.checkoutButton.setEnabled(False)
        self.ui.cancelButton.setEnabled(False)
        self.buttonclicked.emit(b.objectName())
        self.close()

class MainWidget(qtw.QWidget):

    def __init__(self):
        """MainWindow Constructor"""
        super(MainWidget, self).__init__()
        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)
        self.showFullScreen()      
        self.ui.barcode.returnPressed.connect(self.checkInOut)
        self.show()

    @qtc.pyqtSlot()
    def checkInOut(self):

        dbconn = None
        studentname = None
        barcode_id = self.ui.barcode.text()
        print(f'Barcode is {barcode_id}')

        # Need to determine if the barcode matches up with a valid student in the database
        try:
            dbconn = sqlite3.connect(db_file, isolation_level=None)
            cursor=dbconn.cursor()
            sql_statement = 'SELECT name FROM students WHERE id = ?'
            cursor.execute(sql_statement, (barcode_id,))
            studentname = cursor.fetchone()
            cursor.close()

        except Exception as e:
            raise e
    
        finally:
            dbconn.close()

        # If a student name was returned, meaning it's a valid bardcode, open the InOutWindget
        if (studentname):
            self.ui.message.setText(studentname[0])
            self.inoutwindow = InOutWidget(studentname[0])
            self.inoutwindow.buttonclicked.connect(self.processClickedButton)
            self.inoutwindow.show()
        else:
            self.ui.message.setText("No student match found")
            self.timer = qtc.QTimer.singleShot(3000, lambda:self.ui.message.clear())
            self.ui.barcode.clear() 

    @qtc.pyqtSlot(str)

    def processClickedButton(self, clickedbutton):

        message = None
        if (clickedbutton == 'cancelButton'):
            message = 'Check in/out cancelled'
        elif (clickedbutton == 'checkinButton'):
            message = checkinstudent(self.ui.barcode.text())
        elif (clickedbutton == 'checkoutButton'):
            message = checkoutstudent(self.ui.barcode.text())
        else:
            print('In a place I should not be')

        self.ui.message.setText(message)
        self.timer = qtc.QTimer.singleShot(3000, lambda:self.ui.message.clear())
        self.ui.barcode.clear()

def checkinstudent(barcode_id):

    #Try to open the database
    dbconn = None
    return_message = None
    try:
        dbconn = sqlite3.connect(db_file, isolation_level=None)
        cursor=dbconn.cursor()
        # When a row exists with checkin but no checkout, student is checked in 
        sql_statement = 'SELECT COUNT(*) FROM activity WHERE id = ? AND checkin IS NOT NULL and checkout IS NULL'
        cursor.execute(sql_statement, (barcode_id,))
        rowcount = cursor.fetchone()[0]
        cursor.close()

        # Row found so let the user know they're already checked in
        if (rowcount == 1):
            return_message='You are already checked in. Check out first.'
        else:
            cursor=dbconn.cursor()
            sql_statement = "INSERT INTO activity (id, checkin, checkout) VALUES (?, DATETIME('Now', 'localtime'), NULL)"
            cursor.execute(sql_statement, (barcode_id,))
            cursor.close()
            return_message = 'Checked in'  

    except Exception as e:
        raise e
    
    finally:
        dbconn.close()
        return return_message

def checkoutstudent(barcode_id):

    #Try to open the database
    dbconn = None
    return_message = None
    try:
        dbconn = sqlite3.connect(db_file, isolation_level=None)
        cursor=dbconn.cursor()
        # When a row exists with checkin but no checkout, student is checked in 
        sql_statement = 'SELECT COUNT(*) FROM activity WHERE id = ? AND checkin IS NOT NULL and checkout IS NULL'
        cursor.execute(sql_statement, (barcode_id,))
        rowcount = cursor.fetchone()[0]
        cursor.close()

        if (rowcount != 1):
            return_message='You are not checked in. Check in first.'
        else:
            cursor=dbconn.cursor()
            sql_statement = "UPDATE activity SET checkout = DATETIME('Now', 'localtime') WHERE id = ? AND checkin IS NOT NULL and checkout IS NULL"
            cursor.execute(sql_statement, (barcode_id,))
            cursor.close()
            cursor=dbconn.cursor()
            sql_statement = "SELECT SUM( ROUND( CAST( (JULIANDAY(checkout) - JULIANDAY(checkin)) * 24 AS REAL), 2)) FROM activity where id = ?"
            cursor.execute(sql_statement, (barcode_id,))
            totalhours = cursor.fetchone()[0]
            cursor.close

            return_message = 'Checked out. Total hours: ' + f'{totalhours:.2f}'

    except Exception as e:
        raise e
    
    finally:
        dbconn.close()
        return return_message

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWidget()
    sys.exit(app.exec_())