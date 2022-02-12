from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import numpy as np
import time
import cv2
import os

#User modules import
from scripts_jetsonnano_to_database import *

BASE_DIR = os.getcwd()
IMAGE_DIR = os.path.join(BASE_DIR, 'tmp')

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('UI_NCKH_2022.ui', self)
    #    self.showFullScreen()

        self.thread = {}
        self.activate_camera_thread()
        self.activate_test_thread()
        self.activate_test_thread_1()

    def activate_test_thread(self):
        self.thread[1] = TestThread(parent=None)
        self.thread[1].start()

    def activate_test_thread_1(self):
        self.thread[3] = TestThread1(parent=None)
        self.thread[3].start()

    def activate_camera_thread(self):
        self.thread[2] = VideoThread()
        print(self.thread[2])
        self.thread[2].change_pixmap_signal.connect(self.update_image)
        self.thread[2].start()

    @QtCore.pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.cameraFrame.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(
            rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(800, 611, QtCore.Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


class VideoThread(QtCore.QThread):
    change_pixmap_signal = QtCore.pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False

        # self.wait()


class TestThread(QtCore.QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._run_flag = True

    def run(self):
        os.chdir(IMAGE_DIR)
        print('Start Thread Test')
        while True:
            if os.listdir(IMAGE_DIR):
                img_name = os.listdir(IMAGE_DIR)[0]
                print(img_name)
                img_data = img_name.split('.')[0]
                img_data = img_data.split('_')
                #insert_log_database(img_data[0], img_data[1], img_data[2], img_data[3], img_data[4], img_name)
                insert_log_database(105180292, img_data[1], img_data[2], img_data[3], img_data[4], img_name)
                print(img_data)
                img_path = os.path.join(IMAGE_DIR, img_name)
                os.remove(img_path)

    def stop(self):
        self._run_flag = False


class TestThread1(QtCore.QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._run_flag = True

    def run(self):
        print('Start Thread Test 2....')
        while True:
            pass

    def stop(self):
        self._run_flag = False


app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())
