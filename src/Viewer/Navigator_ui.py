# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Navigator.ui'
#
# Created: Sat Jun 13 11:45:07 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Navigator(object):
    def setupUi(self, Navigator):
        Navigator.setObjectName(_fromUtf8("Navigator"))
        Navigator.resize(536, 389)
        self.gridLayout = QtGui.QGridLayout(Navigator)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.imageTree = QtGui.QTreeWidget(Navigator)
        self.imageTree.setHeaderHidden(False)
        self.imageTree.setColumnCount(2)
        self.imageTree.setObjectName(_fromUtf8("imageTree"))
        self.imageTree.header().setDefaultSectionSize(294)
        self.gridLayout.addWidget(self.imageTree, 3, 0, 1, 1)
        self.frame = QtGui.QFrame(Navigator)
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setMargin(1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.firstButton = QtGui.QToolButton(self.frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/Resources/first.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.firstButton.setIcon(icon)
        self.firstButton.setObjectName(_fromUtf8("firstButton"))
        self.horizontalLayout.addWidget(self.firstButton)
        self.prevButton = QtGui.QToolButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/Resources/prev.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevButton.setIcon(icon1)
        self.prevButton.setObjectName(_fromUtf8("prevButton"))
        self.horizontalLayout.addWidget(self.prevButton)
        self.imageNumEdit = QtGui.QLineEdit(self.frame)
        self.imageNumEdit.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageNumEdit.sizePolicy().hasHeightForWidth())
        self.imageNumEdit.setSizePolicy(sizePolicy)
        self.imageNumEdit.setBaseSize(QtCore.QSize(0, 0))
        self.imageNumEdit.setObjectName(_fromUtf8("imageNumEdit"))
        self.horizontalLayout.addWidget(self.imageNumEdit)
        self.nextButton = QtGui.QToolButton(self.frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/Resources/next.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon2)
        self.nextButton.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.lastButton = QtGui.QToolButton(self.frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/Resources/last.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lastButton.setIcon(icon3)
        self.lastButton.setObjectName(_fromUtf8("lastButton"))
        self.horizontalLayout.addWidget(self.lastButton)
        self.imageNumSlider = QtGui.QSlider(self.frame)
        self.imageNumSlider.setMinimum(1)
        self.imageNumSlider.setMaximum(1)
        self.imageNumSlider.setTracking(True)
        self.imageNumSlider.setOrientation(QtCore.Qt.Horizontal)
        self.imageNumSlider.setObjectName(_fromUtf8("imageNumSlider"))
        self.horizontalLayout.addWidget(self.imageNumSlider)
        self.imageTotallabel = QtGui.QLabel(self.frame)
        self.imageTotallabel.setObjectName(_fromUtf8("imageTotallabel"))
        self.horizontalLayout.addWidget(self.imageTotallabel)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.actionNextImage = QtGui.QAction(Navigator)
        self.actionNextImage.setObjectName(_fromUtf8("actionNextImage"))

        self.retranslateUi(Navigator)
        QtCore.QMetaObject.connectSlotsByName(Navigator)

    def retranslateUi(self, Navigator):
        Navigator.setWindowTitle(_translate("Navigator", "Navigator", None))
        self.imageTree.headerItem().setText(0, _translate("Navigator", "Name", None))
        self.imageTree.headerItem().setText(1, _translate("Navigator", "Properties", None))
        self.firstButton.setText(_translate("Navigator", "...", None))
        self.prevButton.setText(_translate("Navigator", "...", None))
        self.nextButton.setText(_translate("Navigator", "...", None))
        self.lastButton.setText(_translate("Navigator", "...", None))
        self.imageTotallabel.setText(_translate("Navigator", "0", None))
        self.actionNextImage.setText(_translate("Navigator", "nextImage", None))

