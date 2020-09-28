import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from controller import Controller


def main():
    controller = Controller(sys.argv)
    controller.launch()

if __name__ == '__main__':
    main()