# -*- coding: utf-8 -*-
__author__ = 'Rainer Arencibia'
import logging
import numpy as np
import time
from PyQt4 import QtGui, QtCore

import cv2
from PyQt4.QtCore import QObject

from Configurator import Ui_ConfiguratorWidget

"""
The MIT License (MIT)

Copyright (c) 2016 Rainer Arencibia

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

class WindowBuilder(QtGui.QDialog):
    """
    This class it´s the window for the builder,
    object that allow us to select and change the settings
    for the Gaussian blur filter.
    """
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_ConfiguratorWidget()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())


class GaussianBlurBuilder:
    """
    This class it´s the GaussianBlur builder, witch receive an image in color or gray and
    :return a blur image as the result to apply the Gaussian blur function to the original image.
    """

    def __init__(self, img):
        """
        :param img: receive a picture/video frame
        :return: self.dst_image, an image with only the edges of objects of image received.
        """
        self.image = cv2.imread(img)
        self.dst_image = np.zeros_like(self.image)
        self.size = (0, 0)
        self.sigmaX = 0
        self.sigmaY = 0

        self.window_builder = WindowBuilder()
        QObject.connect(self.window_builder.ui.sliderX, QtCore.SIGNAL('valueChanged(int)'), self.sliderSize1)
        QObject.connect(self.window_builder.ui.sliderY, QtCore.SIGNAL('valueChanged(int)'), self.sliderSize2)
        QObject.connect(self.window_builder.ui.sliderX_sigma, QtCore.SIGNAL('valueChanged(int)'), self.sliderX)
        QObject.connect(self.window_builder.ui.sliderY_sigma, QtCore.SIGNAL('valueChanged(int)'), self.sliderY)
        QObject.connect(self.window_builder.ui.apply_btn, QtCore.SIGNAL('clicked()'), self.apply)

    def apply(self):
        self.gaussian_blur()
        self.window_builder.close()

    def sliderSize1(self, value):
        """
        :param value: will be the number selected by the user for the width. value have to be positive and odd.
        :return: save the value selected by the user in self.size(X,_).
        """
        if value > 0 and value % 2 == 0:
            value += 1
        self.size = (value, self.size[1])

    def sliderSize2(self, value):
        """
        :param value: will be the number selected by the user for the height. value have to be positive and odd.
        :return: save the value selected by the user in self.size(_,X).
        """
        if value > 0 and value % 2 == 0:
            value += 1
        self.size = (self.size[0], value)

    def sliderX(self, value):
        """
        :param value: will be the number selected by the user for Sigma X.
        :return: save the value selected by the user in self.sigmaX.
        """
        self.sigmaX = value/3

    def sliderY(self, value):
        """
        :param value: will be the number selected by the user for Sigma Y.
        :return: save the value selected by the user in self.sigmaY.
        """
        self.sigmaY = value/3

    def gaussian_blur(self):
        """ The gaussian_blur method apply the Gaussian Blur algorithms to the image received on __init__
        :return: an image with the blur effect on it, with setting by default.
        If the user select some setting call a private method __gaussian_blur2
        to do the same process with the new values.
        """
        if self.matrix_size_not_zeros() and self.sigma_x_y_not_zeros():
            self.dst_image = cv2.GaussianBlur(self.image, self.size, self.sigmaX, self.sigmaY)
            return self.dst_image
        elif self.matrix_size_not_zeros():
            self.dst_image = cv2.GaussianBlur(self.image, self.size, 1)
            return self.dst_image
        elif self.sigma_x_y_not_zeros():
            self.dst_image = cv2.GaussianBlur(self.image, None, self.sigmaX, self.sigmaY)
            return self.dst_image
        else:
            logging.info(''.join([' ', str(time.asctime(time.localtime(time.time()))), ' : ',
                                  'Gaussian Blur Filter. Need more parameters.']))
            self.window_builder.ui.info_label.setStyleSheet("QLabel{background-color : yellow;}")

    def matrix_size_not_zeros(self):
        return self.size[0] != 0 and self.size[1] != 0

    def sigma_x_y_not_zeros(self):
        return self.sigmaX != 0 and self.sigmaY != 0

