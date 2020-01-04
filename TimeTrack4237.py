import sys
import sqlite3
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from MainWidget import Ui_MainWidget
from InOutWidget import Ui_InOutWidget

db_file='TimeTrack4237.db'

class InOutWidget(qtw.QWidget):

    buttonclicked = qtc.pyqtSignal(str)

    def __init__(self):
        super(InOutWidget, self).__init__()
        self.ui = Ui_InOutWidget()
        self.ui.setupUi(self)
        #self.showFullScreen() 

        self.ui.checkinButton.clicked.connect(lambda:self.whichbtnclicked(self.ui.checkinButton))
        self.ui.checkoutButton.clicked.connect(lambda:self.whichbtnclicked(self.ui.checkoutButton))
        self.ui.cancelButton.clicked.connect(lambda:self.whichbtnclicked(self.ui.cancelButton))

    @qtc.pyqtSlot(qtw.QPushButton)
    def whichbtnclicked(self, b):
        print(f'{b.objectName()} was clicked')
        self.buttonclicked.emit(b.objectName())
        self.close()

class MainWidget(qtw.QWidget):

    def __init__(self):
        """MainWindow Constructor"""
        super(MainWidget, self).__init__()
        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)  
        #self.showFullScreen()      
        
        self.ui.barcode.returnPressed.connect(self.checkInOut)
        self.show()

    @qtc.pyqtSlot()
    def checkInOut(self):

        dbconn = None
        barcode_exists = None
        barcode_id = self.ui.barcode.text()
        print(f'Barcode is {barcode_id}')

        # Need to determine if the barcode matches up with a valid student in the databse
        try:
            dbconn = sqlite3.connect(db_file, isolation_level=None)
            cursor=dbconn.cursor()
            sql_statement = 'SELECT COUNT(*) FROM students WHERE id = ?'
            cursor.execute(sql_statement, (barcode_id,))
            barcode_exists = cursor.fetchone()[0]
            cursor.close()

        except Exception as e:
            raise e
    
        finally:
            dbconn.close()

        if (barcode_exists != 1):
            self.ui.message.setText("No student match found")
            self.timer = qtc.QTimer.singleShot(3000, lambda:self.ui.message.clear())
            self.ui.barcode.clear() 
        else:
            self.inoutwindow = InOutWidget()
            print("Show checkInOut window")
            self.inoutwindow.buttonclicked.connect(self.processClickedButton)
            self.inoutwindow.show()

    @qtc.pyqtSlot(str)
    def processClickedButton(self, clickedbutton):

        print(f'In processClickedButton: {clickedbutton}')
        message = None
        if (clickedbutton == 'cancelButton'):
            print('Check in cancelled')
            message = 'Check in/out cancelled'
        elif (clickedbutton == 'checkinButton'):
            print(f'{clickedbutton} clicked')
            message = checkinstudent(self.ui.barcode.text())
        elif (clickedbutton == 'checkoutButton'):
            print(f'{clickedbutton} clicked')
            message = checkoutstudent(self.ui.barcode.text())
        else:
            print('In a place I should not be')

        self.ui.message.setText(message)
        self.timer = qtc.QTimer.singleShot(3000, lambda:self.ui.message.clear())
        self.ui.barcode.clear()

def checkinstudent(barcode_id):

    #Try to open the database
    print (f'Inside of checkinstudent. barcode_id is {barcode_id}')
    dbconn = None
    return_message = None
    try:
        # If the barcode is good, insert a new activity record as required:
        #   1. If there is an existing row with a checkin but no checkout,
        #      update the row setting the checkout time to checkin time plus 
        #      one hour or current time, whichever is less. This is for when
        #      someone checks in 30 seconds after the prior checkin without
        #      checking out.
        #   2. If no existing rows or no existing rows from case #1, insert
        #      a new row.
        dbconn = sqlite3.connect(db_file, isolation_level=None)
        cursor=dbconn.cursor()
        sql_statement = 'SELECT COUNT(*) FROM activity WHERE id = ? AND checkin IS NOT NULL and checkout IS NULL'
        cursor.execute(sql_statement, (barcode_id,))
        rowcount = cursor.fetchone()[0]
        cursor.close()
        print (f'rowcount of not null checkin/null checkout is {rowcount}')

        # Rows found, so update the record. There should be just one... hopefully.
        if (rowcount == 1):
            #cursor=dbconn.cursor()
            #sql_statement = "UPDATE activity SET checkout = DATETIME('Now', 'localtime') WHERE id = ? AND checkin IS NOT NULL and checkout IS NULL"
            #cursor.execute(sql_statement, (barcode_id,))
            #cursor.close()
            return_message='You are already checked in. Check out first.'
        else:
            cursor=dbconn.cursor()
            sql_statement = "INSERT INTO activity (id, checkin, checkout) VALUES (?, DATETIME('Now', 'localtime'), NULL)"
            cursor.execute(sql_statement, (barcode_id,))
            cursor.close()
            return_message = 'Check in successful'    

    except Exception as e:
        # Roll back any change if something goes wrong
        raise e
    
    finally:
        dbconn.close()
        return return_message

def checkoutstudent(barcode_id):

    #Try to open the database
    print (f'Inside of checkoutstudent. barcode_id is {barcode_id}')
    dbconn = None
    return_message = None
    try:
        dbconn = sqlite3.connect(db_file, isolation_level=None)
        cursor=dbconn.cursor()
        sql_statement = 'SELECT COUNT(*) FROM activity WHERE id = ? AND checkin IS NOT NULL and checkout IS NULL'
        cursor.execute(sql_statement, (barcode_id,))
        rowcount = cursor.fetchone()[0]
        cursor.close()
        print (f'rowcount of not null checkin/null checkout is {rowcount}')

        if (rowcount != 1):
            #cursor=dbconn.cursor()
            #sql_statement = "UPDATE activity SET checkout = DATETIME('Now', 'localtime') WHERE id = ? AND checkin IS NOT NULL and checkout IS NULL"
            #cursor.execute(sql_statement, (barcode_id,))
            #sql_statement = "UPDATE activity SET checkout = DATETIME('Now', 'localtime') WHERE id = ? AND checkin IS NOT NULL and checkout IS NULL"
            #cursor.execute(sql_statement, (barcode_id,))
            #cursor.close()
            return_message='You are not checked in. Check in first.'
        else:
            cursor=dbconn.cursor()
            sql_statement = "UPDATE activity SET checkout = DATETIME('Now', 'localtime') WHERE id = ? AND checkin IS NOT NULL and checkout IS NULL"
            cursor.execute(sql_statement, (barcode_id,))
            cursor.close()
            return_message = 'Check out successful'  

    except Exception as e:
        # Roll back any change if something goes wrong
        raise e
    
    finally:
        dbconn.close()
        return return_message

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWidget()
    sys.exit(app.exec_())