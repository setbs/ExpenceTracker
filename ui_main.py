# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
# import res_ico_rc
# import res_ico_rc
import res_rc
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(842, 600)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"\n"
"color: black; \n"
"font-family: Noto Sans SC;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.BalancFrame = QFrame(self.centralwidget)
        self.BalancFrame.setObjectName(u"BalancFrame")
        self.BalancFrame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40); \n"
"border-radius: 7px;\n"
"margin: 12pt; \n"
"spacing: 0; ")
        self.verticalLayout = QVBoxLayout(self.BalancFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.BalancFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white; \n"
"font-weight: bold; \n"
"font-size: 20pt; \n"
"background-color: none; \n"
"border: none; ")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.BalancFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: white; \n"
"font-size: 30pt; \n"
"background-color: none; \n"
"border: none; ")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.BalancFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setMaximumSize(QSize(24, 16777215))
        self.label_3.setStyleSheet(u"background-color: none; \n"
"border: none; \n"
"padding-top: 10px; \n"
"max-width: 24px; \n"
"border-top: 2px solid rgba(255, 255, 255, 25); \n"
"border-radius: none; ")
        self.label_3.setPixmap(QPixmap(u":/icons/north_west_white_24dp.svg"))

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.BalancFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: white; \n"
"font-size: 16pt; \n"
"background-color: none; \n"
"border: none; \n"
"font-weight: bold; \n"
"padding-top: 10px; \n"
"spacing: 0; \n"
"border-top: 2px solid rgba(255, 255, 255, 25); \n"
"border-radius: none; ")

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_8 = QLabel(self.BalancFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: white; \n"
"font-size: 20pt; \n"
"background-color: none; \n"
"border: none; ")

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.BalancFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: none; \n"
"border: none; \n"
"padding-top: 10px; \n"
"max-width: 24px; \n"
"font-width: bold; \n"
"border-top: 2px solid rgba(255, 255, 255, 25); \n"
"border-radius: none; ")
        self.label_6.setPixmap(QPixmap(u":/icons/call_received_white_24dp.svg"))

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_5 = QLabel(self.BalancFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: white; \n"
"font-size: 16pt; \n"
"background-color: none; \n"
"border: none; \n"
"font-weight: bold; \n"
"padding-top: 10px; \n"
"spacing: 0px; \n"
"border-top: 2px solid rgba(255, 255, 255, 25); \n"
"border-radius: none; ")

        self.horizontalLayout_2.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_7 = QLabel(self.BalancFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: white; \n"
"font-size: 20pt; \n"
"background-color: none; \n"
"border: none; ")

        self.verticalLayout.addWidget(self.label_7)


        self.horizontalLayout_7.addWidget(self.BalancFrame)

        self.ExpenceCategorie = QFrame(self.centralwidget)
        self.ExpenceCategorie.setObjectName(u"ExpenceCategorie")
        self.ExpenceCategorie.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40); \n"
"border-radius: 7px;\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.ExpenceCategorie)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_11 = QLabel(self.ExpenceCategorie)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: white; \n"
"font-weight: bold; \n"
"font-size: 20pt; \n"
"background-color: none; \n"
"border: none; ")

        self.verticalLayout_2.addWidget(self.label_11)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.ExpenceCategorie)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: none; \n"
"border: none; \n"
"max-width: 24px;")
        self.label_9.setPixmap(QPixmap(u":/icons/local_grocery_store_white_24dp.svg"))

        self.horizontalLayout_6.addWidget(self.label_9)

        self.label_10 = QLabel(self.ExpenceCategorie)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: white; \n"
"font-weight: bold; \n"
"font-size: 14pt; \n"
"background-color: none;\n"
"border: none; ")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.label_12 = QLabel(self.ExpenceCategorie)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: white; \n"
"font-size: 16pt; \n"
"background-color: none;\n"
"border: none; ")

        self.horizontalLayout_6.addWidget(self.label_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_15 = QLabel(self.ExpenceCategorie)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color: none; \n"
"border: none; \n"
"max-width: 24px;\n"
"")
        self.label_15.setPixmap(QPixmap(u":/icons/sports_esports_white_24dp.svg"))

        self.horizontalLayout_5.addWidget(self.label_15)

        self.label_14 = QLabel(self.ExpenceCategorie)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: white; \n"
