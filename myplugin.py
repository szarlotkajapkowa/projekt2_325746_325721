# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:08:19 2024

@author: User
"""

import os
from PyQt5 import QtWidgets, uic
from qgis.core import QgsProject
from qgis.utils import iface

import os
from PyQt5 import QtWidgets, uic
from qgis.core import QgsProject, QgsGeometry, QgsPointXY, QgsWkbTypes, QgsFeature
from qgis.utils import iface

class MyPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.dialog = MyPluginDialog()

    def initGui(self):
        self.action = QtWidgets.QAction("wtyczka_projekt2", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&wtyczka_projekt2", self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("&wtyczka_projekt2", self.action)

    def run(self):
        self.dialog.populate_layers()
        self.dialog.show()

class MyPluginDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), 'wtyczka_projekt2_dialog_base.ui'), self)
        self.calculateDifferenceButton.clicked.connect(self.calculate_difference)
        self.calculateAreaButton.clicked.connect(self.calculate_area)

    def populate_layers(self):
        self.layerComboBox.clear()
        layers = [layer for layer in QgsProject.instance().mapLayers().values() if layer.type() == QgsWkbTypes.PointGeometry]
        for layer in layers:
            self.layerComboBox.addItem(layer.name(), layer)

    def calculate_difference(self):
        layer = self.layerComboBox.currentData()
        if layer is None:
            iface.messageBar().pushMessage("Error", "No layer selected", level=2)
            return

        selected_features = layer.selectedFeatures()
        iface.messageBar().pushMessage("Debug", f"Selected features count: {len(selected_features)}", level=0)

        if len(selected_features) != 2:
            iface.messageBar().pushMessage("Error", "Select exactly 2 points", level=2)
            return

        try:
            height1 = selected_features[0]['wysokosc']
            height2 = selected_features[1]['wysokosc']
        except KeyError as e:
            iface.messageBar().pushMessage("Error", f"KeyError: {str(e)}", level=2)
            return

        result = abs(height1 - height2)
        iface.messageBar().pushMessage("Result", f"Height difference between points {selected_features[0].id()} and {selected_features[1].id()} is {result} meters", level=0)

    def calculate_area(self):
        layer = self.layerComboBox.currentData()
        if layer is None:
            iface.messageBar().pushMessage("Error", "No layer selected", level=2)
            return

        selected_features = layer.selectedFeatures()
        if len(selected_features) < 3:
            iface.messageBar().pushMessage("Error", "Select at least 3 points", level=2)
            return

        points = [feature.geometry().asPoint() for feature in selected_features]
        area = self.gauss_area(points)
        iface.messageBar().pushMessage("Result", f"Area of the polygon with points {[f.id() for f in selected_features]} is {area} square meters", level=0)

    def gauss_area(self, points):
        n = len(points)
        area = 0.0
        for i in range(n):
            x1, y1 = points[i].x(), points[i].y()
            x2, y2 = points[(i + 1) % n].x(), points[(i + 1) % n].y()
            area += x1 * y2 - x2 * y1
        return abs(area) / 2.0
