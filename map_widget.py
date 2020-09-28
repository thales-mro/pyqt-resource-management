import os, sys
from PyQt5 import QtCore, QtWidgets, QtGui, QtWebEngineWidgets
import resources

class MapWidget(QtWidgets.QWidget):
    """
    Instantiate a map widget
    """

    def __init__(self):
        """
        Build widget elements
        """
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Map Widget')
        self.resize(600, 400)
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        self.setStyleSheet('background-color: rgb(224,224,224);')
        layout = QtWidgets.QGridLayout()

        self.web_browser = QtWebEngineWidgets.QWebEngineView()
        url = QtCore.QUrl("qrc:///map.html")
        self.web_browser.load(url)
        self.web_browser.loadFinished.connect(self.onLoadFinished)

        self.label = QtWidgets.QLabel("Widget Label <>")
        self.button = QtWidgets.QPushButton('Close')
        self.button.clicked.connect(self.close)

        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.web_browser, 1, 0)
        layout.addWidget(self.button, 2, 0)
        self.setLayout(layout)


    def onLoadFinished(self, ok):
        """
        process logic when web page finishes loading
        """
        if ok:
            pass

    
def main():
    """
    Load widget for testing purposes
    """
    app = QtWidgets.QApplication(sys.argv)
    mapWidget = MapWidget()
    mapWidget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
