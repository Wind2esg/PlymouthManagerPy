# Modified .py files for plymouth manager
# Copyright: 2018 Wind2esg 
# License: GPL-3+

import gtk
import os
from platform import dist
import ConfigParser

import hwinfo
import funcmain
import driver
import themescontroller
import editor
import info

import locale
import gettext

APP = 'plymouth-manager'
DIR = "/usr/share/locale/"

locale.setlocale(locale.LC_ALL, '')
gettext.bindtextdomain(APP, DIR)
gettext.textdomain(APP)
_ = gettext.gettext

class PlymouthManager:
	def __init__(self):
		
		builder = gtk.Builder()
		builder.add_from_file("../ui/plymouth-manager.glade")
		go = builder.get_object
		
		self.wndMain = go("wndMain")						#load of wndMain and its widget
		self.cmbResolution = go("cmbResolution")
		self.btnAbleDisable = go("btnAbleDisable")
		self.btnBurg = go("btnBurg")
		self.iconThemes = go("iconThemes")
		self.lblTheme = go("lblTheme")
		self.btnInstallRemove = go("btnInstallRemove")
		self.lblCurrentTheme = go("lblCurrentTheme")
		self.btnPreview = go("btnPreview")
		self.flcBackground = go("flcBackground")
		self.flcLogo = go("flcLogo")
		self.btnCreate = go("btnCreate")
		self.btnInstallTheme = go("btnInstallTheme")
		
		self.label1 = go("label1")
		self.label2 = go("label2")
		self.label3 = go("label3")
		self.label4 = go("label4")
		
		self.lblResolution = go("lblResolution")
		self.btnChangeRes = go("btnChangeRes")
		self.lblAbleDisable = go("lblAbleDisable")
		self.lblDriver = go("lblDriver")
		self.btnDriver = go("btnDriver")
		self.lblEdit = go("lblEdit")
		self.btnEdit = go("btnEdit")
		
		self.lblRefresh = go("lblRefresh")
		self.btnSelect = go("btnSelect")
		self.btnPreview = go("btnPreview")

		self.lblSelection = go("lblSelection")
		self.lblLogo = go("lblLogo")
		self.btnCreate = go("btnCreate")
		self.btnInstallTheme = go("btnInstallTheme")
		
		self.lblSelect = go("lblSelect")
		self.fileSelect = go("fileSelect")
		self.lblPreview = go("lblPreview")
		self.filePreview = go("filePreview")
		self.lblName = go("lblName")
		self.lblAuthor = go("lblAuthor")
		self.lblEmail = go("lblEmail")
		self.btnShare = go("btnShare")
		self.entryName = go("entryName")
		self.entryAuthor = go("entryAuthor")
		self.entryEmail = go("entryEmail")
				
		signals = {
			"on_wndMain_destroy":gtk.main_quit,			
			"on_btnChangeRes_clicked":self.on_btnChangeRes_clicked,			
			"on_btnAbleDisable_clicked":self.on_btnAbleDisable_clicked,
			"on_btnDriver_clicked":self.on_btnDriver_clicked,
			"on_btnEdit_clicked":self.on_btnEdit_clicked,
			"on_btnRefresh_clicked":self.on_btnRefresh_clicked,			
			"on_btnInstallRemove_clicked":self.on_btnInstallRemove_clicked,	
			"on_btnSelect_clicked":self.on_btnSelect_clicked,
			"on_btnPreview_clicked":self.on_btnPreview_clicked,
			"on_iconThemes_selection_changed":self.on_iconThemes_selection_changed,
			"on_iconThemes_size_allocate":self.on_iconThemes_size_allocate,
			"on_btnCreate_clicked":self.on_btnCreate_clicked,					
			"on_btnInstallTheme_clicked":self.on_btnInstallTheme_clicked,
			"on_flcBackground_file_set":self.on_flcBackground_file_set,
			"on_flcLogo_file_set":self.on_flcLogo_file_set,
			"on_itemHelp_activate":self.on_itemHelp_activate,
			"on_btnShare_clicked":self.on_btnShare_clicked						
		}
		
		builder.connect_signals(signals)
		
		self.translate()
		self.inizialize()
	
	"""function to translate the window"""
	def translate(self):
		"""tab labels"""
		self.label1.set_text(_("General"))
		self.label2.set_text(_("Themes"))
		self.label3.set_text(_("Create your theme"))
		self.label4.set_text(_("Share your theme"))
		"""first tab"""
		self.lblResolution.set_text(_("Select your resolution"))
		self.btnChangeRes.set_label(_("Change"))
		self.lblAbleDisable.set_text(_("Enable/Disable Plymouth"))
		self.lblDriver.set_text(_("Make Plymouth compatible with closed source video driver"))
		self.btnDriver.set_label(_("Begin"))
		self.lblEdit.set_text(_("Edit manually the configuration files"))
		self.btnEdit.set_label(_("Edit"))
		"""second tab"""
		self.lblRefresh.set_text(_("Refresh the list of avaible themes"))
		self.btnSelect.set_label(_("Apply an installed theme"))
		self.btnPreview.set_label(_("Preview"))
		self.btnInstallRemove.set_label(_("Install/Remove"))
		"""third"""
		self.lblSelection.set_text(_("Select a png which is not over the 500 Kb for your background..."))
		self.lblLogo.set_text(_("...and now for your logo"))
		self.btnCreate.set_label(_("Create Theme"))
		self.btnInstallTheme.set_label(_("Install"))
		"""fourth"""
		self.lblSelect.set_text(_("Select the theme (*.tar.gz)"))
		self.lblPreview.set_text(_("Select the preview (*.png, *.jpg)"))
		self.lblName.set_text(_("Theme's name"))
		self.lblAuthor.set_text(_("Author"))
		self.lblEmail.set_text(_("Email"))
		self.btnShare.set_label(_("Share"))

	"""Combobox function"""
	def set_combobox(self):
		tmpInfo = hwinfo.getRes()
		
		cmbModelScore = gtk.ListStore(str)
		count = 0
		for value in tmpInfo:
			iter=cmbModelScore.append()
			cmbModelScore.set_value(iter, 0, value)
			self.cmbResolution.set_model(cmbModelScore)
			cell = gtk.CellRendererText()
			if value == funcmain.getCurrentRes():
				self.cmbResolution.set_active(count)
			else:
				count += 1
		self.cmbResolution.pack_start(cell, True)
		self.cmbResolution.add_attribute(cell, 'text',0)
		
	"""IconView function"""
	def set_iconview(self):
		self.icons = os.listdir("../themes_preview")
		
		liststore = gtk.ListStore(gtk.gdk.Pixbuf)
		self.iconThemes.set_model(liststore)
		self.iconThemes.set_pixbuf_column(0)
		
		for icon in self.icons:
			pixbuf = gtk.gdk.pixbuf_new_from_file_at_size("../themes_preview/" + icon, 100, 100)
			liststore.append([pixbuf])
			
	"""generic functions"""
	def get_plymouth_status(self):
		#check plymouth status
		if funcmain.getPlymouthStatus() == 1:
			self.btnAbleDisable.set_label(_("Disable"))
		else:
			self.btnAbleDisable.set_label(_("Enable"))		
			
	def get_current_resolution(self):
		#set the current resolution in the combo box
		self.cmbResolution.set_title(funcmain.getCurrentRes())
		
	def get_current_theme(self):
		#get the plymouth's theme in use
		#if not os.path.isdir("/usr/share/plymouth/themes/default.plymouth"):
		try:
			#get theme's name
			self.fileTheme = ConfigParser.RawConfigParser()					 
			self.fileTheme.read("/usr/share/plymouth/themes/default.plymouth")
			self.Theme = self.fileTheme.get("Plymouth Theme", "Name")
			#set it into the label
			self.lblCurrentTheme.set_label(_("Current theme: ") + self.Theme)
		except:
			self.lblCurrentTheme.set_label(_("Current theme: "))
		#else:
		#	self.btnPreview.set_sensitive(False)
	
	def get_ppa_status(self):
		distro = dist()
		if os.path.exists("/etc/apt/sources.list.d/mefrio-g-plymouthmanager-" + distro[2] + ".list"):
			return 0
		else:
			os.system("gksudo -D=\"Add ppa and update source.list\" apt-add-repository ppa:mefrio-g/plymouthmanager && (sudo apt-get update) | zenity --progress --pulsate")
		
	"""function to inizializate plymouth manager"""
	def inizialize(self):
		self.set_combobox()
		self.set_iconview()
		self.get_plymouth_status()
		self.get_current_resolution()
		self.get_current_theme()
		self.get_ppa_status()
		
	"""buttons and widgets functions for the first tab"""
	def on_btnChangeRes_clicked(self, widget):
		funcmain.ChangeRes(self.cmbResolution.get_active_text())
            
	def on_btnAbleDisable_clicked(self, widget):
		funcmain.AbleDisable()
		self.get_plymouth_status()

	def on_btnDriver_clicked(self, widget):
		d_app = driver.Driver()
		d_app.main()

	def on_btnEdit_clicked(self, widget):
		e_app = editor.Editor()
		e_app.main()
		
	"""buttons and widgets functions for the second tab"""
	def on_btnRefresh_clicked(self, widget):
		funcmain.Refresh()
		self.set_iconview()
	
	def on_btnInstallRemove_clicked(self, widget):
		funcmain.InstallRemove(self.lblTheme.get_label(), self.InstallRemoveTheme)
		self.get_current_theme()		
						
	def on_btnSelect_clicked(self, widget):
		funcmain.Select()				

	def on_btnPreview_clicked(self, widget):
		funcmain.Preview()
		
	def on_iconThemes_selection_changed(self, widget):
		self.lblTheme.set_label( funcmain.SelectIcon(self.iconThemes.get_selected_items()) )
		if themescontroller.ControllTheme(self.lblTheme.get_label()) == 1:
			self.btnInstallRemove.set_label(_("Remove"))
			self.InstallRemoveTheme = "r"
		else:
			self.btnInstallRemove.set_label(_("Install"))
			self.InstallRemoveTheme = "i"
					
	def on_iconThemes_size_allocate(self, object, rectangle):
		 columns = int(rectangle.width/(self.iconThemes.get_columns()*2))
		 self.iconThemes.set_columns(columns)
	
	"""buttons and widgets functions for the third tab"""
	def on_flcBackground_file_set(self, widget): 
		if  (self.flcBackground.get_filename()[-3:-1] + self.flcBackground.get_filename()[-1]) == "png":
			self.btnCreate.set_sensitive(True)
			self.btnInstallTheme.set_sensitive(True)	
			self.background = self.flcBackground.get_filename()
		else:
			self.btnCreate.set_sensitive(False)
			self.btnInstallTheme.set_sensitive(False)
				
	def on_flcLogo_file_set(self, widget):
		if  (self.flcLogo.get_filename()[-3:-1] + self.flcLogo.get_filename()[-1]) == "png":
			self.btnCreate.set_sensitive(True)
			self.btnInstallTheme.set_sensitive(True)	
			self.logo = self.flcLogo.get_filename()
		else:
			self.btnCreate.set_sensitive(False)
			self.btnInstallTheme.set_sensitive(False)		
		
	def on_btnCreate_clicked(self, widget):
		funcmain.Create(self.background, self.logo)
		
	def on_btnInstallTheme_clicked(self, widget):
		funcmain.InstallTheme()
		self.get_current_theme
		
	"""buttons and widgets functions for the fourth tab"""
	def on_btnShare_clicked(self, widget):
		funcmain.Share( self.fileSelect.get_filename(), self.filePreview.get_filename(), self.entryName.get_text(), 
			self.entryAuthor.get_text(), self.entryEmail.get_text() 
		)
	
	"""menubar function"""
	def on_itemHelp_activate(self, widget):
		i_app = info.Info()
		i_app.main()
	
	"""main function"""
	def main(self):
		self.wndMain.show_all()
		gtk.main()
		
if __name__ == "__main__":
	app = PlymouthManager()
	app.main()
