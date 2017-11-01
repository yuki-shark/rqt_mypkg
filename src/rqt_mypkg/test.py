#!/usr/bin/python
import sys, time, urllib2
from PyQt4 import QtCore, QtGui, uic
import rospy
from sensor_msgs.msg import Image
import Queue

img = None
form_class = uic.loadUiType("/home/yuki/catkin_ws/tutorials/src/rqt_mypkg/resource/team1_window.ui")[0]
q = Queue.Queue()
# Load the UI

def callback(data):
	# horizontal = data.axes[2]
	# vertical = data.axes[3]
    global img
    img = data.data

def listener():
    rospy.init_node('ui', anonymous=True)
    rospy.Subscriber("/networkCam", Image, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

class OwnImageWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.image = None

    def setImage(self, image):
        self.image = image
        sz = image.size()
        self.setMinimumSize(sz)
        self.update()

    def paintEvent(self, event):
        qp = QtGui.Qpainter()
        qp.begin(self)
        if self.image:
            qp.drawImage(QtCore.QPoint(0,0), self.image)
        qp.end()


class MyWindowClass(QtGui.QMainWindow, form_class):
    global img
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        # self.startButton.clicked.connect(self.start_clicked)

        # self.window_width = self.ImgWidget.frameSize().width()
        # self.window_height = self.ImgWidget.frameSize().height()
        self.ImgWidget = OwnImageWidget(self.ImgWidget)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)


    # def start_clicked(self):
    #     global running
    #     running = True
    #     capture_thread.start()
    #     self.startButton.setEnabled(False)
    #     self.startButton.setText('Starting...')


    # def update_frame(self):
    #     if not q.empty():
    #         # self.startButton.setText('Camera is live')
    #         frame = q.get()
    #         img = frame["img"]

    #         img_height, img_width, img_colors = img.shape
    #         scale_w = float(self.window_width) / float(img_width)
    #         scale_h = float(self.window_height) / float(img_height)
    #         scale = min([scale_w, scale_h])

    #         if scale == 0:
    #             scale = 1

    #         # img = cv2.resize(img, None, fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
    #         # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #         # height, width, bpc = img.shape
    #         # bpl = bpc * width
    #         image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)
    #         self.ImgWidget.setImage(image)

    def update_frame(self):
        # self.startButton.setText('Camera is live')
        # frame = q.get()
        # img = frame["img"]
        global img
        # img_height, img_width, img_colors = img.shape
        # scale_w = float(self.window_width) / float(640)
        # scale_h = float(self.window_height) / float(480)
        # scale_w = float(self.window_width) / float(img_width)
        # scale_h = float(self.window_height) / float(img_height)
        # scale = min([scale_w, scale_h])

        # if scale == 0:
        #     scale = 1

        # img = cv2.resize(img, None, fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # height, width, bpc = img.shape
        # bpl = bpc * width
        image = QtGui.QImage(img, 640, 480, 1920, QtGui.QImage.Format_RGB888)
        self.ImgWidget.setImage(image)

    # def closeEvent(self, event):
    #     global running
    #     running = False


        # self.setupUi(self)
        # self.pushUp.clicked.connect(self.upCallback)  # Bind the event handlers
        # self.pushDown.clicked.connect(self.downCallback)  #   to the buttons
        # self.pushLeft.clicked.connect(self.leftCallback)
        # self.pushRight.clicked.connect(self.rightCallback)
        # rospy.init_node('camera_ui', anonymous=True)
        # rospy.Subscriber("/image", Image, callback)

    # def upCallback(self):
    #     if myWindow.radUI.isChecked():
    #         urlExecution(0)
    #         time.sleep(0.1)
    #         urlExecution(1)

    # def downCallback(self):
    #     if myWindow.radUI.isChecked():
    #         urlExecution(2)
    #         time.sleep(0.1)
    #         urlExecution(3)

    # def leftCallback(self):
    #     if myWindow.radUI.isChecked():
    #         urlExecution(4)
    #         time.sleep(0.1)
    #         urlExecution(5)

    # def rightCallback(self):
    #     if myWindow.radUI.isChecked():
    #         urlExecution(6)
    #         time.sleep(0.1)
    #         urlExecution(7)


app = QtGui.QApplication(sys.argv)
w = MyWindowClass(None)
# w.setWindowTitle('Kurokesu PyQT OpenCV USB camera test panel')
w.show()
app.exec_()

print("tttt")

if __name__ == '__main__':
    listener()
