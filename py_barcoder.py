from barcode import EAN13
from barcode.writer import ImageWriter
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys 




class Window(QtWidgets.QWidget):
	"""docstring for Window"""
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Python Barcode Generator") 
		self.setGeometry(300,200, 50, 40)
		self.UiComponents()
		self.show()

	def UiComponents(self):
		
		self.label1 = QLabel("Enter the number to Generate Barcode")
		self.generate_btn = QPushButton("Generate")
		self.save_btn = QPushButton("Save")
		self.type_space = QLineEdit()
		self.label2 = QLabel("")

		v_box = QVBoxLayout()
		v_box.addWidget(self.label1)
		v_box.addWidget(self.type_space)
		v_box.addWidget(self.save_btn)
		
		self.save_btn.clicked.connect(lambda x : self.saveFunc(self.type_space.text()))


		self.setLayout(v_box)


	def saveFunc(self,text):
		try:

			name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',"Imagefile Files")
			name = name[0]
			self.text = text
			my_code = EAN13(self.text, writer=ImageWriter())
			my_code.save(name)
			
		except Exception as e:
			return



	
if __name__ == '__main__':
	
	App = QApplication(sys.argv)
	window = Window()
	sys.exit(App.exec())	

