#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp1254 -*-

import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *

a = (":#><`$|{[]}@.,;!^+&/()=?_%-* ~abcdefghijklmnopqrstwyzuvxUABCDEFGHIJKLMNOQPRSTWXVYZ1234567890'" + "\\" + "\""+u"ĞÜŞÇÖİğüşıöç" + u"é£¨æß")

class DaVinci(QWidget):
	def __init__(self, parent=None):
	
		QWidget.__init__(self,parent)
		self.setGeometry(300,200,600,400)
		self.setWindowTitle(u"DaVinci (Şifreleme ve Deşifreleme)")
		self.setWindowIcon(QIcon(".\\anonymous.png"))
		self.KLabel = QLabel("Anahtar Kelime:",self)
		self.TLabel = QLabel(u"Metin Ekranı:",self)
		self.RLabel = QLabel(u"Sonuç Ekranı:",self)
		self.EButton = QPushButton(u"Şifrele")
		self.DButton = QPushButton(u"Deşifrele")
		self.KEdit = QLineEdit(self)
		self.TEdit = QTextEdit(self)
		self.REdit = QPlainTextEdit(self)
		self.REdit.setReadOnly(1)
		self.connect(self.EButton,SIGNAL("clicked()"),self.Encrypt)
		self.connect(self.DButton,SIGNAL("clicked()"),self.Decrypt)
		self.grid = QGridLayout()
		self.grid.setSpacing(10)
		self.grid.addWidget(self.KLabel,0,0)
		self.grid.addWidget(self.TLabel,1,0)
		self.grid.addWidget(self.RLabel,2,0)
		self.grid.addWidget(self.KEdit,0,1)
		self.grid.addWidget(self.TEdit,1,1)
		self.grid.addWidget(self.REdit,2,1)
		self.grid.addWidget(self.EButton,3,1)
		self.grid.addWidget(self.DButton,4,1)
		self.setLayout(self.grid)
		
	def Encrypt(self):
		key = unicode(self.KEdit.text())
		word = unicode(self.TEdit.toPlainText())
		word = len(key) * " " + ":" + word
		son = ""
		i = 0
		for k in word:
			if i >= len(key):
					i = 0
			if a.find(k) + a.find(key[i]) + 1 >= len(a):
				son = son + a[a.find(k) + a.find(key[i]) - len(a)]
			else:
				son = son + a[a.find(k) + a.find(key[i])]
				
			i = i + 1
		
		self.REdit.setPlainText(son)
		
	def Decrypt(self):
		key = unicode(self.KEdit.text())
		word = unicode(self.TEdit.toPlainText())
		son = ""
		i = 0
		for k in word:
			if i >= len(key):
					i = 0
			if a.find(k) - a.find(key[i]) + 1 < 0:
				son = son + a[a.find(k) - a.find(key[i]) + len(a)]
			else:
				son = son + a[a.find(k) - a.find(key[i])]
			i = i + 1
		son = son[len(key) + 1:]
		self.REdit.setPlainText(son)

app = QApplication(sys.argv)
DaVinci = DaVinci()
DaVinci.show()
sys.exit(app.exec_())
