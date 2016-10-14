__author__ = 'jvelez'

from PyQt4 import QtGui

from Navigator_ui import Ui_Navigator


class Navigator(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Navigator()
        self.ui.setupUi(self)

