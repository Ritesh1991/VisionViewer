# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Configurator.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_ConfiguratorWidget(object):
    def setupUi(self, ConfiguratorWidget):
        ConfiguratorWidget.setObjectName(_fromUtf8("ConfiguratorWidget"))
        ConfiguratorWidget.resize(394, 304)
        self.gaussian_frame = QtGui.QFrame(ConfiguratorWidget)
        self.gaussian_frame.setGeometry(QtCore.QRect(0, 0, 421, 331))
        self.gaussian_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.gaussian_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gaussian_frame.setObjectName(_fromUtf8("gaussian_frame"))
        self.size_label = QtGui.QLabel(self.gaussian_frame)
        self.size_label.setGeometry(QtCore.QRect(20, 30, 231, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.size_label.setFont(font)
        self.size_label.setObjectName(_fromUtf8("size_label"))
        self.x_label = QtGui.QLabel(self.gaussian_frame)
        self.x_label.setGeometry(QtCore.QRect(20, 70, 41, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.x_label.setFont(font)
        self.x_label.setObjectName(_fromUtf8("x_label"))
        self.y_label = QtGui.QLabel(self.gaussian_frame)
        self.y_label.setGeometry(QtCore.QRect(20, 110, 41, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.y_label.setFont(font)
        self.y_label.setObjectName(_fromUtf8("y_label"))
        self.sliderX = QtGui.QSlider(self.gaussian_frame)
        self.sliderX.setGeometry(QtCore.QRect(70, 90, 160, 22))
        self.sliderX.setOrientation(QtCore.Qt.Horizontal)
        self.sliderX.setObjectName(_fromUtf8("sliderX"))
        self.sliderY = QtGui.QSlider(self.gaussian_frame)
        self.sliderY.setGeometry(QtCore.QRect(70, 130, 160, 22))
        self.sliderY.setOrientation(QtCore.Qt.Horizontal)
        self.sliderY.setObjectName(_fromUtf8("sliderY"))
        self.sigmas_label = QtGui.QLabel(self.gaussian_frame)
        self.sigmas_label.setGeometry(QtCore.QRect(10, 160, 211, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.sigmas_label.setFont(font)
        self.sigmas_label.setObjectName(_fromUtf8("sigmas_label"))
        self.sigma_x_label = QtGui.QLabel(self.gaussian_frame)
        self.sigma_x_label.setGeometry(QtCore.QRect(20, 200, 41, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.sigma_x_label.setFont(font)
        self.sigma_x_label.setObjectName(_fromUtf8("sigma_x_label"))
        self.sigma_y_label = QtGui.QLabel(self.gaussian_frame)
        self.sigma_y_label.setGeometry(QtCore.QRect(20, 240, 41, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.sigma_y_label.setFont(font)
        self.sigma_y_label.setObjectName(_fromUtf8("sigma_y_label"))
        self.sliderX_sigma = QtGui.QSlider(self.gaussian_frame)
        self.sliderX_sigma.setGeometry(QtCore.QRect(70, 220, 160, 22))
        self.sliderX_sigma.setOrientation(QtCore.Qt.Horizontal)
        self.sliderX_sigma.setObjectName(_fromUtf8("sliderX_sigma"))
        self.sliderY_sigma = QtGui.QSlider(self.gaussian_frame)
        self.sliderY_sigma.setGeometry(QtCore.QRect(70, 250, 160, 22))
        self.sliderY_sigma.setOrientation(QtCore.Qt.Horizontal)
        self.sliderY_sigma.setObjectName(_fromUtf8("sliderY_sigma"))
        self.apply_btn = QtGui.QPushButton(self.gaussian_frame)
        self.apply_btn.setGeometry(QtCore.QRect(270, 250, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.apply_btn.setFont(font)
        self.apply_btn.setObjectName(_fromUtf8("apply_btn"))
        self.info_label = QtGui.QLabel(self.gaussian_frame)
        self.info_label.setGeometry(QtCore.QRect(20, 10, 351, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.info_label.setFont(font)
        self.info_label.setObjectName(_fromUtf8("info_label"))

        self.retranslateUi(ConfiguratorWidget)
        QtCore.QMetaObject.connectSlotsByName(ConfiguratorWidget)

    def retranslateUi(self, ConfiguratorWidget):
        ConfiguratorWidget.setWindowTitle(_translate("ConfiguratorWidget", "Gaussian Configurator", None))
        self.size_label.setText(_translate("ConfiguratorWidget", "Matrix Size: (X, Y) ", None))
        self.x_label.setText(_translate("ConfiguratorWidget", " X:", None))
        self.y_label.setText(_translate("ConfiguratorWidget", " Y:", None))
        self.sigmas_label.setText(_translate("ConfiguratorWidget", " Sigmas Value: X, Y", None))
        self.sigma_x_label.setText(_translate("ConfiguratorWidget", " X:", None))
        self.sigma_y_label.setText(_translate("ConfiguratorWidget", " Y:", None))
        self.apply_btn.setText(_translate("ConfiguratorWidget", "Apply", None))
        self.info_label.setText(_translate("ConfiguratorWidget", " At least have to select one of the two fields.", None))

