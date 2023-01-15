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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

from lib.mygraphicsview import MyGraphicsView
from lib.mytabwidget import MyTabWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(929, 989)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.openImgButton = QPushButton(Dialog)
        self.openImgButton.setObjectName(u"openImgButton")

        self.horizontalLayout_6.addWidget(self.openImgButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.controlTabWidget = MyTabWidget(Dialog)
        self.controlTabWidget.setObjectName(u"controlTabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.controlTabWidget.sizePolicy().hasHeightForWidth())
        self.controlTabWidget.setSizePolicy(sizePolicy1)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.verticalLayout = QVBoxLayout(self.tab1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.tab1)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.tab1)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.line_check = QCheckBox(self.tab1)
        self.line_check.setObjectName(u"line_check")

        self.horizontalLayout_3.addWidget(self.line_check)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.tab1)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.from_edit = QLineEdit(self.tab1)
        self.from_edit.setObjectName(u"from_edit")
        self.from_edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.from_edit)

        self.label_5 = QLabel(self.tab1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.tab1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.to_edit = QLineEdit(self.tab1)
        self.to_edit.setObjectName(u"to_edit")
        self.to_edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.to_edit)

        self.label_6 = QLabel(self.tab1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.controlTabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.verticalLayout_2 = QVBoxLayout(self.tab2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.tab2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.pushButton_2 = QPushButton(self.tab2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.controlTabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.verticalLayout_5 = QVBoxLayout(self.tab3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.tab3)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.pushButton_3 = QPushButton(self.tab3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_7.addWidget(self.pushButton_3)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.controlTabWidget.addTab(self.tab3, "")

        self.verticalLayout_4.addWidget(self.controlTabWidget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gv = MyGraphicsView(Dialog)
        self.gv.setObjectName(u"gv")
        self.gv.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.gv.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_3.addWidget(self.gv)

        self.imgSlider = QSlider(Dialog)
        self.imgSlider.setObjectName(u"imgSlider")
        self.imgSlider.setOrientation(Qt.Horizontal)
        self.imgSlider.setTickPosition(QSlider.TicksAbove)

        self.verticalLayout_3.addWidget(self.imgSlider)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.logger = QTextEdit(Dialog)
        self.logger.setObjectName(u"logger")
        self.logger.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.logger)

        self.verticalLayout_4.setStretch(2, 10)

        self.retranslateUi(Dialog)

        self.controlTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Wen Wenyu and Her Fathers 2.0", None))
        self.openImgButton.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u56fe\u7247", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7528\u4e8e\u5bf9\u4efb\u610f\u56fe\u50cf\u8fdb\u884cRoI\u6846\u9009\u4ee5\u53ca\u901a\u9053\u5206\u79bb", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.line_check.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u6807\u5c3a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"From", None))
        self.from_edit.setText(QCoreApplication.translate("Dialog", u"100.0", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"um", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"To", None))
        self.to_edit.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"um", None))
        self.controlTabWidget.setTabText(self.controlTabWidget.indexOf(self.tab1), QCoreApplication.translate("Dialog", u"RoI\u533a\u57df\u6846\u9009", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u7528\u4e8e\u5bf9\u56fe\u50cf\u8fdb\u884c\u970d\u592b\u5706\u8ba1\u6570", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb\u8ba1\u6570", None))
        self.controlTabWidget.setTabText(self.controlTabWidget.indexOf(self.tab2), QCoreApplication.translate("Dialog", u"\u970d\u592b\u5706\u8ba1\u6570", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u7528\u4e8e\u5bf9\u80f6\u56fe\u8fdb\u884c\u9762\u79ef\u8ba1\u7b97", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb\u8ba1\u6570", None))
        self.controlTabWidget.setTabText(self.controlTabWidget.indexOf(self.tab3), QCoreApplication.translate("Dialog", u"\u80f6\u56fe\u7b97\u7070\u5ea6", None))
    # retranslateUi

