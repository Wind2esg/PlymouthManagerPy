# Modified .py files for plymouth manager
# Copyright: 2018 Wind2esg 
# License: GPL-3+

import os, sys, shutil, getpass, pickle, stat, subprocess
import gtk, gtk.glade, pygtk
import hwinfo

#function that happen before the start of PM
#get the plymouth status (is it enabled or not?)
def getPlymouthStatus():
	if os.path.exists("/etc/init/plymouth-splash.conf"):
		return 1
	else:
		return 0

#get the resolution in use
def getCurrentRes():
	try:
		tmpBuf = open("/etc/default/" + hwinfo.getBoot(), "r")
		for line in tmpBuf:
			if "GRUB_GFXMODE=" in line:
				return line.split("=")[1].split('\n')[0]
	except:
		return '0'
	
			
#functions for the general tab
def ChangeRes(res):
	if os.path.exists("/etc/default/grub"):
		bl = "grub"

		shutil.copyfile("/etc/default/" + bl, "/home/" + getpass.getuser() + "/." + bl + ".backup")

		sourceFile = open("/home/" + getpass.getuser() + "/." + bl, "w")
	
		tmpBuf = open("/home/" + getpass.getuser() + "/." + bl + ".backup", 'r').read()

	
		for line in tmpBuf.split('\n'):
			if line[0:13] == "GRUB_GFXMODE=":
				line = "GRUB_GFXMODE=" + res + "\n"
			elif line[0:14] == "#GRUB_GFXMODE=":
				line = "GRUB_GFXMODE=" + res + "\n"
			
			sourceFile.write(line + "\n")
	
		sourceFile.close()

		os.system("gksu mv /home/" + getpass.getuser() + "/." + bl + " /etc/default/" + bl)
	

def AbleDisable():
	if os.path.exists("/etc/init/plymouth-splash.conf"):
		os.system("gksu mv /etc/init/plymouth-splash.conf /etc/init/plymouth-splash.conf.disabled")
	elif os.path.exists("/etc/init/plymouth-splash.conf.disabled"):
		os.system("gksu mv /etc/init/plymouth-splash.conf.disabled /etc/init/plymouth-splash.conf")
	else:
		print "ERROR: /etc/init/plymouth-splash.conf & /etc/init/plymouth-splash.conf.disabled don't exist"
		
def Burg():
	if not os.path.exists("/home/" + getpass.getuser() + "/.plymouth-manager.cf"):
		fBurg = open("/home/" + getpass.getuser() + "/.plymouth-manager.cf", "w")
		fBurg.write("[Boot options]\nBOOT_LOADER=burg")
		fBurg.close()
		
def Driver(boot):
	if boot == "grub":
		dir = str(os.getcwd()) + "/../scripts"
		os.system("xterm -e 'cd " + dir + " && sudo ./plymouth-resolution-fix.sh'")
		
	if boot == "burg":
		dir = str(os.getcwd()) + "/../scripts"
		os.system("xterm -e 'cd " + dir + " && sudo ./plymouth-resolution-fix_burg.sh'")

	
#functions for the themes tab
def SelectIcon(value):
	#a and b are casual variables name
	try:
		icons = os.listdir("../themes_preview")
		a = str(value[0])
		b = ((a.replace("(", "")).replace(")", "")).replace(",", "")
		return icons[int(b)].replace(".jpg", "")
	except:
		return ""
	
def Refresh():
	#os.system("cd /usr/share/plymouth-manager/data && gksudo -D\"Update themes list\" (rm themes.txt && sudo wget http://launchpadlibrarian.net/68472604/themes.txt && cd /usr/share/plymouth-manager/themes_preview && sudo rm *.jpg && sudo wget http://launchpadlibrarian.net/68472604/themes_preview.zip && sudo unzip themes_preview.zip && sudo rm themes_preview.zip && cd /usr/share/plymouth-manager/src && sudo rm themescontroller.py && sudo wget http://launchpadlibrarian.net/68472604/themescontroller.py'")
	os.system("echo \"#\!/bin/bash (cd /usr/share/plymouth-manager/data && rm themes.txt && sudo wget http://launchpadlibrarian.net/68472604/themes.txt && cd /usr/share/plymouth-manager/themes_preview && sudo rm *.jpg && sudo wget http://launchpadlibrarian.net/68472604/themes_preview.zip && sudo unzip themes_preview.zip && sudo rm themes_preview.zip && cd /usr/share/plymouth-manager/src && sudo rm themescontroller.py && sudo wget http://launchpadlibrarian.net/68472604/themescontroller.py) | zenity --progress --pulsate)\" > ~/.plymouth-manager && gksudo -D\"Update themes list\" sh ~/.plymouth-manager")
	
