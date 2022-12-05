# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(838, 614)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.pushButton_8 = QPushButton(self.tab_17)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(270, 200, 75, 24))
        self.tabWidget.addTab(self.tab_17, "")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.tabWidget.addTab(self.tab_18, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_17), QCoreApplication.translate("Dialog", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_18), QCoreApplication.translate("Dialog", u"Tab 2", None))
    # retranslateUi

