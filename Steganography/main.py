from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import numpy as np
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QPlainTextEdit, QFileDialog, QGraphicsView, QPushButton, QFrame, QProgressBar
from PyQt5.QtCore import QRect, Qt, QSize, QEventLoop, QThread, pyqtSignal
import os
import time

class Ui_SaveDecode(object):
    def setupUi(self, SaveDecode):
        if not SaveDecode.objectName():
            SaveDecode.setObjectName(u"SaveDecode")
        SaveDecode.setWindowModality(Qt.ApplicationModal)
        SaveDecode.resize(1920, 1080)
        icon = QIcon()
        icon.addFile(u"../Desktop/undefined - Imgur.png", QSize(), QIcon.Normal, QIcon.Off)
        SaveDecode.setWindowIcon(icon)
        SaveDecode.setAutoFillBackground(False)
        SaveDecode.setSizeGripEnabled(False)
        self.EncPhoto = QGraphicsView(SaveDecode)
        self.EncPhoto.setObjectName(u"EncPhoto")
        self.EncPhoto.setGeometry(QRect(870, 40, 331, 241))
        self.EncPhoto.setStyleSheet(u"\n"
                                    "	selection-background-color:#f39c12;\n"
                                    "	background-color:#000000;\n"
                                    "	border: 1px solid #C0DB50;\n"
                                    "	color: #a9b7c6;")
        self.encPhotoButton = QPushButton(SaveDecode)
        self.encPhotoButton.setObjectName(u"encPhotoButton")
        self.encPhotoButton.setGeometry(QRect(990, 290, 93, 28))
        self.encPhotoButton.setStyleSheet(u"QPushButton{\n"
                                          "	border-style: solid;\n"
                                          "	border-color: #050a0e;\n"
                                          "	border-width: 1px;\n"
                                          "	border-radius: 5px;\n"
                                          "	color: #d3dae3;\n"
                                          "	padding: 2px;\n"
                                          "	background-color: #100E19;\n"
                                          "}\n"
                                          "QPushButton::default{\n"
                                          "	border-style: solid;\n"
                                          "	border-color: #050a0e;\n"
                                          "	border-width: 1px;\n"
                                          "	border-radius: 5px;\n"
                                          "	color: #FFFFFF;\n"
                                          "	padding: 2px;\n"
                                          "	background-color: #151a1e;\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "	border-style: solid;\n"
                                          "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
                                          "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
                                          "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
                                          "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, s"
                                          "top:1 #100E19);\n"
                                          "	border-width: 2px;\n"
                                          "    border-radius: 1px;\n"
                                          "	color: #d3dae3;\n"
                                          "	padding: 2px;\n"
                                          "}\n"
                                          "QPushButton:pressed{\n"
                                          "	border-style: solid;\n"
                                          "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
                                          "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
                                          "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                          "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                          "	border-width: 2px;\n"
                                          "    border-radius: 1px;\n"
                                          "	color: #d3dae3;\n"
                                          "	padding: 2px;\n"
                                          "}")
        self.EncodedPhoto = QGraphicsView(SaveDecode)
        self.EncodedPhoto.setObjectName(u"EncodedPhoto")
        self.EncodedPhoto.setGeometry(QRect(1380, 40, 331, 241))
        self.EncodedPhoto.setStyleSheet(u"\n"
                                        "	selection-background-color:#f39c12;\n"
                                        "	background-color:#000000;\n"
                                        "	border: 1px solid #C0DB50;\n"
                                        "	color: #a9b7c6;")
        self.DecPhoto = QGraphicsView(SaveDecode)
        self.DecPhoto.setObjectName(u"DecPhoto")
        self.DecPhoto.setGeometry(QRect(290, 700, 441, 241))
        self.DecPhoto.setStyleSheet(u"\n"
                                    "	selection-background-color:#f39c12;\n"
                                    "	background-color:#000000;\n"
                                    "	border: 1px solid #C0DB50;\n"
                                    "	color: #a9b7c6;")
        self.decPhoButton = QPushButton(SaveDecode)
        self.decPhoButton.setObjectName(u"decPhoButton")
        self.decPhoButton.setGeometry(QRect(450, 950, 93, 28))
        self.decPhoButton.setStyleSheet(u"QPushButton{\n"
                                        "	border-style: solid;\n"
                                        "	border-color: #050a0e;\n"
                                        "	border-width: 1px;\n"
                                        "	border-radius: 5px;\n"
                                        "	color: #d3dae3;\n"
                                        "	padding: 2px;\n"
                                        "	background-color: #100E19;\n"
                                        "}\n"
                                        "QPushButton::default{\n"
                                        "	border-style: solid;\n"
                                        "	border-color: #050a0e;\n"
                                        "	border-width: 1px;\n"
                                        "	border-radius: 5px;\n"
                                        "	color: #FFFFFF;\n"
                                        "	padding: 2px;\n"
                                        "	background-color: #151a1e;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "	border-style: solid;\n"
                                        "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
                                        "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
                                        "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
                                        "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, s"
                                        "top:1 #100E19);\n"
                                        "	border-width: 2px;\n"
                                        "    border-radius: 1px;\n"
                                        "	color: #d3dae3;\n"
                                        "	padding: 2px;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "	border-style: solid;\n"
                                        "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
                                        "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
                                        "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                        "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                        "	border-width: 2px;\n"
                                        "    border-radius: 1px;\n"
                                        "	color: #d3dae3;\n"
                                        "	padding: 2px;\n"
                                        "}")
        self.CommitDecode = QPushButton(SaveDecode)
        self.CommitDecode.setObjectName(u"CommitDecode")
        self.CommitDecode.setGeometry(QRect(910, 790, 141, 41))
        self.CommitDecode.setStyleSheet(u"QPushButton{\n"
                                        "	border-style: solid;\n"
                                        "	border-color: #050a0e;\n"
                                        "	border-width: 1px;\n"
                                        "	border-radius: 5px;\n"
                                        "	color: #d3dae3;\n"
                                        "	padding: 2px;\n"
                                        "	background-color: #100E19;\n"
                                        "}\n"
                                        "QPushButton::default{\n"
                                        "	border-style: solid;\n"
                                        "	border-color: #050a0e;\n"
                                        "	border-width: 1px;\n"
                                        "	border-radius: 5px;\n"
                                        "	color: #FFFFFF;\n"
                                        "	padding: 2px;\n"
                                        "	background-color: #151a1e;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "	border-style: solid;\n"
                                        "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
                                        "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
                                        "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
                                        "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, s"
                                        "top:1 #100E19);\n"
                                        "	border-width: 2px;\n"
                                        "    border-radius: 1px;\n"
                                        "	color: #d3dae3;\n"
                                        "	padding: 2px;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "	border-style: solid;\n"
                                        "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
                                        "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
                                        "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                        "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                        "	border-width: 2px;\n"
                                        "    border-radius: 1px;\n"
                                        "	color: #d3dae3;\n"
                                        "	padding: 2px;\n"
                                        "}")
        self.CommitEncode = QPushButton(SaveDecode)
        self.CommitEncode.setObjectName(u"CommitEncode")
        self.CommitEncode.setGeometry(QRect(1500, 290, 93, 28))
        self.CommitEncode.setStyleSheet(u"QPushButton{\n"
                                        "	border-style: solid;\n"
                                        "	border-color: #050a0e;\n"
                                        "	border-width: 1px;\n"
                                        "	border-radius: 5px;\n"
                                        "	color: #d3dae3;\n"
                                        "	padding: 2px;\n"
                                        "	background-color: #100E19;\n"
                                        "}\n"
                                        "QPushButton::default{\n"
                                        "	border-style: solid;\n"
                                        "	border-color: #050a0e;\n"
                                        "	border-width: 1px;\n"
                                        "	border-radius: 5px;\n"
                                        "	color: #FFFFFF;\n"
                                        "	padding: 2px;\n"
                                        "	background-color: #151a1e;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "	border-style: solid;\n"
                                        "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
                                        "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
                                        "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
                                        "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, s"
                                        "top:1 #100E19);\n"
                                        "	border-width: 2px;\n"
                                        "    border-radius: 1px;\n"
                                        "	color: #d3dae3;\n"
                                        "	padding: 2px;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "	border-style: solid;\n"
                                        "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
                                        "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
                                        "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                        "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                        "	border-width: 2px;\n"
                                        "    border-radius: 1px;\n"
                                        "	color: #d3dae3;\n"
                                        "	padding: 2px;\n"
                                        "}")
        self.pushButton = QPushButton(SaveDecode)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1410, 950, 93, 28))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
                                      "	border-style: solid;\n"
                                      "	border-color: #050a0e;\n"
                                      "	border-width: 1px;\n"
                                      "	border-radius: 5px;\n"
                                      "	color: #d3dae3;\n"
                                      "	padding: 2px;\n"
                                      "	background-color: #100E19;\n"
                                      "}\n"
                                      "QPushButton::default{\n"
                                      "	border-style: solid;\n"
                                      "	border-color: #050a0e;\n"
                                      "	border-width: 1px;\n"
                                      "	border-radius: 5px;\n"
                                      "	color: #FFFFFF;\n"
                                      "	padding: 2px;\n"
                                      "	background-color: #151a1e;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "	border-style: solid;\n"
                                      "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
                                      "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
                                      "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
                                      "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, s"
                                      "top:1 #100E19);\n"
                                      "	border-width: 2px;\n"
                                      "    border-radius: 1px;\n"
                                      "	color: #d3dae3;\n"
                                      "	padding: 2px;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "	border-style: solid;\n"
                                      "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
                                      "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
                                      "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                      "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                      "	border-width: 2px;\n"
                                      "    border-radius: 1px;\n"
                                      "	color: #d3dae3;\n"
                                      "	padding: 2px;\n"
                                      "}")
        self.encText = QPlainTextEdit(SaveDecode)
        self.encText.setObjectName(u"encText")
        self.encText.setGeometry(QRect(250, 40, 461, 241))
        self.encText.setStyleSheet(u"\n"
                                   "	selection-background-color:#f39c12;\n"
                                   "	background-color:#000000;\n"
                                   "	border: 1px solid #C0DB50;\n"
                                   "	color: #a9b7c6;")
        self.DecodedText = QPlainTextEdit(SaveDecode)
        self.DecodedText.setObjectName(u"DecodedText")
        self.DecodedText.setGeometry(QRect(1220, 700, 501, 241))
        self.DecodedText.setStyleSheet(u"\n"
                                       "	selection-background-color:#f39c12;\n"
                                       "	background-color:#000000;\n"
                                       "	border: 1px solid #C0DB50;\n"
                                       "	color: #a9b7c6;")
        self.TerminalOutput = QPlainTextEdit(SaveDecode)
        self.TerminalOutput.setObjectName(u"TerminalOutput")
        self.TerminalOutput.setGeometry(QRect(80, 390, 1801, 241))
        self.TerminalOutput.setStyleSheet(u"\n"
                                          "	selection-background-color:#f39c12;\n"
                                          "	background-color:#000000;\n"
                                          "	border: 1px solid #C0DB50;\n"
                                          "	color: #a9b7c6;")
        self.frame = QFrame(SaveDecode)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, -1, 2011, 1181))
        self.frame.setStyleSheet(
            u"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(88, 0, 255, 255))")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txtButton = QPushButton(self.frame)
        self.txtButton.setObjectName(u"txtButton")
        self.txtButton.setGeometry(QRect(420, 290, 111, 28))
        self.txtButton.setStyleSheet(u"QPushButton{\n"
                                     "	border-style: solid;\n"
                                     "	border-color: #050a0e;\n"
                                     "	border-width: 1px;\n"
                                     "	border-radius: 5px;\n"
                                     "	color: #d3dae3;\n"
                                     "	padding: 2px;\n"
                                     "	background-color: #100E19;\n"
                                     "}\n"
                                     "QPushButton::default{\n"
                                     "	border-style: solid;\n"
                                     "	border-color: #050a0e;\n"
                                     "	border-width: 1px;\n"
                                     "	border-radius: 5px;\n"
                                     "	color: #FFFFFF;\n"
                                     "	padding: 2px;\n"
                                     "	background-color: #151a1e;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "	border-style: solid;\n"
                                     "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
                                     "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
                                     "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
                                     "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, s"
                                     "top:1 #100E19);\n"
                                     "	border-width: 2px;\n"
                                     "    border-radius: 1px;\n"
                                     "	color: #d3dae3;\n"
                                     "	padding: 2px;\n"
                                     "}\n"
                                     "QPushButton:pressed{\n"
                                     "	border-style: solid;\n"
                                     "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
                                     "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
                                     "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                     "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                     "	border-width: 2px;\n"
                                     "    border-radius: 1px;\n"
                                     "	color: #d3dae3;\n"
                                     "	padding: 2px;\n"
                                     "}")

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(570, 330, 760, 40))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
                                       "background-color: rgb(200,200,200);\n"
                                       "color: rgb(170,85,127);\n"
                                       "border-style:solid;\n"
                                       "border-radius: 10px;\n"
                                       "text-align: center;\n"
                                       "}\n"
                                       "QProgressBar::chunk{\n"
                                       "border-radius: 10px;\n"
                                       "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(118, 62, 167, 255), stop:1 rgba(64, 136, 167, 255));\n"
                                       "\n"
                                       "}")

        self.resetButton = QPushButton(self.frame)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(920, 880, 93, 28))
        self.resetButton.setStyleSheet(u"QPushButton{\n"
                                       "	border-style: solid;\n"
                                       "	border-color: #050a0e;\n"
                                       "	border-width: 1px;\n"
                                       "	border-radius: 5px;\n"
                                       "	color: #d3dae3;\n"
                                       "	padding: 2px;\n"
                                       "	background-color: #100E19;\n"
                                       "}\n"
                                       "QPushButton::default{\n"
                                       "	border-style: solid;\n"
                                       "	border-color: #050a0e;\n"
                                       "	border-width: 1px;\n"
                                       "	border-radius: 5px;\n"
                                       "	color: #FFFFFF;\n"
                                       "	padding: 2px;\n"
                                       "	background-color: #151a1e;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "	border-style: solid;\n"
                                       "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
                                       "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
                                       "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
                                       "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, s"
                                       "top:1 #100E19);\n"
                                       "	border-width: 2px;\n"
                                       "    border-radius: 1px;\n"
                                       "	color: #d3dae3;\n"
                                       "	padding: 2px;\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "	border-style: solid;\n"
                                       "	border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
                                       "    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
                                       "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                       "    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
                                       "	border-width: 2px;\n"
                                       "    border-radius: 1px;\n"
                                       "	color: #d3dae3;\n"
                                       "	padding: 2px;\n"
                                       "}")
        self.frame.raise_()
        self.progressBar.setValue(0)
        self.EncPhoto.raise_()
        self.EncodedPhoto.raise_()
        self.encPhotoButton.raise_()
        self.EncodedPhoto.raise_()
        self.DecPhoto.raise_()
        self.decPhoButton.raise_()
        self.CommitDecode.raise_()
        self.CommitEncode.raise_()
        self.pushButton.raise_()
        self.encText.raise_()
        self.DecodedText.raise_()
        self.TerminalOutput.raise_()

        self.retranslateUi(SaveDecode)
        self.encoding_completed = False
        QtCore.QMetaObject.connectSlotsByName(SaveDecode)

        # Connect the buttons to the functions in the LSB steganography app
        self.txtButton.clicked.connect(self.select_text)
        self.encPhotoButton.clicked.connect(self.select_image_for_encoding)
        self.decPhoButton.clicked.connect(self.select_image_for_decoding)
        self.CommitDecode.clicked.connect(self.decode_image)
        self.CommitEncode.clicked.connect(self.encode_text)
        self.pushButton.clicked.connect(self.save_decoded_text)
        self.resetButton.clicked.connect(self.reset_ui)
        # Initialize variables for image and text
        self.img = None
        self.text = ""

        self.timer_running = False
        self.timer_start = 0
        self.loss_time = 0

    def start_timer(self):
        self.timer_start = time.time()
        self.timer_running = True

    def stop_timer(self):
        self.timer_running = False

    def elapsed_time(self):
        if self.timer_running:
            return time.time() - self.timer_start
        else:
            return 0
    def retranslateUi(self, SaveDecode):
        _translate = QtCore.QCoreApplication.translate
        SaveDecode.setWindowTitle(_translate("SaveDecode", "LSB Stego Encoder/Decoder"))
        self.txtButton.setText(_translate("SaveDecode", "Select your text"))
        self.encText.setPlainText(_translate("SaveDecode", "Please select your text "))
        self.encPhotoButton.setText(_translate("SaveDecode", "Photo Select"))
        self.decPhoButton.setText(_translate("SaveDecode", "Photo select"))
        self.DecodedText.setPlainText(_translate("SaveDecode", "Decoded Text"))
        self.CommitDecode.setText(_translate("SaveDecode", "Decode"))
        self.CommitEncode.setText(_translate("SaveDecode", "Encode"))
        self.TerminalOutput.setPlainText(_translate("SaveDecode", "Outputs:"))
        self.pushButton.setText(_translate("SaveDecode", "Save Text"))
        self.resetButton.setText(_translate("reset_ui", "Reset"))

    def reset_ui(self):
        # Reset image and text variables
        self.img = None
        self.text = ""

        # Clear UI elements
        self.encText.setPlainText("Please select your text ")
        self.EncPhoto.setScene(None)
        self.DecPhoto.setScene(None)
        self.TerminalOutput.setPlainText("Outputs:")
        self.DecodedText.setPlainText("Decoded Text")
        self.progressBar.setValue(0)

    def select_text(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Text File", "",
                                                             "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'r') as file:
                self.text = file.read()
            self.encText.setPlainText(f"Selected Text: {self.text}")
            self.update_terminal_output(f"Selected Text: {file_name}")
            self.update_terminal_output(f"Text is selected please proceed with selecting photo")

    def update_terminal_output(self, message):
        current_text = self.TerminalOutput.toPlainText()

        try:
            # Attempt to decode as hexadecimal
            formatted_message = bytes.fromhex(message).decode('utf-8', errors='replace')
        except ValueError:
            # If decoding fails, display the original message
            formatted_message = message

        self.TerminalOutput.setPlainText(current_text + formatted_message + "\n")

        # Scroll down to the bottom after adding new text
        scrollbar = self.TerminalOutput.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

        # Ensure the GUI updates immediately
        QtWidgets.QApplication.processEvents(QtCore.QEventLoop.ExcludeUserInputEvents)

    def select_image_for_encoding(self):
        self.progressBar.setValue(0)
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Image for Encoding", "", "Image Files (*.png *.jpg *.bmp);;All Files (*)", options=options
        )
        if file_name:
            self.img = Image.open(file_name)

            # Store the last selected image
            self.last_selected_image = self.img.copy()

            # Scale the image to fit within the QGraphicsView dimensions
            pixmap = self.get_scaled_pixmap(file_name, self.EncPhoto.width(), self.EncPhoto.height())

            self.EncPhoto.setScene(QtWidgets.QGraphicsScene())
            self.EncPhoto.scene().addPixmap(pixmap)
            self.update_terminal_output(f"Selected Photo: {file_name}")
            self.update_terminal_output(f"Image is selected please proceed with encoding")



    def get_scaled_pixmap(self, file_name, width, height):
        original_pixmap = QtGui.QPixmap(file_name)
        return original_pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)

    def select_image_for_decoding(self):
        self.progressBar.setValue(0)
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Image for Decoding", "", "Image Files (*.png *.jpg *.bmp);;All Files (*)", options=options
        )
        if file_name:
            self.img = Image.open(file_name)

            # Scale the image to fit within the QGraphicsView dimensions
            pixmap = self.get_scaled_pixmap(file_name, self.DecPhoto.width(), self.DecPhoto.height())

            self.DecPhoto.setScene(QtWidgets.QGraphicsScene())
            self.DecPhoto.scene().addPixmap(pixmap)
            self.update_terminal_output(f"Selected Photo: {file_name}")
            self.update_terminal_output(f"Image is selected please proceed with decoding")
    def decode_image(self):
        if self.img:

            self.timer_start = time.time()
            decoded_message = self.decode_LSB(self.img, "L$B")
            self.DecodedText.setPlainText(f"Decoded Text: {decoded_message}")
            self.update_terminal_output(f"Decoding Completed")
            elapsed_time = time.time() - self.timer_start
            self.update_terminal_output(f"Decoding Time: {elapsed_time:.2f} seconds")

            # Update progress bar to indicate completion
            self.progressBar.setValue(100)

    def encode_text(self, filename):
        if self.img and self.text:
            text_to_encode = self.text + "L$B"
            binary_text = ''.join(format(ord(char), '08b') for char in text_to_encode)

            counter = 1  # Counter for naming multiple images
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog

            total_iterations = len(binary_text)
            current_iteration = 0

            while binary_text:
                self.timer_start = time.time()
                self.img, binary_index = self.calculate_LSB(self.img, binary_text)
                self.update_terminal_output(f"Step {counter} Encoding in Progress...")
                self.loss_time = time.time()
                # Save the stego image
                self.save_stego_image(self.img, filename)
                loss_time_a = time.time() - self.loss_time
                elapsed_time = time.time() - self.timer_start
                elapsed_time = elapsed_time - loss_time_a
                self.update_terminal_output(f"Encoding Time: {elapsed_time:.2f} seconds")
                # Update progress bar
                current_iteration += binary_index
                progress_value = int((current_iteration / total_iterations) * 100)
                self.progressBar.setValue(progress_value)

                # Update the EncodedPhoto with the current stego image
                self.update_encoded_photo(filename)

                binary_text = binary_text[binary_index:]
                counter += 1

                if binary_text and counter > 1:
                    loss_time_a = time.time() - self.loss_time
                    img_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None, "Select Another Image for Encoding", "",
                        "Image Files (*.png *.jpg *.bmp);;All Files (*) a",
                        options=options)
                    if img_path:
                        self.img = Image.open(img_path)
                    else:
                        self.update_terminal_output(f"Process has been stopped by the user ")
                        self.progressBar.setValue(0)
                        break

                    if binary_text:
                        self.text = self.text[binary_index:] + "L$B"

                # Update the GUI
                chunk_size = 8
                chunks = [binary_text[i:i + chunk_size] for i in range(binary_index, len(binary_text), chunk_size)]
                ascii_text = "".join(chr(int(chunk, 2)) for chunk in chunks)
                self.update_terminal_output(f"Remaining Text: {ascii_text}")
                self.update_terminal_output(f"Binary Index: {binary_index}")
                if binary_text:
                    self.update_terminal_output(
                        f"Image was not enough. Please select a new image to continue from remaining.")
                else:
                    self.update_terminal_output(f"Encoding Completed")

                # Allow the GUI to update
                QtWidgets.QApplication.processEvents(QtCore.QEventLoop.ExcludeUserInputEvents)

    def update_encoded_photo(self, filename):
        # Update the EncodedPhoto QGraphicsView with the current stego image
        if filename:
            img = Image.open(filename)
            pixmap = self.get_scaled_pixmap(filename, self.EncodedPhoto.width(), self.EncodedPhoto.height())
            self.EncodedPhoto.setScene(QtWidgets.QGraphicsScene())
            self.EncodedPhoto.scene().addPixmap(pixmap)
            self.update_terminal_output(f"Selected Photo: {filename}")
            self.update_terminal_output(f"Image is selected please proceed with encoding")

    def save_decoded_text(self):
        decoded_text = self.DecodedText.toPlainText()
        if decoded_text:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            file_name, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save Decoded Text", "",
                                                                 "Text Files (*.txt);;All Files (*)", options=options)
            if file_name:
                with open(file_name, 'w') as file:
                    file.write(decoded_text)
                    self.update_terminal_output(f"Selected Photo: {file_name}")
                    self.update_terminal_output(f"Text is saved successfully")

    def decode_LSB(self, image, key):
        width, height = image.size
        binary_text = ""
        current_binary = ""
        key_txt = ''.join(format(ord(char), '08b') for char in key)

        total_iterations = width * height * 3
        current_iteration = 0

        for y in range(height):
            for x in range(width):
                pixel = list(image.getpixel((x, y))[:3])
                for c in range(3):
                    current_binary += str(pixel[c] & 1)
                    current_iteration += 1

                    # Update progress bar
                    progress_value = int((current_iteration / total_iterations) * 100)
                    self.progressBar.setValue(progress_value)

                    if len(current_binary) == 8:
                        binary_text += current_binary
                        if binary_text.endswith(key_txt):
                            decoded_message = "".join(
                                chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text), 8) if
                                i + 8 <= len(binary_text)
                            )

                            decoded_message = decoded_message.replace(key, "")
                            return decoded_message
                        current_binary = ""
        decoded_message = "".join(
            chr(int(binary_text[i:i + 8], 2)) for i in range(0, len(binary_text), 8) if i + 8 <= len(binary_text)
        )

        decoded_message = decoded_message.replace(key, "")
        return decoded_message

    def calculate_LSB(self, image, binary_text):
        image = image.convert("RGB")
        width, height = image.size
        array = np.array(list(image.getdata()))

        total_pixels = array.size // 3
        total_bits = total_pixels * 3
        max_characters = total_bits // 8

        if len(binary_text) > total_bits:
            self.update_terminal_output(
                f"Warning: Text may not be fully hidden in the image. It exceeds the image capacity.")
        binary_index = 0
        for y in range(height):
            for x in range(width):
                if binary_index < len(binary_text):
                    pixel = list(image.getpixel((x, y))[:3])
                    for c in range(3):
                        if binary_index < len(binary_text):
                            pixel[c] = (pixel[c] & 254) | int(binary_text[binary_index])
                            binary_index += 1
                    image.putpixel((x, y), tuple(pixel))
                else:
                    break

        return image, binary_index

    def save_stego_image(self, image, filename):
        if self.img:
            # Ask the user to enter a custom name for the encoded image
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save Encoded Image", "",
                                                                "Image Files (*.png);;All Files (*)", options=options)

            if filename:
                try:
                    self.img.save(filename)
                    self.update_terminal_output(f"Stego image saved as {filename}")
                    print(f"Encoding Completed flag set to: {self.encoding_completed}")

                except Exception as e:
                    self.update_terminal_output(f"Error: {e}")
                    self.update_terminal_output(f"An error occurred while trying to save the stego image.")
                    print(f"Error saving stego image: {e}")

            else:
                self.update_terminal_output("Saving process has been stopped by the user")
                print(f"Encoding Completed flag reset to: {self.encoding_completed}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SaveDecode = QtWidgets.QDialog()
    ui = Ui_SaveDecode()
    ui.setupUi(SaveDecode)
    SaveDecode.show()
    SaveDecode.showMaximized()
    sys.exit(app.exec_())