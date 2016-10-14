# -*- coding: utf-8 -*-
__author__ = 'Rainer Arencibia'
import PyQt4
import numpy as np

import cv2
from PyQt4.QtCore import QString
from PyQt4.QtGui import QColor, QPen, QBrush

from Histograms import Ui_Histograms

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

class WindowHistogram(PyQt4.QtGui.QDialog):
    """
    This class will show a new window for the histograms calculated.
    """
    def __init__(self, parent=None):
        """
        :param parent: This window do NOT have a parent.
        :return: show a new window.
        """
        PyQt4.QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Histograms()
        self.ui.setupUi(self)
        self.setFixedSize(self.width(), self.height())


class HistogramBuilder:
    """
    The class implements a lot´s methods, some with the intention to calculate the histograms of an image.
    Other show the results on the window, using some methods from PyQt4 to draw lines & rectangles.
    We have some (slots & methods) for the signals received from the window.
    """
    def __init__(self, img):
        """
        :param img: an image or a video frame.
        :return: the information calculated from the different histograms in a window.
        """
        img_read = cv2.imread(img)
        self.image = cv2.cvtColor(img_read, cv2.COLOR_BGR2RGB)  # we change the format of the image.

        self.height = self.image.shape[0]
        self.width = self.image.shape[1]
        self.size = self.image.size
        self.num_pixels = self.width * self.height

        self.r_hist = np.zeros_like(self.image)  # arrays that will contain the histogram calculated.
        self.g_hist = np.zeros_like(self.image)
        self.b_hist = np.zeros_like(self.image)
        self.h_hist = np.zeros_like(self.image)
        self.s_hist = np.zeros_like(self.image)
        self.v_hist = np.zeros_like(self.image)

        self.color_bool = False  # True: if the image received it´s a color image.
        self.gray_bool = False  # True: if the image received it´s a gray image.

        (r, g, b) = cv2.split(self.image)
        if np.array_equal(r, g) and np.array_equal(r, b):
            self.gray_bool = True
            self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        else:
            self.color_bool = True
            self.hsv_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2HSV)

        self.window_histogram = WindowHistogram()  # we create the window & connects the signals and slots.
        self.connect_all_checkbox()
        """ we save the size of the window, we need this lines to draw in future steps"""
        self.scene_h = self.window_histogram.sizeHint().height() - int(0.10 * self.window_histogram.sizeHint().height())
        self.scene_w = self.window_histogram.sizeHint().width() - int(0.10 * self.window_histogram.sizeHint().width())

    def connect_all_checkbox(self):
        """
        Just connect the signals with the slots.
        """
        PyQt4.QtCore.QObject.connect(self.window_histogram.ui.redCheckBox, PyQt4.QtCore.SIGNAL('stateChanged(int)'),
                                     self.on_redCheckBox_stateChanged)
        PyQt4.QtCore.QObject.connect(self.window_histogram.ui.greenCheckBox, PyQt4.QtCore.SIGNAL('stateChanged(int)'),
                                     self.on_greenCheckBox_stateChanged)
        PyQt4.QtCore.QObject.connect(self.window_histogram.ui.blueCheckBox, PyQt4.QtCore.SIGNAL('stateChanged(int)'),
                                     self.on_blueCheckBox_stateChanged)
        PyQt4.QtCore.QObject.connect(self.window_histogram.ui.hueCheckBox, PyQt4.QtCore.SIGNAL('stateChanged(int)'),
                                     self.on_hueCheckBox_stateChanged)
        PyQt4.QtCore.QObject.connect(self.window_histogram.ui.saturationCheckBox,
                                     PyQt4.QtCore.SIGNAL('stateChanged(int)'),
                                     self.on_saturationCheckBox_stateChanged)
        PyQt4.QtCore.QObject.connect(self.window_histogram.ui.valueCheckBox, PyQt4.QtCore.SIGNAL('stateChanged(int)'),
                                     self.on_valueCheckBox_stateChanged)
        PyQt4.QtCore.QObject.connect(self.window_histogram.ui.scaleComboBox,
                                     PyQt4.QtCore.SIGNAL('currentIndexChanged(int)'),
                                     self.on_scaleComboBox_currentIndexChanged)

    def draw_256_range(self, scene):
        """
        :param scene: QGraphicsView, we will paint on this.
        :return: scene but with a numbers bar on the bottom from 0 to 255.
        """
        val = 0
        step_w = self.scene_w / 8.0

        for pos in range(0, 9):
            x = float(pos) * step_w
            text = QString.number(val)
            text_item = scene.addText(text)
            text_item.setPos(int(x) - 10, self.scene_h)
            val += 256 / 8

    def draw_1_range(self, scene):
        """
        :param scene: QGraphicsView, we will paint on this.
        :return: scene but with a numbers bar on the bottom from 0.0 to 1.0.
        """
        val = 0
        step_w = self.scene_w / 8.0

        for pos in range(0, 9):
            x = float(pos) * step_w
            text = '%.2f' % (val / 80.0)
            text_item = scene.addText(text)
            text_item.setPos(int(x) - 10, self.scene_h)
            val += 10

    def draw_360_range(self, scene):
        """
        :param scene: QGraphicsView, we will paint on this.
        :return: scene but with a numbers bar on the bottom from 0 to 360.
        """
        val = 0
        step_w = self.scene_w / 8.0

        for pos in range(0, 9):
            x = float(pos) * step_w
            text = QString.number(val)
            text_item = scene.addText(text)
            text_item.setPos(int(x) - 10, self.scene_h)
            val += 365 / 8

    # draw the HUE range of values.
    def draw_hue_range(self, scene):
        """
        :param scene: QGraphicsView, we will paint on this.
        :return: scene but with a HUE color bar on the bottom.
        """
        for pos in range(0, self.scene_w + 1):
            color = pos * 255 / self.scene_w
            pen = PyQt4.QtGui.QPen(QColor(color, 255, 255))
            scene.addLine(float(pos), self.scene_h + 4, float(pos), self.scene_h + 12, pen)

    # draw an underline with black and white colors.
    def draw_value_range(self, scene):
        """
        :param scene: QGraphicsView, we will paint on this.
        :return: scene but with a VALUE color bar on the bottom.
        """
        for pos in range(0, self.scene_w + 1):
            bright = pos * 255 / self.scene_w
            pen = PyQt4.QtGui.QPen(QColor(bright, bright, bright))
            scene.addLine(float(pos), self.scene_h + 4, float(pos), self.scene_h + 12, pen)

    def draw_grid(self, scene):
        """
        :param scene: QGraphicsView, we will paint on this.
        :return: scene but with a grid painted.
        """
        grey = PyQt4.QtGui.QPen(QColor(200, 200, 200))

        step_w = self.scene_w / 8.0
        step_h = self.scene_h / 8.0

        for pos in range(0, 9):
            x = pos * step_w
            y = pos * step_h
            scene.addLine(float(x), 0.0, float(x), self.scene_h, grey)  # draw the vertical lines on the grid
            scene.addLine(0.0, float(y), self.scene_w, float(y), grey)  # draw the horizontal lines on the grid.

        index = self.window_histogram.ui.scaleComboBox.currentIndex()

        if index == 0:
            self.draw_value_range(scene)
        elif index == 1:
            self.draw_256_range(scene)
        elif index == 2:
            self.draw_hue_range(scene)
        elif index == 3:
            self.draw_360_range(scene)
        else:
            self.draw_1_range(scene)

    def draw_lines(self, scene):
        """
        :param scene: QGraphicsView, we will paint on this.
        :return: scene but with the lines of the colors selected on the window histogram.
        """
        step_w = max(1.0, self.scene_w / 256.0)

        red = PyQt4.QtGui.QPen(QColor(255, 0, 0))
        red.setWidthF(step_w)
        green = PyQt4.QtGui.QPen(QColor(0, 255, 0))
        green.setWidthF(step_w)
        blue = PyQt4.QtGui.QPen(QColor(0, 0, 255))
        blue.setWidthF(step_w)
        hue = PyQt4.QtGui.QPen(QColor(255, 0, 128))
        hue.setWidthF(step_w)
        saturation = PyQt4.QtGui.QPen(QColor(255, 128, 0))
        saturation.setWidthF(step_w)
        value = PyQt4.QtGui.QPen(QColor(0, 0, 0))
        value.setWidthF(step_w)

        draw_red = self.window_histogram.ui.redCheckBox.isChecked() and self.r_hist.max() > 0
        draw_green = self.window_histogram.ui.greenCheckBox.isChecked() and self.g_hist.max() > 0
        draw_blue = self.window_histogram.ui.blueCheckBox.isChecked() and self.b_hist.max() > 0
        draw_hue = self.window_histogram.ui.hueCheckBox.isChecked() and self.h_hist.max() > 0
        draw_saturation = self.window_histogram.ui.saturationCheckBox.isChecked() and self.s_hist.max() > 0
        draw_value = self.window_histogram.ui.valueCheckBox.isChecked() and self.v_hist.max() > 0

        if draw_red or draw_green or draw_blue or draw_hue or draw_saturation or draw_value:
            x = 0
            while x < self.scene_w + 1:
                i1 = min(255.0, max(0.0, x * 255.0 / self.scene_w))
                i2 = min(255.0, max(0.0, (x + step_w) * 255.0 / self.scene_w))

                if draw_red:
                    scene.addLine(x, self.scene_h - self.scene_h * self.r_hist[i1], x + step_w,
                                  self.scene_h - self.scene_h * self.r_hist[i2], red)
                if draw_green:
                    scene.addLine(x, self.scene_h - self.scene_h * self.g_hist[i1], x + step_w,
                                  self.scene_h - self.scene_h * self.g_hist[i2], green)
                if draw_blue:
                    scene.addLine(x, self.scene_h - self.scene_h * self.b_hist[i1], x + step_w,
                                  self.scene_h - self.scene_h * self.b_hist[i2], blue)
                if draw_hue:
                    i1 = min(180.0, max(0.0, x * 180.0 / self.scene_w))
                    i2 = min(180.0, max(0.0, (x + step_w) * 180.0 / self.scene_w))
                    scene.addLine(x, self.scene_h - self.scene_h * self.h_hist[i1], x + step_w,
                                  self.scene_h - self.scene_h * self.h_hist[i2], hue)
                if draw_saturation:
                        scene.addLine(x, self.scene_h - self.scene_h * self.s_hist[i1], x + step_w,
                                      self.scene_h - self.scene_h * self.s_hist[i2], saturation)
                if draw_value:
                        scene.addLine(x, self.scene_h - self.scene_h * self.v_hist[i1], x + step_w,
                                      self.scene_h - self.scene_h * self.v_hist[i2], value)
                x += step_w

    def draw_bars(self, scene):
        """
        :param scene: QGraphicsView, we will paint on this.
        :return: scene, if the image is bitonal draw a pair of rectangles with
        the percentage of white and black pixels.
        """
        draw_value = self.window_histogram.ui.valueCheckBox.isChecked() and self.v_hist.any() > 0.0

        if draw_value:
            bar1 = self.scene_h * self.v_hist[0]
            bar2 = self.scene_h * self.v_hist[255]

            pen = QPen(QColor(128, 128, 128))
            brush_white = QBrush(QColor(225, 225, 225))
            brush_black = QBrush(QColor(25, 25, 25))

            scene.addRect(0, self.scene_h - bar1, self.scene_w / 2, bar1, pen, brush_black)
            scene.addRect(self.scene_w / 2, self.scene_h - bar2, self.scene_w / 2, bar2, pen, brush_white)

            total = self.v_hist[0] + self.v_hist[255]
            result_0 = '%.0f' % (100 * self.v_hist[0] / total[0])
            result_255 = '%.0f' % (100 * self.v_hist[255] / total[0])

            black = str(result_0) + '%'
            white = str(result_255) + '%'

            scene.addText(black).setPos(self.scene_w / 4, self.scene_h)
            scene.addText(white).setPos(3 * self.scene_w / 4, self.scene_h)

    def draw_histograms(self):
        """
        Make an new QGraphicsScene (scene) and send it to painted.
        :return: if we have a bitonal image, we will paint rectangles.
                 if not we gonna draw lines on the scene.
                 But first we draw the grid.
        """
        self.scene_h = self.window_histogram.sizeHint().height() - int(0.10 * self.window_histogram.sizeHint().height())
        self.scene_w = self.window_histogram.sizeHint().width() - int(0.10 * self.window_histogram.sizeHint().width())
        scene = PyQt4.QtGui.QGraphicsScene(0, 0, self.scene_w, self.scene_h)
        self.window_histogram.ui.graphicsView.setScene(scene)

        if self.gray_bool and self.is_bitonal():
            self.draw_bars(scene)
        else:
            self.draw_grid(scene)
            self.draw_lines(scene)

    def is_bitonal(self):
        """
        :return: True if an image is bitonal. This types of image only have 0(black) or 255(white) on the pixels value.
        So we check the value histogram array, and only ask for the first and last position.
        If the sum of this positions is the number of pixels of the image, we have a bitonal image.
        """
        return self.v_hist[0] + self.v_hist[255] == self.num_pixels

    def compute_red_histogram(self):
        """
        Input: Color Image.
        :return: self.r_hist, calculated the red histogram(normalize) of a color image.
        """
        self.r_hist = cv2.calcHist([self.image], [0], None, [256], [0, 256])
        cv2.normalize(self.r_hist, self.r_hist, 0, 1, cv2.NORM_MINMAX)

    def compute_green_histogram(self):
        """
        Input: Color Image.
        :return: self.g_hist, calculated the green histogram(normalize) of a color image.
        """
        self.g_hist = cv2.calcHist([self.image], [1], None, [256], [0, 256])
        cv2.normalize(self.g_hist, self.g_hist, 0, 1, cv2.NORM_MINMAX)

    def compute_blue_histogram(self):
        """
        Input: Color Image.
        :return: self.b_hist, calculated the blue histogram(normalize) of a color image.
        """
        self.b_hist = cv2.calcHist([self.image], [2], None, [256], [0, 256])
        cv2.normalize(self.b_hist, self.b_hist, 0, 1, cv2.NORM_MINMAX)

    def compute_hue_histogram(self):
        """
        Input: Color Image.
        :return: self.h_hist, calculated the hue histogram(normalize) of a color image.
        """
        self.h_hist = cv2.calcHist([self.hsv_image], [0], None, [256], [0, 180])
        cv2.normalize(self.h_hist, self.h_hist, 0, 1, cv2.NORM_MINMAX)

    def compute_saturation_histogram(self):
        """
        Input: Color Image.
        :return: self.s_hist, calculated the saturation histogram(normalize) of a color image.
        """
        self.s_hist = cv2.calcHist([self.hsv_image], [1], None, [256], [0, 256])
        cv2.normalize(self.s_hist, self.s_hist, 0, 1, cv2.NORM_MINMAX)

    def compute_value_histogram(self):
        """
        Input: Color / Gray Image.
        :return: self.v_hist,
        IF it´s a gray image calculated the value histogram("equalize" & normalize).
        IF it´s a color image calculated the value histogram(normalize).
        """
        if self.gray_bool:
            equalize_gray_image = cv2.equalizeHist(self.image)
            self.v_hist = cv2.calcHist([equalize_gray_image], [0], None, [256], [0, 256])
        elif self.color_bool:
            self.v_hist = cv2.calcHist([self.hsv_image], [2], None, [256], [0, 256])
        cv2.normalize(self.v_hist, self.v_hist, 0, 1, cv2.NORM_MINMAX)

    def compute_histograms(self):
        """
        :return: If we have an image with at least one pixel, we send it to process.
        If it´s a color image, do all of the histograms.
        If it´s a gray scale image only will calculate the value histogram "equalize"
        """
        if self.num_pixels > 0:
            if self.r_hist.max() == 0 and self.color_bool:
                self.compute_red_histogram()
            if self.g_hist.max() == 0 and self.color_bool:
                self.compute_green_histogram()
            if self.b_hist.max() == 0 and self.color_bool:
                self.compute_blue_histogram()
            if self.h_hist.max() == 0 and self.color_bool:
                self.compute_hue_histogram()
            if self.s_hist.max() == 0 and self.color_bool:
                self.compute_saturation_histogram()
            if self.v_hist.max() == 0:
                self.compute_value_histogram()

    def on_redCheckBox_stateChanged(self):
        """
        This slot is connected automatically in connectSlotsByName
        """
        self.draw_histograms()

    def on_greenCheckBox_stateChanged(self):
        """
        This slot is connected automatically in connectSlotsByName
        """
        self.draw_histograms()

    def on_blueCheckBox_stateChanged(self):
        """
        This slot is connected automatically in connectSlotsByName
        """
        self.draw_histograms()

    def on_hueCheckBox_stateChanged(self):
        """
        This slot is connected automatically in connectSlotsByName
        """
        self.draw_histograms()

    def on_saturationCheckBox_stateChanged(self):
        """
        This slot is connected automatically in connectSlotsByName
        """
        self.draw_histograms()

    def on_valueCheckBox_stateChanged(self):
        """
        This slot is connected automatically in connectSlotsByName
        """
        self.draw_histograms()

    def on_scaleComboBox_currentIndexChanged(self):
        """
        This slot is connected automatically in connectSlotsByName
        """
        self.draw_histograms()

    def update_panel_to_image(self, img):
        if self.window_histogram.isVisible():
            self.__init__(img)
            self.compute_histograms()
            self.draw_histograms()

    def keyPressEvent(self, e):
        """
        This slot is connected automatically in connectSlotsByName
        """
        if e.key() == PyQt4.QtCore.Qt.Key_Escape:
            self.window_histogram.close()

    """ Know the value of a pixel of a color image.
        (r, g, b) = self.image[0, 0]
        print "Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b)
    """