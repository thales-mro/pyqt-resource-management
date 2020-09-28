import sys
import map_widget
from PyQt5 import QtCore, QtWidgets, QtGui

class Controller:
    """
    pyqt controller boilerplate
    """

    def __init__(self, argv):
        self.app = QtWidgets.QApplication(argv)
        self.map_widget = map_widget.MapWidget()

    
    def launch(self):
        """
        launch method in order to show first widget specified
        """
        self.show_map()
        sys.exit(self.app.exec_())


    def show_map(self):
        """
        launch map widget on screen
        """
        self.map_widget.show()
