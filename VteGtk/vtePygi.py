#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk, Vte, GLib
import os

__author__ = "Chiheb NeXus"

class Signal():
	"""
	Les signaux de notre programme
	"""
	def onUpdate(self, update):
		"""
		Update repositories
		"""
		# os.getcwd() : permet de retourner une chaîne de caractère qui contient le chemin du dossier 
		# qui contient notre fichier.py
		directory = os.getcwd()
		# command contient une commande Gnu/Linux : cd chemin
		# le \n prmet de faire un retour à la ligne => un appuit sur la touche entrer
		command = "cd "+ directory +"\n"
		# feed_child(command, len(command)) permet de passer une commande au /bin/bash (ou /bin/sh) 
		VteExample.terminal.feed_child(command, len(command))
		run = "./loginscreen.sh\n"
		VteExample.terminal.feed_child(run, len(run))

	def onRelease(self, release):
		"""
		Show Distributor ID, Description, Release, Codename 
		"""
		command = "lsb_release -a\n"
		
		VteExample.terminal.feed_child(command, len(command))


	def onKernelVersion(self, version):
		"""
		Show Gnu/Linux Kernel Version
		"""
		command = "uname -r\n"
		VteExample.terminal.feed_child(command, len(command))

	def onKernelInformations(self, information):
		"""
		Show Gnu/Linux Kernel informations 
		"""
		command = "uname -a\n"
		VteExample.terminal.feed_child(command, len(command))

	def onWirlessInformations(self, winformation):
		"""
		Show network informations
		"""
		command = "ifconfig\n"
		VteExample.terminal.feed_child(command, len(command))

	def onNetworkInformations(self, ninformation):
		"""
		Show Wirless informations
		"""
		command = "iwconfig\n"
		VteExample.terminal.feed_child(command, len(command))

	def onGedit(self, gedit):
		"""
		Open Gedit
		"""
		command = "gedit\n"
		VteExample.terminal.feed_child(command, len(command))

	def onUser(self, chrome):
		"""
		Whoami
		"""
		command = "whoami\n"
		VteExample.terminal.feed_child(command, len(command))

	def onFreeSpace(self, firefox):
		"""
		Free disk space
		"""
		command = "free\n"
		VteExample.terminal.feed_child(command, len(command))

class VteExample(Gtk.Window):
	"""
	Main class
	"""

	def __init__(self):
		"""
		La méthode __init__ sera appelée au lancement de notre app et qui sera notre UI par défaut
		"""
		# Initialisation de Gtk.Window => Initialisation de VteExample vu qu'il hérite toutes les méthodes de Gtk.Window
		Gtk.Window.__init__(self)

		# Builder est l'objet(widget) de type Gtk.Builder
		builder = Gtk.Builder()
		# Ajouter le chemin du fichier XML générée pr glade
		builder.add_from_file("vte.glade")
		# Connecter notre objet Builder à notre classe Signal qui abrite nos signaux
		builder.connect_signals(Signal())
		# window est l'objet nommé window dans glade
		# On va l'extraire pour y faire des modifications
		window = builder.get_object("window")
		window.connect("delete-event", Gtk.main_quit)
		# box est l'objet box utilisé par glade
		# On va l'extraire pour y faire des modifications
		box = builder.get_object("box")

		# Déclaration de l'objet VteExample qui est un Vte.Terminal()
		VteExample.terminal = Vte.Terminal()

		try:
			"""
			Connecter Vte à /bin/bash (on peut utiliser /bin/sh) en utilisant Vte.PtyFlags.DEFAULT et GLib.SpawnFlags.DO_NOT_REAP_CHILD
			Nb: terminal.fork_command_full a été changé par terminal.spawn_sync dans la nouvelle version de GTK+.
			    Mais pour que ce tuto fonctionne correctement sur toutes les machines et pour toutes les configurations
			    la boucle try ... except essayera de déterminer la fonction correcte présente dans votre OS.
			"""
			VteExample.terminal.spawn_sync(
				Vte.PtyFlags.DEFAULT,
				os.environ['HOME'],
				["/bin/bash"],                     # si la version de Vte >=0.38
				[],
				GLib.SpawnFlags.DO_NOT_REAP_CHILD,
				None,
				None)
		except:
			VteExample.terminal.fork_command_full(
				Vte.PtyFlags.DEFAULT,
				os.environ['HOME'],                # Si la version de Vte < 0.38
				["/bin/bash"],
				[],
				GLib.SpawnFlags.DO_NOT_REAP_CHILD,
				None,
				None
				)

		# Ajouter VteExample.terminal au widget box
		box.add(VteExample.terminal)
		# Tout afficher dans le widget window
		window.show_all()

if __name__=='__main__':
	# win est un objet de Type VteExample()
	win = VteExample()
	# Lancement de la boucle infinie de Gtk 
	Gtk.main()
