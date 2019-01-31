# Copyright (C) 2019 Kyaw Kyaw Htike @ Ali Abdul Ghafur. All rights reserved.
import glob
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def qt_browse_directory(parent_widget=None, text_display="Select Directory"):
    return str(QtWidgets.QFileDialog.getExistingDirectory(parent_widget, text_display))
# def qt_browse_single_file(parent_widget=None, text_display='Open file', ini_directory='c:\', str_filter='Image files(*.jpg *.gif)'):' \
#                                                                                                                                  '  return QtWidgets.QFileDialog.getOpenFileName(parent_widget, text_display, ini_directory, str_filter)[0]
# def qt_browse_multiple_files(parent_widget=None, text_display='Open files', ini_directory='c:\', str_filter='Image files(*.jpg *.gif)'):
#     return QtWidgets.QFileDialog.getOpenFileNames(parent_widget, text_display, ini_directory, str_filter)[0]

#######################################
# For Form_MainWin.ui file:
#######################################

from ui_Form_MainWin import Ui_Form_MainWin

class Form_MainWin(QtWidgets.QMainWindow):  # or class Form_MainWin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_MainWin()
        self.ui.setupUi(self)

    def browse_folder(self):
        self.dir_sel = qt_browse_directory(self)
        self.ui.label_folderSelected.setText(self.dir_sel)

    def generate_sigs(self):
        dir_input_header_files = self.dir_sel
        str_define_sdk = self.ui.lineEdit_sdkApiDefine.text()
        fpaths_input_header_files = glob.glob(os.path.join(dir_input_header_files, '*.h'))

        str_display = []
        len_str_define_sdk = len(str_define_sdk)
        # fid_out = open(fpath_output_header_file, 'w')

        for fpath_input_header_file in fpaths_input_header_files:
            fid = open(fpath_input_header_file, 'r')
            header_file_contents = fid.readlines()
            fid.close()
            for cur_line in header_file_contents:
                # print(cur_line)
                cur_line = cur_line.strip(' \t\n\r')
                if (cur_line[0:len_str_define_sdk] == str_define_sdk):
                    str_display.append(cur_line[len_str_define_sdk+1:])
        # fid_out.close()
        self.ui.textEdit_outputGen.setText('\n'.join(str_display))

        #######################################
# Main application start
#######################################

app = QtWidgets.QApplication(sys.argv)
qwin = Form_MainWin()
qwin.show()
sys.exit(app.exec_())




