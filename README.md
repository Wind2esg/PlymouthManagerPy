# PlymouthManagerPy

Modified ,py files for playmouth manager to make it working in Ubuntu 16.04LTS.

Actually it is a good and convinent tool for you to manager your plymouth themes which was shown to you after grub. Huge themes provided for you to customize the appearance during during the booting process.

However, it stoped maintained in 2011. I found it and modified its python code to make it able to serve you again in Ubuntu 16.04LTS

When using plymouth manager, if you see python errors, this might help.

## plymouth manager

It isn't recommanded to install plymouth manager by ppa source.

Better download .deb from [SourceForge.net](https://sourceforge.net/projects/plymouthmanager/) . Then
```
sudo dpkg -i plymouth-manager.deb
```
If you lack some dependencies, try
```
sudo apt-get -f install dependency
```

## download modified .py files from github repo
```
git clone https://www.github.com/Wind2esg/PlymouthManagerPy
```
## replace files.
```
cd PlymouthManagerPy
sudo mv *.py /usr/share/plymouth-manager/src
```

## go

Search from dash or type `plymouth-manager` in your shell

# DO NOT try those options related to plymouth compatibility. 

## The software plymouth manager is licensed under GPL-3+. 
