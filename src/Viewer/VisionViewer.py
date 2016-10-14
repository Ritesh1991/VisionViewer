# -*- coding: utf-8 -*-
__author__ = 'José Francisco Velez & Rainer Arencibia'
import logging
import numpy as np
import os
import sys
import time
from PyQt4 import QtCore, QtGui

import cv2

from ViewerWindow_uy import Ui_ViewerWindow
from WindowAboutus import Ui_Dialog
from src.Builders.Canny.CannyBuilder import CannyBuilder
from src.Builders.GaussianBlur.GaussianBlurBuilder import GaussianBlurBuilder
from src.Builders.Histogram.HistogramBuilder import HistogramBuilder

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


class WindowAboutus(QtGui.QMainWindow):
    """
    This window will show information about this application, developer & info related it.
    """
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())


class ViewerWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_ViewerWindow()
        self.ui.setupUi(self)
        self.ui.graphicsView.setMouseTracking(True)
        self.ui.graphicsView.mousePressEvent = self.mouse_press_event_viewer
        self.ui.preview.mousePressEvent = self.mouse_press_event_preview

        # New Windows ABOUT-US Code by Rainer
        self.window_aboutus = WindowAboutus()
        # when click in apply, the image in preview tab will go to the viewer tab.
        # On this moment we saved because if the user want to save the result
        # it´s easier. check: def on_actionSave_Image_triggered(self):
        self.image_viewer = None  # image loaded on the viewer tab
        self.image_preview = None  # the result image loaded on the preview tab
        self.url = ''
        self.start = time.time()
        self.timer = QtCore.QTimer()
        self.timer.connect(self.timer, QtCore.SIGNAL('timeout()'), self.display_time_elapsed)
        self.timer.start(1000)

    def mouse_press_event_viewer(self, event):
        position = QtCore.QPoint(event.pos().x(), event.pos().y())
        image = self.to_qimage(self.image_viewer)
        color = QtGui.QColor.fromRgb(image.pixel(position))

        if color.isValid():
            self.ui.coordsLabel.setText(' '.join([str(event.pos().x()), 'x', str(event.pos().y())]))
            self.ui.valueLabel.setText('RGB: ' + ' '.join([str(color.red()), 'x', str(color.green()), 'x', str(color.blue())]))
            self.ui.zoomLabel.setText(str(1.0))

    def mouse_press_event_preview(self, event):
        position = QtCore.QPoint(event.pos().x(), event.pos().y())
        image = self.to_qimage(self.image_preview)
        color = QtGui.QColor.fromRgb(image.pixel(position))

        if color.isValid():
            self.ui.coordsLabel.setText(' '.join([str(event.pos().x()), 'x', str(event.pos().y())]))
            self.ui.valueLabel.setText('RGB: ' + ' '.join([str(color.red()), 'x', str(color.green()), 'x', str(color.blue())]))
            self.ui.zoomLabel.setText(str(1.0))

    def display_time_elapsed(self):
        secs = time.time() - self.start
        minutes = (secs / 60) % 60
        hours = (secs / 3600)
        secs %= 60
        self.ui.elapsedTime.setText(''.join([str('%02d' % int(hours)), ':', str('%02d' % int(minutes)), ':',
                                             str('%02d' % int(secs))]))

    @QtCore.pyqtSlot()
    def on_actionHistogram_triggered(self):
        """
        This method and slot will generate a histogram of a Color, Gray or Bitonal image.
        :return: Will show a new window with the Histogram information.
        """
        if self.url == '':
            fd = QtGui.QFileDialog(self)
            self.url = str(fd.getOpenFileName(self, 'Open an image or a video file',
                                              '/',
                                              "Images (*.bmp *.dib *.jpeg *.jpe *.jpg *.pbm *.pgm *.png *.ppm *.ras *.sr)"
                                              ";;Videos (*.avi *flv *mp4 *mpeg *mpg *m4v *wmv)"
                                              'Choose your file'))

        self.drawImageViewer(self.url)
        builder = HistogramBuilder(self.url)
        builder.compute_histograms()
        builder.draw_histograms()
        builder.window_histogram.show()
        builder.window_histogram.exec_()

    @QtCore.pyqtSlot()
    def on_actionGaussianBlur_triggered(self):
        """
        This method and slot will generate a new image with the gaussian blur effect on it.
        :return: Will show the new image as result of the Gaussian Blur.
        """
        if self.url == '':
            fd = QtGui.QFileDialog(self)
            self.url = str(fd.getOpenFileName(self, 'Open an image or a video file', '/',
                                          "Images (*.bmp *.dib *.jpeg *.jpe *.jpg *.pbm *.pgm *.png *.ppm *.ras *.sr)"
                                          ";;Videos (*.avi *flv *mp4 *mpeg *mpg *m4v *wmv)"
                                          'Choose your file'))

        self.drawImageViewer(self.url)
        builder = GaussianBlurBuilder(self.url)
        builder.window_builder.show()
        ''' Hay que comprobar como se puede pasar la imagen de gaussianbuilder hasta aqui. '''
        builder.window_builder.exec_()
        self.image_preview = builder.dst_image
        self.drawImagePreview(self.image_preview)

    @QtCore.pyqtSlot()
    def on_actionExit_triggered(self):
        logging.info(''.join([' ', str(time.asctime(time.localtime(time.time()))), ' : ',
                              'VisionViewer app Finished.']))
        self.close()

    @QtCore.pyqtSlot()
    def on_actionLog_2_triggered(self):
        """
        :return: Open the LOG file.
        """
        os.system("notepad.exe ./Extra/VisionViewer.log")

    @QtCore.pyqtSlot()
    def on_actionCanny_triggered(self):
        """
        This method and slot will generate a new image with the edges of the original image.
        :return: Will show the new image as result of the Canny effect depending on the setting selected by the user.
        """
        if self.url == '':
            fd = QtGui.QFileDialog(self)
            self.url = str(fd.getOpenFileName(self, 'Open an image or a video file',
                                          '/',
                                          "Images (*.bmp *.dib *.jpeg *.jpe *.jpg *.pbm *.pgm *.png *.ppm *.ras *.sr)"
                                          ";;Videos (*.avi *flv *mp4 *mpeg *mpg *m4v *wmv)"
                                          'Choose your file'))

        self.drawImageViewer(self.url)
        builder = CannyBuilder(self.url)
        dst = builder.canny()
        self.image_preview = dst
        self.drawImagePreview(dst)

    @QtCore.pyqtSlot()
    def on_actionAbout_us_triggered(self):
        """
        This method and slot will show the about us window.
        :return: a new window on the screen.
        """
        self.window_aboutus.show()

    @QtCore.pyqtSlot()
    def on_actionSave_Image_triggered(self):
        """
        This method and slot will show the about us window.
        :return: save an image if there is one in Viewer tab.
        """
        if self.image_preview is not None:
            fd = QtGui.QFileDialog(self)
            s = str(fd.getSaveFileName())
            if s is not '':
                cv2.imwrite(s, self.image_preview)
            else:
                logging.info(''.join([' ', str(time.asctime(time.localtime(time.time()))), ' : ',
                                  'There is no Name or directory to save.']))

        if self.image_preview is None:
            logging.info(''.join([' ', str(time.asctime(time.localtime(time.time()))), ' : ',
                                  'There is no image to save.']))

    @QtCore.pyqtSlot()
    def on_actionOpen_file_triggered(self):
        """
        :return: Open a photo or a video file.
        """
        fd = QtGui.QFileDialog(self)
        s = str(fd.getOpenFileName())
        self.drawImageViewer(s)
        self.image_viewer = cv2.imread(s)
        self.url = s

    def drawImageViewer(self, s):
        """
        :param s: string with the url of the picture loaded.
        :return: put the photo on the QgraphicsView
        """
        cvBGRImg = cv2.imread(s)
        cvRGBImg = cv2.cvtColor(cvBGRImg, cv2.cv.CV_BGR2RGB)
        qimg = QtGui.QImage(cvRGBImg, cvRGBImg.shape[1], cvRGBImg.shape[0], cvBGRImg.strides[0],
                            QtGui.QImage.Format_RGB888)
        qpm = QtGui.QPixmap.fromImage(qimg)
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(qpm)
        self.ui.graphicsView.setScene(scene)
        self.image_viewer = cvRGBImg

    def drawImagePreview(self, img):
        """
        :param img: the result image (numpy array).
        :return: put the image on the QgraphicsView (QImage).
        """
        q_img = self.to_qimage(img)
        qpm = QtGui.QPixmap.fromImage(q_img)
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(qpm)
        self.ui.preview.setScene(scene)
        self.image_preview = img

    def to_qimage(self, img, copy=False):
        """ Transform a image(numpy array) to a QImage.
        :param img: img is a numpy array
        :return: QImage
        """
        gray_color_table = [QtGui.qRgb(i, i, i) for i in range(256)]

        if img is None:
            return QtGui.QImage()

        if img.dtype == np.uint8:
            if len(img.shape) == 2:
                qim = QtGui.QImage(img.data, img.shape[1], img.shape[0], img.strides[0], QtGui.QImage.Format_Indexed8)
                qim.setColorTable(gray_color_table)
                return qim.copy() if copy else qim
            elif len(img.shape) == 3:
                im = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                if im.shape[2] == 3:
                    qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_RGB888)
                    return qim.copy() if copy else qim
                elif im.shape[2] == 4:
                    qim = QtGui.QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QtGui.QImage.Format_ARGB32)
                    return qim.copy() if copy else qim


def main():
    logging.basicConfig(filename='./Extra/VisionViewer.log', level=logging.DEBUG)
    with open("./Extra/VisionViewer.log", "w") as f:
        f.truncate()

    logging.info(' Type - User - Date & Time - Details')
    logging.info(''.join([' ', str(time.asctime(time.localtime(time.time()))), ' : ',
                         'VisionViewer app Started.']))
    app = QtGui.QApplication(sys.argv)
    window = ViewerWindow()
    window.display_time_elapsed()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
