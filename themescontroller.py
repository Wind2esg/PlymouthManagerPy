# Modified .py files for plymouth manager
# Copyright: 2018 Wind2esg 
# License: GPL-3+


import os

def ControllTheme(theme_name):
	if theme_name == "Azenis" and os.path.exists("/usr/share/plymouth/themes/azenis"):
		return 1
	elif theme_name == "Dm Ubuntu" and os.path.exists("/usr/share/plymouth/themes/DM_Ubuntu"):
		return 1
	elif theme_name == "Earth Sunrise" and os.path.exists("/usr/share/plymouth/themes/earth-sunrise"):
		return 1
	elif theme_name == "Elementary Logo One" and os.path.exists("/usr/share/plymouth/themes/elementary-logo"):
		return 1
	elif theme_name == "Elementary Logo Two" and os.path.exists("/usr/share/plymouth/themes/elementary-logo2"):
		return 1
	elif theme_name == "Glow" and os.path.exists("/usr/share/plymouth/themes/glow"):
		return 1
	elif theme_name == "Internauta" and os.path.exists("/usr/share/plymouth/themes/Internauta"):
		return 1
	elif theme_name == "Internauta 2000" and os.path.exists("/usr/share/plymouth/themes/internauta2000"):
		return 1
	elif theme_name == "Kmint" and os.path.exists("/usr/share/plymouth/themes/Kmint"):
		return 1
	elif theme_name == "Kubuntu Logo" and os.path.exists("/usr/share/plymouth/themes/kubuntu-logo"):
		return 1
	elif theme_name == "Lubuntu Logo" and os.path.exists("/usr/share/plymouth/themes/lubuntu-logo"):
		return 1
	elif theme_name == "MIB" and os.path.exists("/usr/share/plymouth/themes/MIB-Ubuntu"):
		return 1
	elif theme_name == "MIB Oxygen" and os.path.exists("/usr/share/plymouth/themes/MIBOxygen"):
		return 1
	elif theme_name == "MIB Kubuntu" and os.path.exists("/usr/share/plymouth/themes/MIB-Kubuntu"):
		return 1
	elif theme_name == "Orange" and os.path.exists("/usr/share/plymouth/themes/orange"):
		return 1
	elif theme_name == "Paw OSX" and os.path.exists("/usr/share/plymouth/themes/Paw-OSX"):
		return 1
	elif theme_name == "Paw Arch" and os.path.exists("/usr/share/plymouth/themes/paw-arch"):
		return 1
	elif theme_name == "Plymouth 10.10" and os.path.exists("/usr/share/plymouth/themes/ubuntu_plymouth_1010"):
		return 1	
	elif theme_name == "Sabily" and os.path.exists("/usr/share/plymouth/themes/sabily"):
		return 1
	elif theme_name == "Seven" and os.path.exists("/usr/share/plymouth/themes/7"):
		return 1
	elif theme_name == "Solar" and os.path.exists("/usr/share/plymouth/themes/solar"):
		return 1
	elif theme_name == "Space Sunrise" and os.path.exists("/usr/share/plymouth/themes/space-sunrise"):
		return 1
	elif theme_name == "Stargate" and os.path.exists("/usr/share/plymouth/themes/Stargate"):
		return 1
	elif theme_name == "Sunrise" and os.path.exists("/usr/share/plymouth/themes/sunrise"):
		return 1
	elif theme_name == "Texans" and os.path.exists("/usr/share/plymouth/themes/Texans"):
		return 1
	elif theme_name == "Ubuntu Logo" and os.path.exists("/usr/share/plymouth/themes/ubuntu-logo"):
		return 1
	elif theme_name == "Ubuntu New" and os.path.exists("/usr/share/plymouth/themes/newsplash"):
		return 1
	elif theme_name == "Ubuntu Studio" and os.path.exists("/usr/share/plymouth/themes/ubuntustudio-logo"):
		return 1
	elif theme_name == "Xubuntu Logo" and os.path.exists("/usr/share/plymouth/themes/xubuntu-logo"):
		return 1
	elif theme_name == "AzenisBuntu" and os.path.exists("/usr/share/plymouth/themes/AzenisBuntu"):
		return 1
	elif theme_name == "Ubuntu Green One" and os.path.exists("/usr/share/plymouth/themes/Ubuntu_green"):
		return 1
	elif theme_name == "Ubuntu Green Two" and os.path.exists("/usr/share/plymouth/themes/Ubuntu_GREEN_2.1"):
		return 1
	elif theme_name == "Ubuntu Pink One" and os.path.exists("/usr/share/plymouth/themes/U-p"):
		return 1
	elif theme_name == "Ubuntu Pink Two" and os.path.exists("/usr/share/plymouth/themes/U-p_2"):
		return 1
	elif theme_name == "Fun With Linux One" and os.path.exists("/usr/share/plymouth/themes/Fun_With_LinuxU"):
		return 1
	elif theme_name == "Fun With Linux Two" and os.path.exists("/usr/share/plymouth/themes/Fun_With_Linux_2"):
		return 1
	elif theme_name == "Wheat" and os.path.exists("/usr/share/plymouth/themes/wheat"):
		return 1
	elif theme_name == "Ubuntu Logo Women" and os.path.exists("/usr/share/plymouth/themes/ubuntu-logo-women"):
		return 1
	elif theme_name == "Mint Logo" and os.path.exists("/usr/share/plymouth/themes/mint-logo"):
		return 1
	elif theme_name == "Mud World Black" and os.path.exists("/usr/share/plymouth/themes/mud-world-black"):
		return 1
	elif theme_name == "Mud World Blue" and os.path.exists("/usr/share/plymouth/themes/mud-world-blue"):
		return 1
	elif theme_name == "Narwhals" and os.path.exists("/usr/share/plymouth/themes/Narwhals"):
		return 1
	elif theme_name == "Spinfinity" and os.path.exists("/usr/share/plymouth/themes/spinfinity"):
		return 1
	elif theme_name == "Spinfinity Mint One" and os.path.exists("/usr/share/plymouth/themes/spinfinity-mint-01"):
		return 1
	elif theme_name == "Spinfinity Mint Two" and os.path.exists("/usr/share/plymouth/themes/spinfinity-mint-02"):
		return 1
	elif theme_name == "Mint Sunrise" and os.path.exists("/usr/share/plymouth/themes/mint-sunrise"):
		return 1
	elif theme_name == "Mint Does Seven" and os.path.exists("/usr/share/plymouth/themes/mintdoes7"):
		return 1
	elif theme_name == "Lmint" and os.path.exists("/usr/share/plymouth/themes/Lmint"):
		return 1
	elif theme_name == "LMDE" and os.path.exists("/usr/share/plymouth/themes/LMDE"):
		return 1
	elif theme_name == "Satanic" and os.path.exists("/usr/share/plymouth/themes/satanic"):
		return 1
	elif theme_name == "Script" and os.path.exists("/usr/share/plymouth/themes/script"):
		return 1
	elif theme_name == "Linux Is Sexy" and os.path.exists("/usr/share/plymouth/themes/linux-is-sexy"):
		return 1
	elif theme_name == "Int Mint" and os.path.exists("/usr/share/plymouth/themes/INT-MINT"):
		return 1
	elif theme_name == "Fade In" and os.path.exists("/usr/share/plymouth/themes/fade-in"):
		return 1
		
	else:
		return 0