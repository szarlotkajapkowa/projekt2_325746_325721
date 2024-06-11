# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:08:51 2024

@author: User
"""

# myplugin_dialog.py
from PyQt5 import QtWidgets, uic

class MyPluginDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('myplugin_dialog_base.ui', self)
