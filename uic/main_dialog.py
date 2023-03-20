# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

from lib.mygraphicsview import MyGraphicsView
from lib.roi import RoI

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1115, 1206)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.controlTabWidget = QTabWidget(Dialog)
        self.controlTabWidget.setObjectName(u"controlTabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.controlTabWidget.sizePolicy().hasHeightForWidth())
        self.controlTabWidget.setSizePolicy(sizePolicy1)
        self.tab1 = RoI()
        self.tab1.setObjectName(u"tab1")
        self.verticalLayout_7 = QVBoxLayout(self.tab1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.tab1)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.tab1OpenImgButton = QPushButton(self.tab1)
        self.tab1OpenImgButton.setObjectName(u"tab1OpenImgButton")

        self.horizontalLayout.addWidget(self.tab1OpenImgButton)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_14)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.tab1ChannelGroup = QGroupBox(self.tab1)
        self.tab1ChannelGroup.setObjectName(u"tab1ChannelGroup")
        self.horizontalLayout_6 = QHBoxLayout(self.tab1ChannelGroup)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton = QRadioButton(self.tab1ChannelGroup)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.horizontalLayout_6.addWidget(self.radioButton)

        self.radioButton_4 = QRadioButton(self.tab1ChannelGroup)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_6.addWidget(self.radioButton_4)

        self.radioButton_3 = QRadioButton(self.tab1ChannelGroup)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_6.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.tab1ChannelGroup)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_6.addWidget(self.radioButton_2)


        self.verticalLayout_7.addWidget(self.tab1ChannelGroup)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tab1GV = MyGraphicsView(self.tab1)
        self.tab1GV.setObjectName(u"tab1GV")
        self.tab1GV.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tab1GV.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_3.addWidget(self.tab1GV)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.tab1)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.tab1SaveButton = QPushButton(self.groupBox)
        self.tab1SaveButton.setObjectName(u"tab1SaveButton")

        self.horizontalLayout_11.addWidget(self.tab1SaveButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.tab1AddLineCheck = QGroupBox(self.groupBox)
        self.tab1AddLineCheck.setObjectName(u"tab1AddLineCheck")
        self.tab1AddLineCheck.setCheckable(True)
        self.tab1AddLineCheck.setChecked(False)
        self.verticalLayout_8 = QVBoxLayout(self.tab1AddLineCheck)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.tab1AddLineCheck)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.from_edit = QLineEdit(self.tab1AddLineCheck)
        self.from_edit.setObjectName(u"from_edit")
        self.from_edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.from_edit)

        self.label_5 = QLabel(self.tab1AddLineCheck)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.tab1AddLineCheck)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(30, 0))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.to_edit = QLineEdit(self.tab1AddLineCheck)
        self.to_edit.setObjectName(u"to_edit")
        self.to_edit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.to_edit)

        self.label_6 = QLabel(self.tab1AddLineCheck)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)


        self.verticalLayout_10.addWidget(self.tab1AddLineCheck)

        self.tab1SaveAllCheckBox = QCheckBox(self.groupBox)
        self.tab1SaveAllCheckBox.setObjectName(u"tab1SaveAllCheckBox")
        self.tab1SaveAllCheckBox.setChecked(True)

        self.verticalLayout_10.addWidget(self.tab1SaveAllCheckBox)

        self.tab1SaveEachCheckBox = QCheckBox(self.groupBox)
        self.tab1SaveEachCheckBox.setObjectName(u"tab1SaveEachCheckBox")

        self.verticalLayout_10.addWidget(self.tab1SaveEachCheckBox)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.groupBox_2 = QGroupBox(self.tab1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tab1Hist = QLabel(self.groupBox_2)
        self.tab1Hist.setObjectName(u"tab1Hist")
        self.tab1Hist.setMinimumSize(QSize(0, 256))

        self.verticalLayout_9.addWidget(self.tab1Hist)

        self.tab1ParaGroup = QGroupBox(self.groupBox_2)
        self.tab1ParaGroup.setObjectName(u"tab1ParaGroup")
        self.verticalLayout = QVBoxLayout(self.tab1ParaGroup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_5 = QRadioButton(self.tab1ParaGroup)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.tab1ParaGroup)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.verticalLayout.addWidget(self.radioButton_6)


        self.verticalLayout_9.addWidget(self.tab1ParaGroup)

        self.tab1BCBar = QGroupBox(self.groupBox_2)
        self.tab1BCBar.setObjectName(u"tab1BCBar")
        self.verticalLayout_6 = QVBoxLayout(self.tab1BCBar)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.tab1BCBar)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_8.addWidget(self.label_8)

        self.tab1SliderMin = QSlider(self.tab1BCBar)
        self.tab1SliderMin.setObjectName(u"tab1SliderMin")
        self.tab1SliderMin.setMaximum(255)
        self.tab1SliderMin.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.tab1SliderMin)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.tab1BCBar)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_9.addWidget(self.label_9)

        self.tab1SliderMax = QSlider(self.tab1BCBar)
        self.tab1SliderMax.setObjectName(u"tab1SliderMax")
        self.tab1SliderMax.setMaximum(255)
        self.tab1SliderMax.setValue(255)
        self.tab1SliderMax.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.tab1SliderMax)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.tab1BCBar)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_10.addWidget(self.label_10)

        self.horizontalSlider_3 = QSlider(self.tab1BCBar)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.horizontalSlider_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.tab1BCBar)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_14.addWidget(self.label_14)

        self.horizontalSlider_7 = QSlider(self.tab1BCBar)
        self.horizontalSlider_7.setObjectName(u"horizontalSlider_7")
        self.horizontalSlider_7.setOrientation(Qt.Horizontal)

        self.horizontalLayout_14.addWidget(self.horizontalSlider_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)


        self.verticalLayout_9.addWidget(self.tab1BCBar)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3.setStretch(0, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tab1ImgSlider = QSlider(self.tab1)
        self.tab1ImgSlider.setObjectName(u"tab1ImgSlider")
        self.tab1ImgSlider.setEnabled(False)
        self.tab1ImgSlider.setOrientation(Qt.Horizontal)
        self.tab1ImgSlider.setTickPosition(QSlider.TicksAbove)

        self.verticalLayout_7.addWidget(self.tab1ImgSlider)

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

        self.logger = QTextEdit(Dialog)
        self.logger.setObjectName(u"logger")
        self.logger.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.logger)

        self.verticalLayout_4.setStretch(0, 1)