def InstallRemove(theme_name, install_remove):
	index = 0
	indexSplit = 0
	themesFile = open("../data/themes.txt", "r")
	themesLines = themesFile.readlines()
	themesFile.close()
	while theme_name not in themesLines[index]:
		index += 1
	if theme_name in themesLines[index]:
		themeSplit = str(themesLines).split("|")
	while theme_name != themeSplit[indexSplit]:
		indexSplit += 1
	if theme_name == themeSplit[indexSplit]:
		if install_remove == "i":	
			os.system("xterm -e " + themeSplit[indexSplit-1])		#system comand to install a theme	
		else:
			os.system("xterm -e " + themeSplit[indexSplit+1])		#system comand to remove a theme
	

def Select():
	os.system("xterm -e 'sudo update-alternatives --config default.plymouth && sudo update-initramfs -u'")
	
def Preview():
	dir = str(os.getcwd()) + "/../scripts"
	os.system("cd " + dir + " && gksu ./plymouth-theme-preview.sh")

#functions for the themes creations tab
def Create(background, logo):
	#creation of the necessary folders
	os.system("xterm -e 'sudo mkdir /usr/share/plymouth/themes/PMtheme'")
	os.system("xterm -e 'sudo cp " + background + " /usr/share/plymouth/themes/PMtheme/background.png'")
	os.system("xterm -e 'sudo cp " + logo + " /usr/share/plymouth/themes/PMtheme/logo.png'")
	os.system("xterm -e 'sudo cp " + os.getcwd() + "/../model/* /usr/share/plymouth/themes/PMtheme")
	
	
	listFile = os.listdir("/usr/share/plymouth/themes/PMtheme")
	for image in listFile:
		os.system("xterm -e 'sudo mv /usr/share/plymouth/themes/PMtheme/" + image + " /usr/share/plymouth/themes/PMtheme/background.png'")
		
	#creation of the necessary file
	#file.plymouth
	filePlymouth = open("/home/" + getpass.getuser() + "/.PMtheme.plymouth", "w")
	textPlymouth = "[Plymouth Theme]\nName=Theme by PM\nDescription=Theme made by Plymouth Manager\nModuleName=script\n[script]\nImageDir=/usr/share/plymouth/themes/PMtheme\nScriptFile=/usr/share/plymouth/themes/PMtheme/PMtheme.script"
	filePlymouth.write(textPlymouth)
	filePlymouth.close()
	os.system("xterm -e 'sudo mv ~/.PMtheme.plymouth /usr/share/plymouth/themes/PMtheme/PMtheme.plymouth'")
	#file.script
	#fileScript = open("/home/" + getpass.getuser() + "/.PMtheme.script", "w")
	#textScript = "wallpaper_image = Image('background.png');\nscreen_width = Window.GetWidth();\nscreen_height = Window.GetHeight();\nresized_wallpaper_image = wallpaper_image.Scale(screen_width,screen_height);\nwallpaper_sprite = Sprite(resized_wallpaper_image);\nwallpaper_sprite.SetZ(-100);"
	#fileScript.write(textPlymouth)
	#fileScript.close()
	#os.system("xterm -e 'sudo mv ~/.PMtheme.script /usr/share/plymouth/themes/PMtheme/PMtheme.script'")
	
def InstallTheme():
	os.system("xterm -e ''sudo update-alternatives --install /usr/share/plymouth/themes/default.plymouth default.plymouth /usr/share/plymouth/themes/PMtheme/PMtheme.plymouth 100 && sudo update-alternatives --config default.plymouth && sudo update-initramfs -u'")


#function for the last tab
def Share(file, preview, name, author, email):
	args = file + " " + preview + " '" + name + "' '" + author + "' " + email
	dir = str(os.getcwd()) + "/../scripts"
	os.system("cd " + dir + " && gksu ./plymouth-theme-preview.sh " + args)
	
#functions for the wndEditor
def Save(Text, File):
	#fileConfig = open(File, "r").read()
	if File == "/usr/share/plymouth/themes/default.plymouth":
		SavingFile = "default.plymouth"
	elif File == "/usr/share/plymouth/themes/text.plymouth":
		SavingFile = "text.plymouth"
	else:
		SavingFile = hwinfo.getBoot()
	fileSaving = open("/home/" +getpass.getuser() + "/." + SavingFile, "w")
	fileSaving.write(Text)
	fileSaving.close()
	if File == "/usr/share/plymouth/themes/default.plymouth":
		os.system("xterm -e 'sudo mv ~/.default.plymouth /usr/share/plymouth/themes/default.plymouth'")
	elif File == "/usr/share/plymouth/themes/text.plymouth":
		os.system("xterm -e 'sudo mv ~/.text.plymouth /usr/share/plymouth/themes/text.plymouth'")
	else:
		os.system("xterm -e 'sudo mv ~/." + hwinfo.getBoot() + " /etc/default/" + hwinfo.getBoot() + "'")


