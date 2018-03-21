# Modified .py files for plymouth manager
# Copyright: 2018 Wind2esg 
# License: GPL-3+

import gtk
import os

import hwinfo

class Editor:
	def __init__(self):
		
		builder = gtk.Builder()
		builder.add_from_file("../ui/editor.glade")
		go = builder.get_object
		
		self.wndEditor = go("wndEditor")
		self.cmbEditor = go("cmbEditor")
		self.txvEditor = go("txvEditor")
		
		signals = {
			"on_wndEditor_destroy":self.on_btnCancel_clicked,
			"on_btnSave_clicked":self.on_btnSave_clicked,
			"on_btnCancel_clicked":self.on_btnCancel_clicked,
			"on_cmbEditor_changed":self.on_cmbEditor_changed
		}
		
		builder.connect_signals(signals)
		
		#set combobox
		if os.path.isfile("/usr/share/plymouth/themes/default.plymouth"):	
			FileList = ["/usr/share/plymouth/themes/default.plymouth", "/usr/share/plymouth/themes/text.plymouth", "/etc/default/" + hwinfo.getBoot()]
		else:
			FileList = ["/usr/share/plymouth/themes/text.plymouth", "/etc/default/" + hwinfo.getBoot()]
		
		cmbModelScore = gtk.ListStore(str)
		
		for value in FileList:
			iter=cmbModelScore.append()
			cmbModelScore.set_value(iter, 0, value)
			self.cmbEditor.set_model(cmbModelScore)
		cell = gtk.CellRendererText()
		self.cmbEditor.pack_start(cell, True)
		self.cmbEditor.add_attribute(cell, 'text',0)
		self.cmbEditor.set_active(0) # The element is active at 0 position
		
		#set textview
		#get buffer, bound and text
		bufferEditor = self.txvEditor.get_buffer()
		start, end = bufferEditor.get_bounds()	
		file = open(self.cmbEditor.get_active_text(), "r").read()
		bufferEditor.set_text(file)	
		
		
		
	"""functions for the widgets"""
	def on_btnSave_clicked(self, widget):
		#get buffer, bound and text
		bufferEditor = self.txvEditor.get_buffer()
		start, end = bufferEditor.get_bounds()
		Text = bufferEditor.get_text(start, end)
		#get file name
		File = self.cmbEditor.get_active_text()
		funcmain.Save(Text, File)
			
	def on_btnCancel_clicked(self, widget):
		self.wndEditor.hide()
		
	def on_cmbEditor_changed(self, widget):
		#get buffer, bound and text
		bufferEditor = self.txvEditor.get_buffer()
		start, end = bufferEditor.get_bounds()
		file = open(self.cmbEditor.get_active_text(), "r").read()	
		bufferEditor.set_text(file)
		
	"""main function"""		
	def main(self):
		self.wndEditor.show_all()
		#gtk.main()
		
if __name__ == "__main__":
	app = Editor()
	app.main()