#if QT_CONFIG(shortcut)
        self.label_8.setBuddy(self.tab1SliderMin)
        self.label_9.setBuddy(self.tab1SliderMax)
        self.label_10.setBuddy(self.horizontalSlider_3)
        self.label_14.setBuddy(self.horizontalSlider_7)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)

        self.controlTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Wen Wenyu and Her Fathers 2.0", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7528\u4e8e\u5bf9\u4efb\u610f\u56fe\u50cf\u8fdb\u884cRoI\u6846\u9009\u4ee5\u53ca\u901a\u9053\u5206\u79bb", None))
        self.tab1OpenImgButton.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u56fe\u7247", None))
        self.tab1ChannelGroup.setTitle(QCoreApplication.translate("Dialog", u"\u989c\u8272\u901a\u9053", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"All", None))
        self.radioButton_4.setText(QCoreApplication.translate("Dialog", u"Red", None))
        self.radioButton_3.setText(QCoreApplication.translate("Dialog", u"Green", None))
        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Blue", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u9009\u9879", None))
        self.tab1SaveButton.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u56fe\u7247", None))
        self.tab1AddLineCheck.setTitle(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u6807\u5c3a", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"From", None))
        self.from_edit.setText(QCoreApplication.translate("Dialog", u"100.0", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"um", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"To", None))
        self.to_edit.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"um", None))
        self.tab1SaveAllCheckBox.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58ROI\u5168\u901a\u9053", None))
        self.tab1SaveEachCheckBox.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58ROI\u5404\u901a\u9053", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"B/C", None))
        self.tab1Hist.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.tab1ParaGroup.setTitle(QCoreApplication.translate("Dialog", u"\u4eae\u5ea6/\u5bf9\u6bd4\u5ea6\u53c2\u6570", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"\u5404\u901a\u9053\u5171\u4eab\u53c2\u6570", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"\u5404\u901a\u9053\u72ec\u7acb\u53c2\u6570", None))
        self.tab1BCBar.setTitle(QCoreApplication.translate("Dialog", u"GroupBox", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Min", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Max", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Bright", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Contrast", None))
        self.controlTabWidget.setTabText(self.controlTabWidget.indexOf(self.tab1), QCoreApplication.translate("Dialog", u"RoI\u533a\u57df\u6846\u9009", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u7528\u4e8e\u5bf9\u56fe\u50cf\u8fdb\u884c\u970d\u592b\u5706\u8ba1\u6570", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb\u8ba1\u6570", None))
        self.controlTabWidget.setTabText(self.controlTabWidget.indexOf(self.tab2), QCoreApplication.translate("Dialog", u"\u970d\u592b\u5706\u8ba1\u6570", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u7528\u4e8e\u5bf9\u80f6\u56fe\u8fdb\u884c\u9762\u79ef\u8ba1\u7b97", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u5f00\u59cb\u8ba1\u6570", None))
        self.controlTabWidget.setTabText(self.controlTabWidget.indexOf(self.tab3), QCoreApplication.translate("Dialog", u"\u80f6\u56fe\u7b97\u7070\u5ea6", None))
    # retranslateUi

