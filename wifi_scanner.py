#!/usr/bin/env python3
import subprocess
import platform
from datetime import datetime
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel,
    QTableWidget, QTableWidgetItem, QHeaderView, QPushButton,
    QHBoxLayout, QMessageBox, QComboBox
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont, QColor

class WiFiScanner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kali Linux Wi-Fi Scanner")
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumSize(700, 500)
        
        # Central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        
        # [Rest of the code from previous implementation]
        # ... [Include all the remaining class methods exactly as shown earlier]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    scanner = WiFiScanner()
    scanner.show()
    sys.exit(app.exec_())
