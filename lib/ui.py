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
from lib.mywidget import MyWidget
from n1c3_roi import N1C3_RoI
from nxc1_roi import NxC1_RoI

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(905, 810)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_10)

        self.line_check = QCheckBox(Dialog)
        self.line_check.setObjectName(u"line_check")

        self.horizontalLayout_3.addWidget(self.line_check)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.from_edit = QLineEdit(Dialog)
        self.from_edit.setObjectName(u"from_edit")
        self.from_edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.from_edit)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.to_edit = QLineEdit(Dialog)
        self.to_edit.setObjectName(u"to_edit")
        self.to_edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.to_edit)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tabWidget = MyTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tab_N1C3_RoI = N1C3_RoI()
        self.tab_N1C3_RoI.setObjectName(u"tab_N1C3_RoI")
        self.verticalLayout_3 = QVBoxLayout(self.tab_N1C3_RoI)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.tab_N1C3_RoI)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_8 = QPushButton(self.tab_N1C3_RoI)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.tab_N1C3_RoI)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.graphicsView = MyGraphicsView(self.tab_N1C3_RoI)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_3.addWidget(self.graphicsView)

        self.tabWidget.addTab(self.tab_N1C3_RoI, "")
        self.tab_NxC1_RoI = NxC1_RoI()
        self.tab_NxC1_RoI.setObjectName(u"tab_NxC1_RoI")
        self.verticalLayout_2 = QVBoxLayout(self.tab_NxC1_RoI)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.tab_NxC1_RoI)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.pushButton_9 = QPushButton(self.tab_NxC1_RoI)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.pushButton_2 = QPushButton(self.tab_NxC1_RoI)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalSlider = QSlider(self.tab_NxC1_RoI)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TicksAbove)

        self.verticalLayout_2.addWidget(self.horizontalSlider)

        self.graphicsView_2 = MyGraphicsView(self.tab_NxC1_RoI)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.verticalLayout_2.addWidget(self.graphicsView_2)

        self.tabWidget.addTab(self.tab_NxC1_RoI, "")
        self.tab = MyWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Wen Wenyu and Her Fathers 2.0", None))
        self.line_check.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u6807\u5c3a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"From", None))
        self.from_edit.setText(QCoreApplication.translate("Dialog", u"100.0", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"um", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"To", None))
        self.to_edit.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"um", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7528\u4e8e\u5bf9\u5355\u5f20\u4e09\u901a\u9053\u56fe\u50cf\u8fdb\u884cRoI\u6846\u9009\u4ee5\u53ca\u989c\u8272\u901a\u9053\u5206\u79bb", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u56fe\u7247", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_N1C3_RoI), QCoreApplication.translate("Dialog", u"N1C3 ROI", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u7528\u4e8e\u5bf9\u5355\u901a\u9053\u56fe\u50cf\u5e8f\u5217\u8fdb\u884cRoI\u6846\u9009", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u56fe\u7247", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_NxC1_RoI), QCoreApplication.translate("Dialog", u"NxC1 ROI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"future", None))
    # retranslateUi

