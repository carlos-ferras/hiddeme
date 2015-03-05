#!/usr/bin/env python2

import pygtk
pygtk.require('2.0')
import gtk
import os
import commands
gtk.gdk.threads_init()

class Pomodoro:
	def __init__(self):
		self.userHome()
		self.icon=gtk.status_icon_new_from_file('icon')
		self.set_state(self.loadState())
		self.icon.connect('activate',self.icon_click)
		self.icon.set_visible(True)
		
	def userHome(self):
		a=str(commands.getoutput('$HOME'))
		b=a.split('/')
		del b[0]
		c=b[-1].split()
		del b[-1]
		if len(c)>1:
			d=c[0].split(':')
			e=d[0]
		else:
			e=c[0]
		home=''
		for i in b:
			home+='/'+i
		home+='/'+e
		self.home=home+'/'
		
	def loadState(self):
		try:
			a=str(commands.getoutput('$HOME'))
			file=open(self.home+'.state.conf','r')
			state=file.readline()
			if state=='on' or state=='off':
				return state
			else:
				return 'on'
		except:
			return 'on'
		
	def saveState(self,state):
		file=open(self.home+'.state.conf','w+')
		file.write(state)
		return True

	def set_state(self,state):
		self.icon.set_from_file(self.icon_directory()+state+".png")
		if state == "off":
			self.icon.set_tooltip("Iconos desactivados")
		else:
			self.icon.set_tooltip("Iconos activados")
		self.state=state

	def icon_directory(self):
		return os.path.dirname(os.path.realpath(__file__)) + os.path.sep
		
	def icon_click(self,dummy):
		if self.state == "off":
			os.system('gsettings set org.gnome.desktop.background show-desktop-icons true')
			self.set_state("on")
			self.saveState('on')
		else:
			os.system('gsettings set org.gnome.desktop.background show-desktop-icons false')
			self.set_state("off")
			self.saveState('off')
			
	def main(self):
		gtk.main()

if __name__ == "__main__":
    app = Pomodoro()
    app.main()
