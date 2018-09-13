import sys
import time
from PyQt5.QtWidgets import *
from krita import *

class MaterialExporterDocker(DockWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Material Exporter')

		mainWidget = QWidget(self)
		self.setWidget(mainWidget)

		self.export_button = QPushButton("Export")
		self.export_button.clicked.connect(self.export)

		self.base_edit = QLineEdit("/home/jed/j3d/adventure")

		self.model_edit = QLineEdit("model_name")

		self.material_edit = QLineEdit("material_name")
		mainWidget.setLayout(QFormLayout())
		mainWidget.layout().addRow(QLabel("Base Project: "), self.base_edit)
		mainWidget.layout().addRow(QLabel("Model: "), self.model_edit)
		mainWidget.layout().addRow(QLabel("Material: "), self.material_edit)
		mainWidget.layout().addRow(QLabel(""), self.export_button)

	def canvasChanged(self, canvas):
		pass



	def set_base_layers(self, b, nodes):
		for child in nodes:
			child.setVisible(b)

	def set_layer(self, n, b, nodes):
		for child in nodes:
			if str(child.name()) == n:
				child.setVisible(b)


	def export(self):
		doc = Krita.instance().activeDocument()

		root = doc.rootNode()

		nodes = root.childNodes()

		# Texture Library
		base_folder = self.base_edit.text()

		# Character / Piece
		project_folder = self.model_edit.text()
		# Object your working on
		base_name = self.material_edit.text()

		format = '.png'

		doc.setBatchmode(True)

		original_v = []
		for child in nodes:
		    original_v.append(child.visible())

		for child in nodes:
		    if str(child.name()) == 'bg':
		        child.setVisible(True)
		        continue
		    if str(child.name())in ['ao', 'alb', 'rgh', 'mtl', 'emi'] and len(child.childNodes()) > 0:
		        self.set_base_layers(False, nodes)
		        self.set_layer('bg', True, nodes)
	        	child.setVisible(True)
		        doc.refreshProjection()
	        	filename = base_folder + '/' + project_folder + ('/' + base_name)*2 + "_" + str(child.name()) + format
		        print("Saving: " + filename)
	        	doc.saveAs(filename)


		for i in range(len(nodes)):
		    nodes[i].setVisible(original_v[i])

		doc.refreshProjection()
		doc.save()
		doc.setBatchmode(False)

Krita.instance().addDockWidgetFactory(DockWidgetFactory("material_exporter", DockWidgetFactoryBase.DockRight, MaterialExporterDocker))
