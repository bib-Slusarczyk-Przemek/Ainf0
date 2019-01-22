import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class HelloWorld (QWidget):
	def __init__ (self, parent=None):
		super (HelloWorld, self).__init__(parent)
		
		#Textfeld
		nameLabel = QLabel ("Bitte klicke diesen Button!")
		
		#Button
		button = QPushButton ("Mitteilung")
		button.setFont(QFont('Times New Roman', 20))
		button.clicked.connect (self.buttonGeklickt)
		button.setToolTip ('Das ist eine <b>Schaltfläche</b>')
		
		#Fensterlayout
		mainLayout = QVBoxLayout()
		mainLayout.addWidget(nameLabel)
		mainLayout.addWidget(button)
		self.setLayout(mainLayout)
		
		#Fenstertitel und -größe
		self.setWindowTitle("Hello World!")
		self.resize(500,300)
		
	def buttonGeklickt (self):
		QMessageBox.information(self, "Mitteilung", "Hello World!")
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	
	screen = HelloWorld()
	screen.show()
	result = app.exec_()
	sys.exit(result)