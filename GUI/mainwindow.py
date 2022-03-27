# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MyCalendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.MyCalendar.setGeometry(QtCore.QRect(20, 20, 391, 461))
        self.MyCalendar.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.MyCalendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.MyCalendar.setObjectName("MyCalendar")
        self.NewNote = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.NewNote.setGeometry(QtCore.QRect(430, 20, 351, 461))
        self.NewNote.setPlainText("")
        self.NewNote.setObjectName("NewNote")
        self.AddNote = QtWidgets.QPushButton(self.centralwidget)
        self.AddNote.setGeometry(QtCore.QRect(350, 500, 80, 25))
        self.AddNote.setObjectName("AddNote")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuNotes = QtWidgets.QMenu(self.menubar)
        self.menuNotes.setObjectName("menuNotes")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuNotes.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My Notes"))
        self.AddNote.setText(_translate("MainWindow", "Add note"))
        self.menuNotes.setTitle(_translate("MainWindow", "Notes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
