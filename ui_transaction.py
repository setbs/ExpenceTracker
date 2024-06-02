# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res_new_window_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(461, 418)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"\n"
"color: black; \n"
"font-family: Noto Sans SC;\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40); \n"
"border-radius: 7px;\n"
"margin: 12pt; \n"
"spacing: 0; ")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lablel_new_transaction = QLabel(self.frame)
        self.lablel_new_transaction.setObjectName(u"lablel_new_transaction")
        self.lablel_new_transaction.setStyleSheet(u"color: white; \n"
"font-weight: bold; \n"
"font-size: 20pt; \n"
"background-color: none; \n"
"border: none; \n"
"text-align: center; ")
        self.lablel_new_transaction.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lablel_new_transaction)

        self.chooseCategory = QComboBox(self.frame)
        self.chooseCategory.addItem("")
        self.chooseCategory.addItem("")
        self.chooseCategory.addItem("")
        self.chooseCategory.addItem("")
        self.chooseCategory.addItem("")
        self.chooseCategory.setObjectName(u"chooseCategory")
        self.chooseCategory.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"QComboBox:item {\n"
"color: black; \n"
"background-color: rgba(255, 255, 255, 40); \n"
"}")

        self.verticalLayout.addWidget(self.chooseCategory)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"font-size: 16pt; \n"
"color: white; \n"
"padding-left: 10px; ")
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.dateEdit.setDate(QDate(2024, 1, 1))

        self.verticalLayout.addWidget(self.dateEdit)

        self.description = QLineEdit(self.frame)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"font-size: 16pt; \n"
"color: white; \n"
"padding-left: 10px; \n"
"")

        self.verticalLayout.addWidget(self.description)

        self.balance = QLineEdit(self.frame)
        self.balance.setObjectName(u"balance")
        self.balance.setStyleSheet(u"font-size: 16pt; \n"
"color: white; \n"
"padding-left: 10px; \n"
"")

        self.verticalLayout.addWidget(self.balance)

        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"QComboBox:item {\n"
"color: black; \n"
"background-color: rgba(255, 255, 255, 40); \n"
"}\n"
"")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.savetran_butt = QPushButton(self.frame)
        self.savetran_butt.setObjectName(u"savetran_butt")
        self.savetran_butt.setStyleSheet(u"/* \u0412\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u044d\u0442\u043e\u0442 \u043a\u043e\u0434 \u0432 \u043f\u043e\u043b\u0435 `styleSheet` \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0432\u0438\u0434\u0436\u0435\u0442\u0430 */\n"
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
        icon.addFile(u":/Incon/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.savetran_butt.setIcon(icon)

        self.verticalLayout.addWidget(self.savetran_butt)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lablel_new_transaction.setText(QCoreApplication.translate("Dialog", u"NewTransaction", None))
        self.chooseCategory.setItemText(0, QCoreApplication.translate("Dialog", u"Groceries", None))
        self.chooseCategory.setItemText(1, QCoreApplication.translate("Dialog", u"Entertaiment", None))
        self.chooseCategory.setItemText(2, QCoreApplication.translate("Dialog", u"Auto", None))
        self.chooseCategory.setItemText(3, QCoreApplication.translate("Dialog", u"Other", None))
        self.chooseCategory.setItemText(4, QCoreApplication.translate("Dialog", u"Work", None))

        self.chooseCategory.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose category", None))
        self.description.setPlaceholderText(QCoreApplication.translate("Dialog", u"Description", None))
        self.balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"Balance", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"Income", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"Outcome", None))

        self.savetran_butt.setText(QCoreApplication.translate("Dialog", u"Save New Transaction", None))
    # retranslateUi