"font-weight: bold; \n"
"font-size: 14pt; \n"
"background-color: none;\n"
"border: none; ")

        self.horizontalLayout_5.addWidget(self.label_14)

        self.label_13 = QLabel(self.ExpenceCategorie)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: white; \n"
"font-size: 16pt; \n"
"background-color: none;\n"
"border: none; ")

        self.horizontalLayout_5.addWidget(self.label_13)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_21 = QLabel(self.ExpenceCategorie)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"background-color: none; \n"
"border: none; \n"
"max-width: 24px;")
        self.label_21.setPixmap(QPixmap(u":/icons/directions_car_white_24dp.svg"))

        self.horizontalLayout_4.addWidget(self.label_21)

        self.label_20 = QLabel(self.ExpenceCategorie)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"color: white; \n"
"font-weight: bold; \n"
"font-size: 14pt; \n"
"background-color: none;\n"
"border: none; ")

        self.horizontalLayout_4.addWidget(self.label_20)

        self.label_18 = QLabel(self.ExpenceCategorie)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: white; \n"
"font-size: 16pt; \n"
"background-color: none;\n"
"border: none; ")

        self.horizontalLayout_4.addWidget(self.label_18)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_16 = QLabel(self.ExpenceCategorie)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background-color: none; \n"
"border: none; \n"
"max-width: 24px;")
        self.label_16.setPixmap(QPixmap(u":/icons/list_white_24dp.svg"))

        self.horizontalLayout_3.addWidget(self.label_16)

        self.label_19 = QLabel(self.ExpenceCategorie)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color: white; \n"
"font-weight: bold; \n"
"font-size: 14pt; \n"
"background-color: none;\n"
"border: none; ")

        self.horizontalLayout_3.addWidget(self.label_19)

        self.label_17 = QLabel(self.ExpenceCategorie)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color: white; \n"
"font-size: 16pt; \n"
"background-color: none;\n"
"border: none; ")

        self.horizontalLayout_3.addWidget(self.label_17)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_7.addWidget(self.ExpenceCategorie)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"/* \u0412\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u044d\u0442\u043e\u0442 \u043a\u043e\u0434 \u0432 \u043f\u043e\u043b\u0435 `styleSheet` \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0432\u0438\u0434\u0436\u0435\u0442\u0430 */\n"
"QAbstractButton {\n"
"    min-width: 24px; \n"
"    min-height: 24px; \n"
"}\n"
"\n"
"QPushButton {\n"
"    color: white; \n"
"    background-color: rgba(255, 255, 255, 30);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 7px;\n"
"    width: 230px; \n"
"    height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed { \n"
"    background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	color: white; \n"
"	background-color: rgba(255, 255, 255, 30);\n"
"	border: 1px solid rgba(255, 255, 255, 40);\n"
"	border-radius: 7px;\n"
"	width: 230px; \n"
"	height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed { \n"
"	background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/edit_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"	color: white; \n"
"	background-color: rgba(255, 255, 255, 30);\n"
"	border: 1px solid rgba(255, 255, 255, 40);\n"
"	border-radius: 7px;\n"
"	width: 230px; \n"
"	height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed { \n"
"	background-color: rgba(255, 255, 255, 70);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.horizontalLayout_8.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255, 255, 255, 40); \n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px;\n"
"}\n"
"QTableView:section {\n"
"background-color: rgba(53, 53, 53); \n"
"color: white; \n"
"border: none; \n"
"height: 50px; \n"
"font-size: 14pt; \n"
"} \n"
"\n"
"QTableView:item {\n"
"border-style: none; \n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"QTableView:item-selected{\n"
"border: none; \n"
"color: rgba(255, 255, 255); \n"
"background-color: rgba(255, 255, 255, 50); \n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ExpenceTracker", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CurrentBalance", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Outcome", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"$1200", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Expence Categories", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Groceries", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"$100", None))
        self.label_15.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Entertaiment", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"$100", None))
        self.label_21.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"$100", None))
        self.label_16.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"$100", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"NewTransaction", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"EditTransaction", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"DeleteTransaction", None))
    # retranslateUi

