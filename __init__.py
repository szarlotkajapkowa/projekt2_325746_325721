# -*- coding: utf-8 -*-
"""
/***************************************************************************
 wtyczka_projekt2
                                 A QGIS plugin
 wtyczka_projekt2
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-06-06
        copyright            : (C) 2024 by Maciej
        email                : 01179132@pw.edu.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):
    from .myplugin import MyPlugin
    return MyPlugin(iface)
